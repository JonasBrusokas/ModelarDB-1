## 10-18

- ``sbt assembly``
- ``java -cp "/Users/jonasb/repos/ModelarDB-ext/target/scala-2.12/ModelarDB-ext-assembly-0.1.337.jar" /Users/jonasb/repos/ModelarDB-ext/scripts/ModelarDBRunner-for-ext.java "/Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/lg_v3_d10/house_1-channel_1.parquet" 0 1 2 5 10 25 50 LG10``
- ``python /Users/jonasb/repos/ModelarDB-ext/scripts/Compute-Data-Metrics.py  /Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/lg_v3_d10/house_1-channel_1_output_segments_metadata.txt > lost_gorilla_v2_d10.json``

## 10-19

- When doing: ``java -cp "/Users/jonasb/repos/ModelarDB-ext/target/scala-2.12/ModelarDB-ext-assembly-0.1.337.jar" /Users/jonasb/repos/ModelarDB-ext/scripts/ModelarDBRunner-for-ext.java "/Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/swing/house_1-channel_1.parquet" 0 1 2 5 10 25 50 L``
- Output (used lossless model as fallback)
```
INFO: processed column 2(2011-04-18 13:22:09.0 to 2011-05-24 19:57:02.0) of 2 using error bound 0
WARNING: lossless fallback model was used for 0.6641651% (10372/1561660) of the data points
INFO: processed column 2(2011-04-18 13:22:09.0 to 2011-05-24 19:57:02.0) of 2 using error bound 1
WARNING: lossless fallback model was used for 0.15150546% (2366/1561660) of the data points
INFO: processed column 2(2011-04-18 13:22:09.0 to 2011-05-24 19:57:02.0) of 2 using error bound 2
WARNING: lossless fallback model was used for 0.109755% (1714/1561660) of the data points
INFO: processed column 2(2011-04-18 13:22:09.0 to 2011-05-24 19:57:02.0) of 2 using error bound 50
WARNING: lossless fallback model was used for 0.0939385% (1467/1561660) of the data points
INFO: processed column 2(2011-04-18 13:22:09.0 to 2011-05-24 19:57:02.0) of 2 using error bound 5
WARNING: lossless fallback model was used for 0.09553936% (1492/1561660) of the data points
INFO: processed column 2(2011-04-18 13:22:09.0 to 2011-05-24 19:57:02.0) of 2 using error bound 25
WARNING: lossless fallback model was used for 0.094194636% (1471/1561660) of the data points
INFO: processed column 2(2011-04-18 13:22:09.0 to 2011-05-24 19:57:02.0) of 2 using error bound 10
WARNING: lossless fallback model was used for 0.09445078% (1475/1561660) of the data points
```