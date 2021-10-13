- ``sbt assembly`` - compiles the uber jar
- ``sbt run`` 

## Setup

- Setup Java 11 JDK
- Run ``sbt compile``

## Running 

- Run ``sbt run path/to/modelardb.conf``

# Run

- ``java -cp "/Users/jonasb/repos/ModelarDB-ext/target/scala-2.12/ModelarDB-ext-assembly-0.1.337.jar" ModelarDBRunner-0.3.1.java "/Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/house_1-channel_1.parquet" 0 1 2 5 10 25 50 C LG``
- 
- ``python /Users/jonasb/repos/ModelarDB-ext/scripts/Output-Segments-To-All.py /Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/house_1-channel_1_output_data_points.parquet``

- ``python /Users/jonasb/repos/ModelarDB-ext/scripts/Compute-Data-Metrics.py  /Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/house_1-channel_1_output_data_points.parquet``