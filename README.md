# LMTs for ACES

ACESLooks is a set of LMTs for ACES versions 1.1, 1.2 and 1.3.

## LMTs

The following LMTs are available:

 - [ARRI Look](img/ARRI_Look.jpg) - approximates the look of the ARRI ALF-2 DRT
 - [ARRI Classic Look](img/ARRI_Classic_Look.jpg) - approximates the look of the ARRI K1S1 DRT
 - [SONY Look](img/SONY_Look.jpg) - approximates the look of the SONY S-Gamut3.Cine DRT
 - [RED Look](img/RED_Look.jpg) - approximates the look of the RED IPP2 DRT
 - plus more...

See [ACESLooks](ACESLooks/) directory for details.

## Installation

Copy the [ACESLooks](ACESLooks/) directory to your grading suite's LUT/LMT/Look directory.  When upgrading to a new version, remove the old directory and copy it again.

### Installation for Davinci Resolve

Copy the [ACESLooks](ACESLooks/) directory to following location:

 - Mac: /Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT
 - Windows: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT
 - Linux: /home/resolve/LUT

*NOTE: Current versions of Davinci Resolve will not work with the CLF's.  Copy all other directories under ACESLooks except CLF to avoid problems.*

## Usage

The LMTs are to be applied in ACES2065-1 AP0 linear.  LMTs are available as [CLF](http://j.mp/S-2014-006) and as Davinci CTL (DCTL) file formats.

*Do not use the LUTs under the LUT directory directly with images; they are component parts of the LMTs, use the LMTs instead.*

### Usage in Davinci Resolve

In Davinci Resolve LMTs can be used as LUTs and they are available in the same location as LUTs are.  Make sure that in project/node settings the LMT is being applied in ACES AP0 linear,
as they cannot be applied in the ACEScct AP1 timeline space.

![Example Davinci Resolve project settings](/img/resolve_project.png)

## Resources

- [ACES Central](https://acescentral.com/)
- [Information about LMTs](https://acescentral.com/knowledge-base-2/lmts/)
