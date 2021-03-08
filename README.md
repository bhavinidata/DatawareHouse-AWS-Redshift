# Datawarehouse - AWS Redshift

### Objective
A client Sparkify - a music streaming startup, has grown their user base and song database. They want to move their processes and data onto the cloud. Their data resides in S3 bucket, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. Need to provide solution that enables music stores to easily process lots of information efficiently.

### Project Summary
An implementation of a Data Warehouse leveraging AWS RedShift. This project builds an ETL pipeline for the database hosted on AWS Redshift that extracts their data from multiple JSON files residing in S3 buckets, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

### Databases and Database Schema:
This contains 5 table star schema and two "staging" tables, which serves as an area for processing the data before insertion into the database.

##### staging table: "staging events table"
    * A staging table for temporary holding and/or preprocessing data coming from the 'log_data' S3 bucket. 
        event_id    BIGINT IDENTITY(0,1),
        artist            VARCHAR,
        auth              VARCHAR,
        firstName         VARCHAR,
        gender            VARCHAR,
        itemInSession     INT,
        lastName          VARCHAR,
        length            FLOAT8,
        level             VARCHAR,
        location          VARCHAR,
        method            VARCHAR,
        page              VARCHAR,
        registration      VARCHAR,
        sessionId         INT,
        song              VARCHAR,
        status            INT,
        ts                BIGINT,
        userAgent         VARCHAR,
        userId            INT    

##### staging table: "staging songs table"
    * A staging table for temporary holding and/or preprocessing data coming from the 'song_data' S3 bucket.
        num_songs         INT,
        artist_id         VARCHAR,
        artist_latitude   FLOAT8,
        artist_longitude  FLOAT8,
        artist_location   VARCHAR,
        artist_name       VARCHAR, 
        song_id           VARCHAR,
        title             VARCHAR,
        duration          FLOAT8,
        year              INT

### ETL Pipeline
The data from song_data and log_data JSON files are extracted and put in staging tables. Staging tables are necessary for data warehouses, as they serve as an area to perform checks and data cleaning and transformation before insertion.Later, from the staging tables, data is loaded into song, user, artist, songplays, time tables.

The ETL process execution:

* Before running scripts, make sure the S3 buckets and the reshift cluster are running, and that a connection instance can be established with the cluster.
* The "sql_queries.py" python script contains sql statements needed to create the 7 tables (two staging tables one dimension and 4 fact tables), and to insert the appropriate data from the correct sources.
* The "create_tables.py" python script will run the create table sql queries in the "sql_queries.py" file, and create the empty tables. 
* The "etl.py" script will create a connection instance to the cluster, load the "log_data" and "song_data" json files from S3 bucket to the staging tables, and then insert the data into the 5 tables accordingly.


### AWS Redshift set-up
AWS Redshift is used in ETL pipeline as the DB solution. Below mentioned set-up has been used:

Cluster: 4x dc2.large nodes
Location: US-West-2


### Example queries:
Running the following query in redshift query editor: 

<1.> 
Get the number of songs.

`SELECT Count(*) FROM songplays;
Result: 333`

<2.> 
Get name of artists by running following query.

`select * from artists limit 10;`

Pick one artist. here for ex- 'John Williams'

`select * from artists where artists.name = 'John Williams';`

Get the songs by artists.

`SELECT songs.song_id, artists.name FROM songs JOIN artists ON songs.artist_id = artists.artist_id WHERE artists.name = 'John Williams';`

Get the number of songs by artists.

`SELECT COUNT(songs.song_id) FROM songs JOIN artists ON songs.artist_id = artists.artist_id WHERE artists.name = 'John Williams';`
Result: 3
