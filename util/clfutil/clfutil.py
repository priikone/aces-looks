#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CLF utility
"""

from __future__ import division

import os
import io
import pathlib
import sys
import array
import optparse
import re
import xml.etree.ElementTree as et

__copyright__ = 'Copyright (C) 2021 Pekka Riikonen'
__email__ = 'priikone@iki.fi'

__major_version__ = '0'
__minor_version__ = '4'
__change_version__ = '0'
__version__ = '.'.join((__major_version__, __minor_version__,
                        __change_version__))

__all__ = [
    'clfprint', 'clf2dctl', 'clf2ocio', 'main'
]

def clfprint(filename):
    """
    Parse and pretty-print CLF file to a buffer and return it.
    """

    tree = et.parse(filename)
    root = tree.getroot()

    buf = ''
    desc = 'No description'
    idesc = ''
    odesc = ''
    revision = ''
    name = root.attrib['name'] if 'name' in root.attrib else ''
    acesname = ''
    acestrid = ''
    copyr = ''

    # Parse the general information before printing, stripping out
    # the namespace which ET always includes in the tag.
    for child in root:
        tag = re.sub(r'^{.*}', '', child.tag)
        if tag == 'Description':
            desc = child.text
        elif tag == 'InputDescriptor':
            idesc = child.text
        elif tag == 'OutputDescriptor':
            odesc = child.text
        elif tag == 'Info':
            for sub in child:
                stag = re.sub(r'^{.*}', '', sub.tag)
                if stag == 'Revision':
                    revision = sub.text
                elif stag == 'ACESuserName':
                    acesname = sub.text
                elif stag == 'ACEStransformID':
                    acestrid = sub.text
                elif stag == 'Copyright':
                    copyr = sub.text

    if acesname:
        buf += "%16s: %s\n" % ('Name', acesname)
    elif name:
        buf += "%16s: %s\n" % ('Name', name)
    buf += "%16s: %s\n" % ('Description', desc)
    if revision:
        buf += "%16s: %s\n" % ('Revision', revision)
    if acestrid:
        buf += "%16s: %s\n" % ('ACEStransformID', acestrid)
    if copyr:
        buf += "%16s: %s\n" % ('Copyright', copyr)
    if idesc:
        buf += "%16s: %s\n" % ('Input', idesc)

    for child in root:
        tag = re.sub(r'^{.*}', '', child.tag)
        if tag == 'Description' or tag == 'InputDescriptor' or tag == 'OutputDescriptor' or tag == 'Info':
            continue

        for sub in child:
            stag = re.sub(r'^{.*}', '', sub.tag)
            if stag != 'Description':
                buf += "%16s: %s\n" % (tag, 'No description')
            else:
                buf += "%16s: %s\n" % (tag, sub.text)
            break

    if odesc:
        buf += "%16s: %s" % ('Output', odesc)

    buf += "\n"
    return buf


def clf2ocio(filename, aces_ver=2):
    """
    Print OCIO config Look entry from the CLF file and return it.
    """

    tree = et.parse(filename)
    root = tree.getroot()

    filename = os.path.basename(filename)
    buf = '  - !<Look>\n'
    name = root.attrib['name'] if 'name' in root.attrib else ''
    acesname = ''
    desc = ''
    acestrid = ''

    # Parse the general information before printing, stripping out
    # the namespace which ET always includes in the tag.
    for child in root:
        tag = re.sub(r'^{.*}', '', child.tag)
        if tag == 'Description':
            desc = child.text
        elif tag == 'Info':
            for sub in child:
                stag = re.sub(r'^{.*}', '', sub.tag)
                if stag == 'ACESuserName':
                    acesname = sub.text
                elif stag == 'ACEStransformID':
                    acestrid = sub.text

    if acesname:
        buf += "    %s: %s\n" % ('name', acesname)
    elif name:
        buf += "    %s: %s\n" % ('name', name)

    buf += '    process_space: ACES - ACES2065-1\n'
    if desc:
        buf += '    description: |\n'
        buf += '      %s\n' % desc
        if acestrid:
            buf += '\n'
            buf += '      ACEStransformID: %s\n' % acestrid
            buf += '\n'
            buf += '      AMF Components\n'
            buf += '      --------------\n'
            buf += '      ACEStransformID: %s\n' % acestrid
    buf += '    transform: !<FileTransform> {src: ACES%dLooks/CLF/%s}\n' % (aces_ver, filename)

    return buf


def clf2dctl(filename, lut_scaling=False):
    """
    Generate Davinci CTL (DCTL) file from CLF file. Creates a new DCTL file and
    any possible LUT files.
    """

    clfbuf = clfprint(filename)
    buf = (
"/* This file is automagically generated by clfutil %s from %s */\n"
"/*\n"
"    Source: https://github.com/priikone/aces-looks\n\n"
"%s"
"*/\n\n") % (__version__, os.path.basename(filename), clfbuf)

    # Append DCTL template
    f = open(pathlib.Path(__file__).parent / 'lmt.tmpl', "r")
    buf += f.read()

    tree = et.parse(filename)
    root = tree.getroot()
    fname = os.path.basename(filename).split('.')[0]

    # Generate LUT files (.cube) and define them in DCTL
    prevtag = None
    prevchild = None
    min_in = max_in = ''
    num_1d = 0
    num_3d = 0
    for child in root:
        tag = re.sub(r'^{.*}', '', child.tag)
        if lut_scaling == False and tag == 'Range' and ('style' not in child.attrib or child.attrib['style'] != 'Clamp'):
            # If <Range> precedes a LUT assume it's for scaling for the LUT and the scale instead is
            # used in the LUT. User must know what to do and can use --lut-scaling option to override.
            for sub in child:
                stag = re.sub(r'^{.*}', '', sub.tag)
                if stag == 'minInValue':
                    min_in = sub.text
                elif stag == 'maxInValue':
                    max_in = sub.text
        elif tag == 'LUT1D' or tag == 'LUT3D':
            # halfDomain LUT1D not supported right now
            for sub in child:
                stag = re.sub(r'^{.*}', '', sub.tag)
                if stag != 'Array':
                    continue
                size = sub.attrib['dim'].split(' ')[0]
                dim = sub.attrib['dim'].split(' ')[1]

                lutbuf = "# This file is automagically generated by clfutil %s from %s\n" % (__version__, os.path.basename(filename))
                if tag == 'LUT1D':
                    lutbuf += "LUT_1D_SIZE %s\n" % size
                    if prevtag == 'Range' and min_in and max_in:
                        lutbuf += "LUT_1D_INPUT_RANGE %s %s\n" % (min_in, max_in)
                        root.remove(prevchild)

                    if num_1d > 0:
                        name = "%s_%s_%d.cube" % (fname, tag, num_1d)
                    else:
                        name = "%s_%s.cube" % (fname, tag)
                    buf += "DEFINE_LUT(%s%d" % (tag, num_1d) + ', ../ACEScct_LUT/%s)\n' % name
                    num_1d += 1
                else:
                    lutbuf += "LUT_3D_SIZE %s\n" % size
                    if prevtag == 'Range' and min_in and max_in:
                        lutbuf += "LUT_3D_INPUT_RANGE %s %s\n" % (min_in, max_in)
                        root.remove(prevchild)

                    if num_3d > 0:
                        name = "%s_%s_%d.cube" % (fname, tag, num_3d)
                    else:
                        name = "%s_%s.cube" % (fname, tag)
                    buf += "DEFINE_LUT(%s%d" % (tag, num_3d) + ', ../ACEScct_LUT/%s)\n' % name
                    num_3d += 1

                if dim == '3' or tag == 'LUT3D':
                    lutbuf += sub.text
                else:
                    f = io.StringIO(sub.text)
                    for line in f:
                        line = re.sub(r'\t', ' ', line)
                        line = re.sub(r'\n', '', line)
                        lutbuf += "%s %s %s\n" % (line, line, line)

                f = open(name, "w")
                f.write(lutbuf)
        prevtag = tag
        prevchild = child

    buf += "\n"
    buf += (
"__DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B)\n"
"{\n"
"  float3 rgb = make_float3(p_R, p_G, p_B);\n\n")

    # Generate the code (NOTE: full CLF spec not supported as of yet)
    min_in = max_in = min_out = max_out = 0.0
    num_1d = 0
    num_3d = 0
    for child in root:
        tag = re.sub(r'^{.*}', '', child.tag)
        if tag == 'Range':
            if 'style' not in child.attrib or child.attrib['style'] == 'NoClamp':
                clamp = 0
            elif 'style' in child.attrib and child.attrib['style'] == 'Clamp':
                clamp = 1
            else:
                clamp = 0

            for sub in child:
                stag = re.sub(r'^{.*}', '', sub.tag)
                if stag == 'minInValue':
                    min_in = sub.text
                elif stag == 'maxInValue':
                    max_in = sub.text
                elif stag == 'minOutValue':
                    min_out = sub.text
                elif stag == 'maxOutValue':
                    max_out = sub.text
            # Some of this could be pre-computed into constants
            buf += "  rgb = range(rgb, %sf, %sf, %sf, %sf, %d);\n" % (min_in, max_in, min_out, max_out, clamp)
        elif tag == 'LUT1D':
            buf += "  rgb = APPLY_LUT(rgb.x, rgb.y, rgb.z, LUT1D%d);\n" % num_1d
            num_1d += 1
        elif tag == 'LUT3D':
            buf += "  rgb = APPLY_LUT(rgb.x, rgb.y, rgb.z, LUT3D%d);\n" % num_3d
            num_3d += 1
        elif tag == 'Log':
            # For now this only detects ACEScct and doesn't actually implement the different log formulas
            for sub in child:
                stag = re.sub(r'^{.*}', '', sub.tag)
                if stag == 'LogParams':
                    if ('logSideSlope' in sub.attrib and 'logSideOffset' in sub.attrib and 'linSideBreak' in sub.attrib and
                        sub.attrib['logSideSlope'] == "0.05707762557" and sub.attrib['logSideOffset'] == "0.5547945205" and sub.attrib['linSideBreak'] == "0.0078125"):
                        if child.attrib['style'] == 'cameraLinToLog':
                            buf += "  rgb = lin2ACEScct(rgb);\n"
                        else:
                            buf += "  rgb = ACEScct2lin(rgb);\n"
                    else:
                        print("Error: Unsupported Log formula, DCTL will not work")
        elif tag == 'Matrix':
            # For now 3x4 matrix not supported
            for sub in child:
                stag = re.sub(r'^{.*}', '', sub.tag)
                if stag != 'Array':
                    continue

                buf += "  rgb = mult_f3_f33(rgb, make_float3x3("

                count = 0
                f = io.StringIO(sub.text)
                for line in f:
                    line = line.strip()
                    if line == '':
                        continue
                    m = [x for x in line.split(' ') if x.strip()]
                    buf += "make_float3(%sf, %sf, %sf)" % (m[0], m[1], m[2])
                    if count < 2:
                        buf += ", "
                    count += 1
                buf += "));\n"
        elif tag == 'Description' or tag == 'InputDescriptor' or tag == 'OutputDescriptor' or tag == 'Info':
            continue
        else:
            print("Error: Unsupported node %s, DCTL will not work" % tag)

    buf += (
"\n"
"  return rgb;\n"
"}\n")

    f = open(fname + ".dctl", "w")
    f.write(buf)


def main():
    """
    CLF utility main function
    """

    p = optparse.OptionParser(
        description='',
        prog='clfutil',
        version='0.4.0',
        usage='clfutil [options] [info|dctl|ocio] <clf-file>')

    p.add_option('--lut-scaling', '-s', nargs=0, default=False)
    p.add_option('--aces-ver', '-a', nargs=1, default=2)

    options, arguments = p.parse_args()

    if len(arguments) < 2:
        print('clfutil: missing argument')
        sys.exit()

    cmd = arguments[0];
    filename = arguments[1];

    if not os.path.exists(filename):
        print('%s: No such file or directory' % filename)
        sys.exit()

    if cmd == 'info':
        buf = clfprint(filename)
        print(buf, end = "")
    elif cmd == 'ocio':
        buf = clf2ocio(filename, options.aces_ver)
        print(buf, end = "")
    elif cmd == 'dctl':
        clf2dctl(filename, options.lut_scaling)
    else:
        print('clfutil: Unknown command: %s' % cmd)
        sys.exit()

if __name__ == '__main__':
    main()
