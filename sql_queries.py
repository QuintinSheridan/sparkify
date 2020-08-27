# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays(
        songplay_id serial primary key,
        start_time bigint NOT NULL,
        user_id int NOT NULL,
        level text NOT NULL, 
        song_id text, 
        artist_id text,
        session_id int NOT NULL,
        location text NOT NULL,
        user_agent text NOT NULL,
        unique(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    );
""")

user_table_create = ("""
    CREATE TABLE  IF NOT EXISTS users(
        user_id int primary key,
        first_name text NOT NULL, 
        last_name text NOT NULL, 
        gender text NOT NULL, 
        level text NOT NULL
    );
""")

song_table_create = ("""
    CREATE TABLE  IF NOT EXISTS songs(
        song_id text primary key,
        title text NOT NULL, 
        artist_id text NOT NULL,
        year int NOT NULL, 
        duration real NOT NULL,
        unique(song_id, title, artist_id, year, duration)
    );
""")

artist_table_create = ("""
    CREATE TABLE  IF NOT EXISTS artists(
        artist_id text primary key,
        name text NOT NULL, 
        location text NOT NULL, 
        latitude real,
        longitude real,
        unique(artist_id, name, location, latitude, longitude)
    );
""")

time_table_create = ("""
    CREATE TABLE  IF NOT EXISTS time(
    start_time bigint NOT NULL,
    hour int NOT NULL, 
    day int NOT NULL, 
    week int NOT NULL, 
    month int NOT NULL, 
    year int NOT NULL, 
    weekday int NOT NULL
    );
""")

# INSERT RECORDS
# row['ts'], row['userId'], row['level'], song_id, artist_id, row['sessionId'], row['location'], row['userAgent']
songplay_table_insert = ("""
    INSERT INTO 
        songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

# userId	firstName	lastName	gender	level
user_table_insert = ("""
    INSERT INTO users(user_id,first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

song_table_insert = ("""
    INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists(artist_id,name, location, latitude,longitude) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

#timestamp	hour	day	week	month	year	weekday
time_table_insert = ("""
    INSERT INTO time(start_time,hour, day, week,  month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
    SELECT  
        s.song_id,
        a.artist_id
    FROM
        songs as s INNER JOIN 
        artists AS a ON s.artist_id = a.artist_id 
    WHERE
        s.title=%s
    AND
        a.name=%s
    AND
        s.duration=%s 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]