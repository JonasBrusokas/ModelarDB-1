
## 10-13

### Error bound, compression rate experiments

Vanilla Gorilla

- X, 4.500949130291144

Lost gorilla v1 (updated the last value all the time, not quite correct)

- 1, 7.396764809405694
- 2, 11.664826523090339
- 5, 15.24357076882343

Lazy Gorilla with Memory Loss (updates the previous value when it exceeds the bound)

- 1, 7.354105827761319
- 2, 11.606114417020185
- 5, 15.07864120264344

PMC (Poor Man's Compression)

- 1, 3.059281588155926
- 2, 6.712125933487347
- 5, 25.585674145798006

### Results from the output script

```json
{
    "file": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 12764814,
                "('zstd', 2147483647)": 15352585,
                "None": 25597986,
                "gzip": 16262406,
                "lz4": 22316058,
                "snappy": 22430573
            }
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 8348348,
                "('zstd', 2147483647)": 8677408,
                "None": 10828893,
                "gzip": 9226045,
                "lz4": 10089449,
                "snappy": 10269104
            }
        }
    },
    "length": 1561660,
    "model_type_unit": "data_points",
    "size_unit": "bytes",
    "value-E0": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 5960103,
                "('zstd', 2147483647)": 7723185,
                "None": 16365243,
                "gzip": 8414203,
                "lz4": 13271384,
                "snappy": 13317387
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 0.0,
            "Mean_Absolute_Percentage_Error": 0.0,
            "Mean_Absolute_Value": 0.0,
            "Mean_Squared_Error": 0.0,
            "Relative_Average_Error": 0.0,
            "Relative_Error_Uniform_Norm": 0.0
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 1561638,
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 22
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 4701863,
                "('zstd', 2147483647)": 4898295,
                "None": 5569648,
                "gzip": 4995641,
                "lz4": 5378563,
                "snappy": 5439076
            }
        }
    },
    "value-E1": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 5115570,
                "('zstd', 2147483647)": 6786515,
                "None": 15423985,
                "gzip": 7544972,
                "lz4": 12312107,
                "snappy": 12375639
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 2348552.4114837646,
            "Mean_Absolute_Percentage_Error": 0.0057730223052203655,
            "Mean_Absolute_Value": 1.7951828241348267,
            "Mean_Squared_Error": 1742.9295654296875,
            "Relative_Average_Error": 0.7911877999673386,
            "Relative_Error_Uniform_Norm": 1418.4217010648135
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 906078,
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 655582
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 2248454,
                "('zstd', 2147483647)": 2403944,
                "None": 2992914,
                "gzip": 2482688,
                "lz4": 2767762,
                "snappy": 2838394
            }
        }
    },
    "value-E10": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3287770,
                "('zstd', 2147483647)": 4747706,
                "None": 13008693,
                "gzip": 5411484,
                "lz4": 9888859,
                "snappy": 9956514
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 6346142.852874756,
            "Mean_Absolute_Percentage_Error": 0.01530047319829464,
            "Mean_Absolute_Value": 4.741724967956543,
            "Mean_Squared_Error": 3850.495361328125,
            "Relative_Average_Error": 2.0898120864853174,
            "Relative_Error_Uniform_Norm": 1417.8303255718927
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 72779,
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 1488881
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 251653,
                "('zstd', 2147483647)": 295954,
                "None": 532000,
                "gzip": 318294,
                "lz4": 418413,
                "snappy": 434679
            }
        }
    },
    "value-E2": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 4353855,
                "('zstd', 2147483647)": 5977905,
                "None": 14552891,
                "gzip": 6666424,
                "lz4": 11371504,
                "snappy": 11481268
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 3537705.004299164,
            "Mean_Absolute_Percentage_Error": 0.012533001601696014,
            "Mean_Absolute_Value": 2.662438154220581,
            "Mean_Squared_Error": 1981.1832275390625,
            "Relative_Average_Error": 1.1734117255045624,
            "Relative_Error_Uniform_Norm": 1417.8303255718927
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 532150,
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 1029510
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 1062046,
                "('zstd', 2147483647)": 1174380,
                "None": 1619057,
                "gzip": 1220417,
                "lz4": 1422715,
                "snappy": 1469222
            }
        }
    },
    "value-E25": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3259196,
                "('zstd', 2147483647)": 4711215,
                "None": 12979736,
                "gzip": 5371336,
                "lz4": 9850511,
                "snappy": 9919375
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 8637584.809856415,
            "Mean_Absolute_Percentage_Error": 0.01995372772216797,
            "Mean_Absolute_Value": 7.095327854156494,
            "Mean_Squared_Error": 6090.51171875,
            "Relative_Average_Error": 3.1271098664363595,
            "Relative_Error_Uniform_Norm": 2493.300101085392
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 55526,
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 1506134
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 234173,
                "('zstd', 2147483647)": 271919,
                "None": 504853,
                "gzip": 298808,
                "lz4": 394967,
                "snappy": 410640
            }
        }
    },
    "value-E5": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3487015,
                "('zstd', 2147483647)": 4978685,
                "None": 13358114,
                "gzip": 5637878,
                "lz4": 10177474,
                "snappy": 10235804
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 4572389.43063736,
            "Mean_Absolute_Percentage_Error": 0.01408215519040823,
            "Mean_Absolute_Value": 3.4936459064483643,
            "Mean_Squared_Error": 1200.9718017578125,
            "Relative_Average_Error": 1.5397487449140284,
            "Relative_Error_Uniform_Norm": 1417.8303255718927
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 198844,
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 1362816
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 450787,
                "('zstd', 2147483647)": 512686,
                "None": 817284,
                "gzip": 540479,
                "lz4": 673085,
                "snappy": 697703
            }
        }
    },
    "value-E50": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3249365,
                "('zstd', 2147483647)": 4700402,
                "None": 12963961,
                "gzip": 5359907,
                "lz4": 9837359,
                "snappy": 9910771
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 12637342.730060577,
            "Mean_Absolute_Percentage_Error": 0.030333079397678375,
            "Mean_Absolute_Value": 10.814419746398926,
            "Mean_Squared_Error": 6608.32958984375,
            "Relative_Average_Error": 4.76622196590387,
            "Relative_Error_Uniform_Norm": 2034.506948834899
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 40347,
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 1521313
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 223426,
                "('zstd', 2147483647)": 259444,
                "None": 487665,
                "gzip": 285871,
                "lz4": 380215,
                "snappy": 395604
            }
        }
    },
    "value-R": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 5960086,
                "('zstd', 2147483647)": 7723168,
                "None": 16365226,
                "gzip": 8414186,
                "lz4": 13271367,
                "snappy": 13317370
            }
        }
    }
}
```