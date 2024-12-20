# Available LMTs for ACES2

## CLF/T-ACES1_SSTS_Tone.clf

```
            Name: ACES2Looks LMT - ACES1 SSTS (HDR) Tone-curve Look
     Description: This LMT emulates the tonal appearance of the ACES 1.3 SSTS tonescale (HDR) when used with ACES 2.0. It does not change colorimetry.
        Revision: 2.0-1
 ACEStransformID: urn:ampas:aces:transformId:v2.0:Look.ACES2Looks.T-ACES1_SSTS_Tone.a2.v1
       Copyright: https://github.com/priikone/aces-looks
           Input: ACES2065-1 AP0 [full dynamic range]
          Matrix: Convert ACES2065-1 (AP0) to ACEScg (AP1)
           Range: Clamp to max 65504
             Log: Convert linear to ACEScct log
           Range: Scale full ACEScct log range to 0-1 range
           LUT1D: Approximate ACES1 SSTS (HDR) Tone curve with full ACEScct output
             Log: Convert ACEScct log to linear
          Matrix: Convert ACEScg (AP1) to ACES2065-1 (AP0)
           Range: Clamp to max 65504
          Output: ACES2065-1 AP0 [full dynamic range]
```

## CLF/T-ACES1_Tone.clf

```
            Name: ACES2Looks LMT - ACES1 Tone-curve Look
     Description: This LMT emulates the tonal appearance of the ACES 1.3 when used with ACES 2.0. It does not change colorimetry.
        Revision: 2.0-1
 ACEStransformID: urn:ampas:aces:transformId:v2.0:Look.ACES2Looks.T-ACES1_Tone.a2.v1
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
            Name: ACES2Looks LMT - ARRI Classic Tone-curve Look
     Description: This LMT emulates the tonal appearance of the ARRI K1S1 DRT when used with ACES 2.0. It does not change colorimetry.
        Revision: 2.0-1
 ACEStransformID: urn:ampas:aces:transformId:v2.0:Look.ACES2Looks.T-ARRI_Classic_Tone.a2.v1
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
            Name: ACES2Looks LMT - ARRI REVEAL Tone-curve Look
     Description: This LMT emulates the tonal appearance of the ARRI REVEAL DRT (2022) when used with ACES 2.0. It does not change colorimetry.
        Revision: 2.0-1
 ACEStransformID: urn:ampas:aces:transformId:v2.0:Look.ACES2Looks.T-ARRI_REVEAL_Tone.a2.v1
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
            Name: ACES2Looks LMT - ARRI Tone-curve Look
     Description: This LMT emulates the tonal appearance of the ARRI ALF-2 DRT when used with ACES 2.0. It does not change colorimetry.
        Revision: 2.0-1
 ACEStransformID: urn:ampas:aces:transformId:v2.0:Look.ACES2Looks.T-ARRI_Tone.a2.v1
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

## CLF/T-RED_Tone.clf

```
            Name: ACES2Looks LMT - RED Tone-curve Look
     Description: This LMT emulates the tonal appearance of the RED IPP2 DRT when used with ACES 2.0. It does not change colorimetry.
        Revision: 2.0-1
 ACEStransformID: urn:ampas:aces:transformId:v2.0:Look.ACES2Looks.T-RED_Tone.a2.v1
       Copyright: https://github.com/priikone/aces-looks
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
            Name: ACES2Looks LMT - SONY Neutral Tone-curve Look
     Description: This LMT emulates a neutral version of the tonal appearance of the SONY S-Gamut3.Cine DRT when used with ACES 2.0. It does not change colorimetry.
        Revision: 2.0-1
 ACEStransformID: urn:ampas:aces:transformId:v2.0:Look.ACES2Looks.T-SONY_Neutral_Tone.a2.v1
       Copyright: https://github.com/priikone/aces-looks
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
            Name: ACES2Looks LMT - SONY Tone-curve Look
     Description: This LMT emulates the tonal appearance of the SONY S-Gamut3.Cine DRT when used with ACES 2.0. It does not change colorimetry.
        Revision: 2.0-1
 ACEStransformID: urn:ampas:aces:transformId:v2.0:Look.ACES2Looks.T-SONY_Tone.a2.v1
       Copyright: https://github.com/priikone/aces-looks
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
