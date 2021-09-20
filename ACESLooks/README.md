# Available LMTs

## CLF/C-ARRI.clf

```
           Name: ACESLooks LMT - ARRI ALF-2 Colorimetric LMT
    Description: This LMT emulates the colorimetry of the ARRI ALF-2 when used with ACES 1.3. Colorimetric LMT changes scene colorimetry, but doesn't change contrast or exposure. It retains saturation across the entire luminance range.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct range for LUT3D input range
          LUT3D: Emulate ARRI ALF-2 colorimetry
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [22 stops dynamic range]
```

## CLF/C-ARRI_Classic.clf

```
           Name: ACESLooks LMT - ARRI K1S1 Colorimetric LMT
    Description: This LMT emulates the colorimetry of the ARRI K1S1 when used with ACES 1.3. Colorimetric LMT changes scene colorimetry, but doesn't change contrast or exposure. It retains saturation across the entire luminance range.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct range for LUT3D input range
          LUT3D: Emulate ARRI K1S1 colorimetry
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [22 stops dynamic range]
```

## CLF/C-RED.clf

```
           Name: ACESLooks LMT - RED IPP2 Colorimetric LMT
    Description: This LMT emulates the colorimetry of the RED IPP2 when used with ACES 1.3. Colorimetric LMT changes scene colorimetry, but doesn't change contrast or exposure. It retains saturation across the entire luminance range.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct range for LUT3D input range
          LUT3D: Emulate RED IPP2 colorimetry
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [22 stops dynamic range]
```

## CLF/C-SONY.clf

```
           Name: ACESLooks LMT - SONY S-Gamut3.Cine Colorimetric LMT
    Description: This LMT emulates the colorimetry of the SONY S-Gamut3.Cine when used with ACES 1.3. Colorimetric LMT changes scene colorimetry, but doesn't change contrast or exposure. It retains saturation across the entire luminance range.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct range for LUT3D input range
          LUT3D: Emulate SONY S-Gamut3.Cine colorimetry
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [22 stops dynamic range]
```

## CLF/M-ARRI.clf

```
           Name: ACESLooks LMT - ARRI ALF-2 Look
    Description: This LMT emulates the look of the ARRI ALF-2 DRT when used with ACES 1.3 and Rec.709 Output Transform.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Emulate ARRI ALF-2 tone curve with full ACEScct output
          Range: Scale full ACEScct range for LUT3D input range
          LUT3D: Emulate ARRI ALF-2 colorimetry
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [22 stops dynamic range]
```

## CLF/M-ARRI_Classic.clf

```
           Name: ACESLooks LMT - ARRI K1S1 Look
    Description: This LMT emulates the look of the ARRI K1S1 DRT when used with ACES 1.3 and Rec.709 Output Transform.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Emulate ARRI K1S1 tone curve with full ACEScct output
          Range: Scale full ACEScct range for LUT3D input range
          LUT3D: Emulate ARRI K1S1 colorimetry
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [22 stops dynamic range]
```

## CLF/M-RED.clf

```
           Name: ACESLooks LMT - RED IPP2 Look
    Description: This LMT emulates the look of the RED IPP2 DRT when used with ACES 1.3 and Rec.709 Output Transform.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Emulate RED IPP2 tone curve with full ACEScct output
          Range: Scale full ACEScct range for LUT3D input range
          LUT3D: Emulate RED IPP2 colorimetry
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [22 stops dynamic range]
```

## CLF/M-SONY.clf

```
           Name: ACESLooks LMT - SONY S-Gamut3.Cine Look
    Description: This LMT emulates the look of the SONY S-Gamut3.Cine DRT when used with ACES 1.3 and Rec.709 Output Transform.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Emulate SONY S-Gamut3.Cine tone curve with full ACEScct output
          Range: Scale full ACEScct range for LUT3D input range
          LUT3D: Emulate SONY S-Gamut3.Cine colorimetry
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [22 stops dynamic range]
```

## CLF/T-ARRI_Classic_Tone.clf

```
           Name: ACESLooks LMT - ARRI Classic Tone-curve Look
    Description: This LMT emulates the tonal appearance of the ARRI K1S1 DRT when used with ACES 1.3. It does not change colorimetry.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate ARRI K1S1 tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/T-ARRI_Tone.clf

```
           Name: ACESLooks LMT - ARRI Tone-curve Look
    Description: This LMT emulates the tonal appearance of the ARRI ALF-2 DRT when used with ACES 1.3. It does not change colorimetry.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate ARRI ALF-2 tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/T-RED_Tone.clf

```
           Name: ACESLooks LMT - RED Tone-curve Look
    Description: This LMT emulates the tonal appearance of the RED IPP2 DRT when used with ACES 1.3. It does not change colorimetry.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate RED IPP2 tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/T-SONY_Neutral_Tone.clf

```
           Name: ACESLooks LMT - SONY Neutral Tone-curve Look
    Description: This LMT emulates a neutral version of the tonal appearance of the SONY S-Gamut3.Cine DRT when used with ACES 1.3. It does not change colorimetry.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate a neutral version of SONY S-Gamut3.Cine tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/T-SONY_Tone.clf

```
           Name: ACESLooks LMT - SONY Tone-curve Look
    Description: This LMT emulates the tonal appearance of the SONY S-Gamut3.Cine DRT when used with ACES 1.3. It does not change colorimetry.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate SONY S-Gamut3.Cine tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [full dynamic range]
```
