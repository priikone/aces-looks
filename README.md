# LMTs for ACES

ACESLooks is a set of LMTs for ACES versions 1.1, 1.2 and 1.3.  The purpose of the LMTs is to provide a sensible starting point for color grading, rather than providing a *final look* as looks/LUTs often do.
All the LMTs can be used anywhere in the grading stack/node tree.  All the LMTs are high dynamic range (20+ stops) and have wide gamut (ACEScg AP1).  The LMTs are available as
[CLF v3 files](https://acescentral.com/knowledge-base-2/common-lut-format-clf/), Davinci CTL (DCTL) files, and as 3D and 1D LUTs (for most of them).

## LMTs

The LMTs are categorized with a filename prefix as follows:

 - **M-XXX**: Emulation (or "Masquerade") LMTs.  These LMTs emulate a pre-existing look (like a DRT) as well as possible.  For ordinary surface colors they provide excellent match.
   For higher luminance and higher saturation levels they differ from the original.  This is mainly because the LMTs have higher dynamic range and wider color gamut.
 - **C-XXX**: Colorimetric LMTs.  These LMTs change *scene colorimetry*, but doesn't change contrast or exposure.  They also retain saturation over the entire luminance range.  They are a
   convenient and fast way to change scene colors without changing anything else.
 - **T-XXX**: Tone-curve LMTs.  These LMTs provide different types of tone-curves (contrast curves).  These LMTs can be combined with one or more colorimetric LMTs to create new looks or
   they can be used as-is with default ACES colorimetry.

The following emulation LMTs are available:

 - [M-ARRI](img/M-ARRI_1.jpg) - emulates the look of the ARRI ALF-2 DRT
 - [M-ARRI_Classic](img/M-ARRI_Classic_1.jpg) - emulates the look of the ARRI K1S1 DRT
 - [M-SONY](img/M-SONY_1.jpg) - emulates the look of the SONY S-Gamut3.Cine DRT
 - [M-RED](img/M-RED_1.jpg) - emulates the look of the RED IPP2 DRT

For all emulation LMTs, equivalent colorimetric LMT exists as well.

See [ACESLooks](ACESLooks/) directory for all LMTs and see [Images](img/) for more example images and comparison images for emulation LMTs.

## Installation

Copy the [ACESLooks](ACESLooks/) directory to your DCC software's LUT/LMT/Look directory.  When upgrading to a new version, remove the old directory and copy it again.

### Installation for Davinci Resolve

Copy the [ACESLooks](ACESLooks/) directory to following location:

 - Mac: /Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT
 - Windows: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT
 - Linux: /home/resolve/LUT

*NOTE: To use the CLFs you must have Davinci Resolve Studio 17.4.2 or later.*

### Installation for OpenColorIO

See [OCIO v2 config](OCIO/) file that defines the LMTs as OCIO Looks.

## Usage

The LMTs are to be applied in ACES2065-1 AP0 linear.

*NOTE: The LUT versions of the LMTs must be applied in ACEScct AP1 space.*

### Usage in Davinci Resolve

In Davinci Resolve LMTs can be used as LUTs and they are available in the same location as LUTs are.  Make sure that in project/clip/node settings the LMT is being applied in ACES AP0 linear,
as they cannot be applied in the ACEScct AP1 timeline space.

![Example Davinci Resolve project settings](/img/resolve_project.png)

### Usage in Foundry Nuke

In Nuke version 13.1 and newer the CLF LMTs can be used with the OCIOFileTransform node or OCIOLookTransform node if the LMTs are defined as looks in the OCIO config file.  The
working space in the OCIOFileTranform node must be changed to ACES2065-1 unless the input is already ACES2065-1, and interpolation must be set to Tetrahedral.

### Gamut Compression and Out of Gamut Colors

Out of gamut colors are pixels with negative color values and they can occur in ACES.  None of the LMTs specifically handle negative values and it is recommended to use the ACES 1.3
Reference Gamut Compression (RGC) operator *before* the LMTs with those images that have out of gamut colors.

Gamut compression can be used also creatively.  Since the colorimetric LMTs retain saturation over the entire luminance range they can retain also super saturated colors.  These colors may
be undesired, too strong or cause clipping with some images.  In these cases gamut compression operator could be used before or after the colorimetric LMTs to achieve the desired look.  This
issue with super saturated colors is generic to ACES 1.3 and not directly related to the LMTs.

### Re-creating emulation LMT with colorimetric LMT

All the current emulation LMTs can be recreated in large part by using Tone-curve LMT and Colorimetric LMT.  For example to re-create the **M-ARRI.clf** one could first apply the
**T-ARRI_Tone.clf** followed by the **C-ARRI.clf**.  This would create exact match for normal surface colors, but because the colorimetric LMT retains saturation while the DRT emulation doesn't,
higher luminance and higher saturation colors would differ.  Gamut compression could then be used to get the match much closer, but probably not exact.  On the other hand, this allows to create,
in this example, ARRI ALF-2 emulation with customizable saturation rolloff.

## Resources

- [ACES Central](https://acescentral.com/)
- [Information about LMTs](https://acescentral.com/knowledge-base-2/lmts/)
