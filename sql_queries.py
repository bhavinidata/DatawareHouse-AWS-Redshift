import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_events (
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
    );
""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs (
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
    );
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
        songplay_id       INT IDENTITY(0,1) PRIMARY KEY,
        start_time        TIMESTAMP NOT NULL SORTKEY,
        user_id           INT NOT NULL,
        level             VARCHAR NOT NULL DISTKEY,
        song_id           VARCHAR NOT NULL,
        artist_id         VARCHAR NOT NULL,
        session_id        VARCHAR NOT NULL,
        location          VARCHAR,
        user_agent        VARCHAR
    );
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
        user_id          INT SORTKEY PRIMARY KEY,
        first_name       VARCHAR,
        last_name        VARCHAR,
        gender           VARCHAR,
        level            VARCHAR NOT NULL DISTKEY
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id         VARCHAR SORTKEY PRIMARY KEY,
        title           VARCHAR NOT NULL,
        artist_id       VARCHAR NOT NULL DISTKEY,
        year            INT,
        duration        NUMERIC
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id     VARCHAR SORTKEY PRIMARY KEY,
        name          VARCHAR NOT NULL,
        location      VARCHAR,
        latitude      FLOAT8,
        longitude     FLOAT8
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time    TIMESTAMP SORTKEY PRIMARY KEY,
        hour          INT NOT NULL,
        day           INT NOT NULL,
        week          INT NOT NULL,
        month         INT NOT NULL,
        year          INT NOT NULL DISTKEY,
        weekday       INT NOT NULL
    );
""")

