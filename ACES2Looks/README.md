# Available LMTs for ACES2

## CLF/T-ACES1_Tone.clf

```
           Name: ACESLooks LMT - ACES1 Tone-curve Look
    Description: This LMT emulates the tonal appearance of the ACES 1.3 when used with ACES 2.0. It does not change colorimetry.
       Revision: 2.0-1
      Copyright: https://github.com/priikone/aces-looks
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate ACES1 tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/T-ARRI_Classic_Tone.clf

```
           Name: ACESLooks LMT - ARRI Classic Tone-curve Look
    Description: This LMT emulates the tonal appearance of the ARRI K1S1 DRT when used with ACES 2.0. It does not change colorimetry.
       Revision: 2.0-1
      Copyright: https://github.com/priikone/aces-looks
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

## CLF/T-ARRI_REVEAL_Tone.clf

```
           Name: ACESLooks LMT - ARRI REVEAL Tone-curve Look
    Description: This LMT emulates the tonal appearance of the ARRI REVEAL DRT (2022) when used with ACES 2.0. It does not change colorimetry.
       Revision: 2.0-1
      Copyright: https://github.com/priikone/aces-looks
          Input: ACES2065-1 AP0 [full dynamic range]
         Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
          Range: Clamp to max 65504
            Log: Convert linear to ACEScct log
          Range: Scale full ACEScct log range to 0-1 range
          LUT1D: Approximate ARRI REVEAL tone curve with full ACEScct output
            Log: Convert ACEScct log to linear
         Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
          Range: Clamp to max 65504
         Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/T-ARRI_Tone.clf

```
           Name: ACESLooks LMT - ARRI Tone-curve Look
    Description: This LMT emulates the tonal appearance of the ARRI ALF-2 DRT when used with ACES 2.0. It does not change colorimetry.
       Revision: 2.0-1
      Copyright: https://github.com/priikone/aces-looks
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
