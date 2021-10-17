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

- ``java -cp "/Users/jonasb/repos/ModelarDB-ext/target/scala-2.12/ModelarDB-ext-assembly-0.1.337.jar" ModelarDBRunner-0.3.1.java "/Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/house_1-channel_1.parquet" 0 1 2 5 10 25 50 C LG``
- ``python /Users/jonasb/repos/ModelarDB-ext/scripts/Compute-Data-Metrics.py  /Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/house_1-channel_1_output_data_points.parquet``

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

- Second set of exps
- ``java -cp "/Users/jonasb/repos/ModelarDB-ext/target/scala-2.12/ModelarDB-ext-assembly-0.1.337.jar" /Users/jonasb/repos/ModelarDB-ext/scripts/ModelarDBRunner-for-ext.java "/Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/house_1-channel_1.parquet" 0 1 2 5 10 25 50 LG``
- ``python /Users/jonasb/repos/ModelarDB-ext/scripts/Compute-Data-Metrics.py  /Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/house_1-channel_1_output_data_points.parquet``

```
{
    "file": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 13969958,
                "('zstd', 2147483647)": 16665184,
                "None": 27270254,
                "gzip": 17709400,
                "lz4": 24004727,
                "snappy": 24143082
            }
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 8560007,
                "('zstd', 2147483647)": 8828910,
                "None": 12989661,
                "gzip": 10225973,
                "lz4": 11166762,
                "snappy": 11284428
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
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 4702120,
                "('zstd', 2147483647)": 4898244,
                "None": 5569599,
                "gzip": 4995618,
                "lz4": 5378528,
                "snappy": 5439140
            }
        }
    },
    "value-E1": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 5403711,
                "('zstd', 2147483647)": 7125729,
                "None": 15922430,
                "gzip": 7911107,
                "lz4": 12793409,
                "snappy": 12873535
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 2411883.2238197327,
            "Mean_Absolute_Percentage_Error": 0.006176621187478304,
            "Mean_Absolute_Value": 1.8839547634124756,
            "Mean_Squared_Error": 652.628173828125,
            "Relative_Average_Error": 0.8303123772373399,
            "Relative_Error_Uniform_Norm": 994.2393394824873
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 2564921,
                "('zstd', 2147483647)": 2751728,
                "None": 3424433,
                "gzip": 2827096,
                "lz4": 3160564,
                "snappy": 3239217
            }
        }
    },
    "value-E10": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3389452,
                "('zstd', 2147483647)": 4855275,
                "None": 13156108,
                "gzip": 5518899,
                "lz4": 10027917,
                "snappy": 10107655
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 4710667.792362213,
            "Mean_Absolute_Percentage_Error": 0.014376001432538033,
            "Mean_Absolute_Value": 3.946420907974243,
            "Mean_Squared_Error": 4174.22216796875,
            "Relative_Average_Error": 1.7392996075244602,
            "Relative_Error_Uniform_Norm": 1447.7515314900022
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 543547,
                "('zstd', 2147483647)": 705075,
                "None": 1269894,
                "gzip": 720317,
                "lz4": 955238,
                "snappy": 1024451
            }
        }
    },
    "value-E2": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 4774384,
                "('zstd', 2147483647)": 6412274,
                "None": 15047191,
                "gzip": 7181783,
                "lz4": 11897517,
                "snappy": 11981007
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 3318013.576766968,
            "Mean_Absolute_Percentage_Error": 0.013509661890566349,
            "Mean_Absolute_Value": 2.604416608810425,
            "Mean_Squared_Error": 1013.2361450195312,
            "Relative_Average_Error": 1.147839927861194,
            "Relative_Error_Uniform_Norm": 1432.3945575035277
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 1345201,
                "('zstd', 2147483647)": 1517240,
                "None": 2131749,
                "gzip": 1556104,
                "lz4": 1838482,
                "snappy": 1906774
            }
        }
    },
    "value-E25": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3325058,
                "('zstd', 2147483647)": 4784381,
                "None": 13075466,
                "gzip": 5441937,
                "lz4": 9939955,
                "snappy": 10008113
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 6578106.682411194,
            "Mean_Absolute_Percentage_Error": 0.017453812062740326,
            "Mean_Absolute_Value": 5.8981146812438965,
            "Mean_Squared_Error": 6970.748046875,
            "Relative_Average_Error": 2.599465785852835,
            "Relative_Error_Uniform_Norm": 1521.9420932773735
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 505090,
                "('zstd', 2147483647)": 669508,
                "None": 1227415,
                "gzip": 683071,
                "lz4": 913354,
                "snappy": 985024
            }
        }
    },
    "value-E5": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3752307,
                "('zstd', 2147483647)": 5264513,
                "None": 13696912,
                "gzip": 5955480,
                "lz4": 10540970,
                "snappy": 10615236
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 3897603.4071998596,
            "Mean_Absolute_Percentage_Error": 0.014642923139035702,
            "Mean_Absolute_Value": 3.0835933685302734,
            "Mean_Squared_Error": 2333.327880859375,
            "Relative_Average_Error": 1.3590265759868647,
            "Relative_Error_Uniform_Norm": 1447.7515314900022
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 763166,
                "('zstd', 2147483647)": 929860,
                "None": 1506682,
                "gzip": 950643,
                "lz4": 1199604,
                "snappy": 1267619
            }
        }
    },
    "value-E50": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3313003,
                "('zstd', 2147483647)": 4772855,
                "None": 13061541,
                "gzip": 5429789,
                "lz4": 9926715,
                "snappy": 10006334
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 8186251.95154953,
            "Mean_Absolute_Percentage_Error": 0.027638040482997894,
            "Mean_Absolute_Value": 8.463390350341797,
            "Mean_Squared_Error": 8954.3759765625,
            "Relative_Average_Error": 3.7300539499992063,
            "Relative_Error_Uniform_Norm": 2679.1822961858375
        },
        "model_types": {
            "dk.aau.modelardb.core.models.LostFacebookGorillaModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 498465,
                "('zstd', 2147483647)": 662929,
                "None": 1221367,
                "gzip": 675941,
                "lz4": 905463,
                "snappy": 977801
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

- Output for PMC
```json
{
    "file": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 11175427,
                "('zstd', 2147483647)": 13471995,
                "None": 23626436,
                "gzip": 14435421,
                "lz4": 20273928,
                "snappy": 20335070
            }
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 12975577,
                "('zstd', 2147483647)": 16402228,
                "None": 40781391,
                "gzip": 18873887,
                "lz4": 31056143,
                "snappy": 31426796
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
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 9286120,
                "('zstd', 2147483647)": 12254778,
                "None": 29334152,
                "gzip": 13610986,
                "lz4": 22867154,
                "snappy": 22996788
            }
        }
    },
    "value-E1": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 4307771,
                "('zstd', 2147483647)": 5839809,
                "None": 14541430,
                "gzip": 6643339,
                "lz4": 11341476,
                "snappy": 11390125
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 959411.655292511,
            "Mean_Absolute_Percentage_Error": 0.00317392498254776,
            "Mean_Absolute_Value": 0.6317207217216492,
            "Mean_Squared_Error": 2.1634461879730225,
            "Relative_Average_Error": 0.2784171638580765,
            "Relative_Error_Uniform_Norm": 1.0
        },
        "model_types": {
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 2744939,
                "('zstd', 2147483647)": 3123083,
                "None": 6458320,
                "gzip": 3467609,
                "lz4": 5043189,
                "snappy": 5150077
            }
        }
    },
    "value-E10": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3266207,
                "('zstd', 2147483647)": 4718112,
                "None": 12988536,
                "gzip": 5377733,
                "lz4": 9858572,
                "snappy": 9927977
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 3627778.4325408936,
            "Mean_Absolute_Percentage_Error": 0.012775897048413754,
            "Mean_Absolute_Value": 2.3831284046173096,
            "Mean_Squared_Error": 49.393184661865234,
            "Relative_Average_Error": 1.0503118463554766,
            "Relative_Error_Uniform_Norm": 9.999984074870238
        },
        "model_types": {
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 256540,
                "('zstd', 2147483647)": 304094,
                "None": 572938,
                "gzip": 331827,
                "lz4": 446256,
                "snappy": 464085
            }
        }
    },
    "value-E2": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3707662,
                "('zstd', 2147483647)": 5211759,
                "None": 13718580,
                "gzip": 5906871,
                "lz4": 10510092,
                "snappy": 10559255
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 1590871.4960632324,
            "Mean_Absolute_Percentage_Error": 0.005493777338415384,
            "Mean_Absolute_Value": 1.0609829425811768,
            "Mean_Squared_Error": 5.689898490905762,
            "Relative_Average_Error": 0.4676050689785556,
            "Relative_Error_Uniform_Norm": 2.0
        },
        "model_types": {
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 1490892,
                "('zstd', 2147483647)": 1783152,
                "None": 3382573,
                "gzip": 1928034,
                "lz4": 2685390,
                "snappy": 2751934
            }
        }
    },
    "value-E25": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3249266,
                "('zstd', 2147483647)": 4703197,
                "None": 12969583,
                "gzip": 5363510,
                "lz4": 9841106,
                "snappy": 9915035
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 5127678.800205231,
            "Mean_Absolute_Percentage_Error": 0.01608528196811676,
            "Mean_Absolute_Value": 3.309873580932617,
            "Mean_Squared_Error": 156.8911590576172,
            "Relative_Average_Error": 1.4587553839952379,
            "Relative_Error_Uniform_Norm": 24.99961595126517
        },
        "model_types": {
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 230787,
                "('zstd', 2147483647)": 272766,
                "None": 516171,
                "gzip": 298359,
                "lz4": 400993,
                "snappy": 417489
            }
        }
    },
    "value-E5": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3386057,
                "('zstd', 2147483647)": 4851850,
                "None": 13136939,
                "gzip": 5516318,
                "lz4": 10010799,
                "snappy": 10085698
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 2775371.805770874,
            "Mean_Absolute_Percentage_Error": 0.010065917856991291,
            "Mean_Absolute_Value": 1.8454371690750122,
            "Mean_Squared_Error": 18.852832794189453,
            "Relative_Average_Error": 0.8133360944659598,
            "Relative_Error_Uniform_Norm": 4.999996242911313
        },
        "model_types": {
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 421816,
                "('zstd', 2147483647)": 531034,
                "None": 989105,
                "gzip": 570593,
                "lz4": 770789,
                "snappy": 802225
            }
        }
    },
    "value-E50": {
        "data_points": {
            "parquet": {
                "('brotli', 2147483647)": 3246421,
                "('zstd', 2147483647)": 4697111,
                "None": 12960762,
                "gzip": 5357245,
                "lz4": 9833639,
                "snappy": 9905778
            }
        },
        "metrics": {
            "Fast_Dynamic_Time_Warping": 10760865.25283432,
            "Mean_Absolute_Percentage_Error": 0.02433118224143982,
            "Mean_Absolute_Value": 7.091466903686523,
            "Mean_Squared_Error": 1971.804443359375,
            "Relative_Average_Error": 3.1254096869607735,
            "Relative_Error_Uniform_Norm": 49.9987170125142
        },
        "model_types": {
            "dk.aau.modelardb.core.models.PMC_MeanModelType": 1561660
        },
        "segments": {
            "parquet": {
                "('brotli', 2147483647)": 220029,
                "('zstd', 2147483647)": 259328,
                "None": 491736,
                "gzip": 284422,
                "lz4": 381975,
                "snappy": 397670
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