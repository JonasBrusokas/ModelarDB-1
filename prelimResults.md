## 10-18

- ``sbt assembly``
- ``java -cp "/Users/jonasb/repos/ModelarDB-ext/target/scala-2.12/ModelarDB-ext-assembly-0.1.337.jar" /Users/jonasb/repos/ModelarDB-ext/scripts/ModelarDBRunner-for-ext.java "/Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/lg_v3_d10/house_1-channel_1.parquet" 0 1 2 5 10 25 50 LG10``
- ``python /Users/jonasb/repos/ModelarDB-ext/scripts/Compute-Data-Metrics.py  /Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/lg_v3_d10/house_1-channel_1_output_segments_metadata.txt > lost_gorilla_v2_d10.json``