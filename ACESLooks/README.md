# Available LMTs

## CLF/C-ARRI.clf

```
           Name: ACESLooks LMT - ARRI Look
    Description: This LMT approximates the look of the ARRI ALF-2 DRT when used with ACES 1.3. It is a very simple LMT and uses only a tone-curve and a 3x3 matrix to achieve the look.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
          Range: Clamp to 0-65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate ARRI ALF-2 tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
         Matrix: Approximate ARRI ALF-2 colorimetry
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to 0-65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/C-ARRI_Classic.clf

```
           Name: ACESLooks LMT - ARRI Classic Look
    Description: This LMT approximates the look of the ARRI K1S1 DRT when used with ACES 1.3. It is a very simple LMT and uses only a tone-curve and a 3x3 matrix to achieve the look.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
          Range: Clamp to 0-65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate ARRI K1S1 tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
         Matrix: Approximate ARRI K1S1 colorimetry
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to 0-65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/C-RED.clf

```
           Name: ACESLooks LMT - RED Look
    Description: This LMT approximates the look of the RED IPP2 DRT when used with ACES 1.3. It is a very simple LMT and uses only a tone-curve and a 3x3 matrix to achieve the look.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
          Range: Clamp to 0-65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate RED IPP2 tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
         Matrix: Approximate RED IPP2 colorimetry
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to 0-65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/C-SONY.clf

```
           Name: ACESLooks LMT - SONY Look
    Description: This LMT approximates the look of the SONY S-Gamut3.Cine DRT when used with ACES 1.3. It is a very simple LMT and uses only a tone-curve and a 3x3 matrix to achieve the look.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
          Range: Clamp to 0-65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate SONY S-Gamut3.Cine tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
         Matrix: Approximate SONY S-Gamut3.Cine colorimetry
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to 0-65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/C-SONY_Neutral.clf

```
           Name: ACESLooks LMT - SONY Look
    Description: This LMT approximates a neutral look of the SONY S-Gamut3.Cine DRT when used with ACES 1.3. It is a very simple LMT and uses only a tone-curve and a 3x3 matrix to achieve the look.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
          Range: Clamp to 0-65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate a neutral version of SONY S-Gamut3.Cine tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
         Matrix: Approximate SONY S-Gamut3.Cine colorimetry
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to 0-65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/T-ARRI_Classic_Tone.clf

```
           Name: ACESLooks LMT - ARRI Classic Tone-curve Look
    Description: This LMT emulates the tonal appearance of the ARRI K1S1 DRT when used with ACES 1.3. It does not change colorimetry.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
          Range: Clamp to 0-65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate ARRI K1S1 tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
          Range: Clamp to 0-65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/T-ARRI_Tone.clf

```
           Name: ACESLooks LMT - ARRI Tone-curve Look
    Description: This LMT emulates the tonal appearance of the ARRI ALF-2 DRT when used with ACES 1.3. It does not change colorimetry.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
          Range: Clamp to 0-65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate ARRI ALF-2 tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
          Range: Clamp to 0-65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/T-RED_Tone.clf

```
           Name: ACESLooks LMT - RED Tone-curve Look
    Description: This LMT emulates the tonal appearance of the RED IPP2 DRT when used with ACES 1.3. It does not change colorimetry.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
          Range: Clamp to 0-65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate RED IPP2 tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
          Range: Clamp to 0-65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/T-SONY_Neutral_Tone.clf

```
           Name: ACESLooks LMT - SONY Neutral Tone-curve Look
    Description: This LMT emulates a neutral version of the tonal appearance of the SONY S-Gamut3.Cine DRT when used with ACES 1.3. It does not change colorimetry.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
          Range: Clamp to 0-65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate a neutral version of SONY S-Gamut3.Cine tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
          Range: Clamp to 0-65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/T-SONY_Tone.clf

```
           Name: ACESLooks LMT - SONY Tone-curve Look
    Description: This LMT emulates the tonal appearance of the SONY S-Gamut3.Cine DRT when used with ACES 1.3. It does not change colorimetry.
       Revision: 1.3-1
          Input: ACES2065-1 AP0 [full dynamic range]
          Range: Clamp to 0-65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate SONY S-Gamut3.Cine tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
          Range: Clamp to 0-65504
         Output: ACES2065-1 AP0 [full dynamic range]
```
