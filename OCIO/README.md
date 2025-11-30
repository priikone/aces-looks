# OCIO v2 Look config

This directory contains OCIO v2 config that contains all the LMTs as Looks.  Copy the contents of the config file to your own OCIO config file,
and copy the ACESLooks directory to your OCIO LUTs directory.  You can use the LMTs with OCIOLookTransform with the config file, or alternatively
you can use OCIOFileTransform directly with the CLF files.

NOTE: The 'process_space' in the config file for these LMTs is "ACES2065-1" defined in the ACES OCIO reference config, available at:
https://github.com/AcademySoftwareFoundation/OpenColorIO-Config-ACES
