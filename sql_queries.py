# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "drop table  IF EXISTS songs;"
artist_table_drop = "drop table  IF EXISTS artists;"
time_table_drop = "drop table IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""Create Table songplays (songplay_id SERIAL PRIMARY KEY, 
                                                    start_time TIMESTAMP NOT NULL, 
                                                    user_id  int NOT NULL, 
                                                    level varchar NOT NULL, 
                                                    song_id varchar, 
                                                    artist_id varchar,
                                                    session_id int NOT NULL,
                                                    location varchar, 
                                                    user_agent varchar);
""")

user_table_create = ("""Create Table users (user_id varchar PRIMARY KEY, 
                                            first_name varchar , 
                                            last_name varchar, 
                                            gender varchar, 
                                            level varchar NOT NULL);
""")

song_table_create = ("""Create Table songs (song_id varchar PRIMARY KEY,
                                            title varchar NOT NULL, 
                                            artist_id varchar NOT NULL, 
                                            year  varchar NOT NULL, 
                                            duration int NOT NULL);
""")

artist_table_create = ("""Create Table artists (artist_id varchar PRIMARY KEY, 
                                                artist_name varchar NOT NULL, 
                                                artist_location varchar NOT NULL, 
                                                artist_latitude varchar, 
                                                artist_longitude varchar);
""")


time_table_create = ("""Create Table time (start_time time  PRIMARY KEY, 
                                           hour int NOT NULL, 
                                           day int NOT NULL, 
                                           week int NOT NULL, 
                                           month int NOT NULL, 
                                           year varchar NOT NULL, 
                                           weekday int NOT NULL);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays
( start_time, 
  user_id,
  level, 
  song_id, 
  artist_id, 
  session_id , 
  location,user_agent) VALUES ( %s, %s,%s,%s,%s,%s,%s,%s);
""")

user_table_insert = ("""INSERT INTO users
(user_id, 
first_name, 
last_name, 
gender, 
level) VALUES (%s, %s, %s,%s,%s)
ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""INSERT INTO songs
(song_id, 
title, 
artist_id, 
year, 
duration) VALUES (%s, %s, %s,%s,%s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists
(artist_id, 
artist_name, 
artist_location, 
artist_latitude, 
artist_longitude) VALUES (%s, %s, %s,%s,%s)
ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time
(start_time,
hour,
day,
week,
month,
year,
weekday) VALUES (%s, %s, %s,%s,%s,%s,%s)
ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""SELECT songs.song_id, songs.artist_id 
FROM songs JOIN artists ON (songs.artist_id = artists.artist_id)
WHERE songs.title = %s 
AND artists.artist_name = %s 
AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]