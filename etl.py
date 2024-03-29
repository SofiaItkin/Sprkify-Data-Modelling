
import os
import glob
import psycopg2
import pandas as pd
import json
from sql_queries import *




def process_song_file(cur, filepath):
    
    """The Function is extracting song data and inserting it into tables (songs and artists).
    """
    # open song file
    with open (filepath) as data_file:
         data = json.load(data_file)

    # insert song record
    

    song_data =pd.DataFrame(data ,index=[0])

    song_data = song_data[['song_id', 'title', 'artist_id', 'year', 'duration']]

    song_data=song_data.values.tolist()
    
    cur.execute(song_table_insert, song_data[0])


    # insert artist record
    
    artist_data =pd.DataFrame(data ,index=[0])

    artist_data = artist_data[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']]

    artist_data=artist_data.values.tolist()
    
    cur.execute(artist_table_insert, artist_data[0])


def process_log_file(cur, filepath):
    """The Function is extracting log data,transforming timestamp to time units and inserting it into tables (time,                  songplay, user)
    """
    
    # open log file
    Log_data=pd.read_json(filepath,lines = True) 


    # filter by NextSong action
    df = Log_data[Log_data['page'] == 'NextSong']
    
  
 

    # convert timestamp column to datetime
    df=df.copy()

    df.loc[:,"ts"]=df.ts.apply(lambda x: pd.to_numeric(x))

    df.loc[:,"ts"]=df.ts/1000.00


    df.loc[:,"ts"] = df.ts.apply(lambda x: pd.datetime.fromtimestamp(x).isoformat())
    
    # insert time data records
    df.ts = pd.to_datetime(df.ts)


    df['start_time'] = df['ts'].dt.time

    df['hour'] = df['ts'].dt.hour

    df['day'] = df['ts'].dt.day

    df['week'] = df['ts'].dt.week

    df['month'] = df['ts'].dt.month

    df['year'] = df['ts'].dt.year

    df['weekday'] = df['ts'].dt.weekday








    column_labels = ['start_time','hour','day','week','month','year','weekday']

    time_df = df.loc[:,column_labels]

 

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df =pd.DataFrame(Log_data)


    user_df = user_df[['userId','firstName', 'lastName', 'gender', 'level']]
    

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = ( pd.to_datetime(row.ts, unit='ms'), row.userId, row.level, songid, artistid, row.sessionId,                                   row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    
    """
    The function extracts the files names and sends it to processing functions.
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    
    """
    The function creates connection to postgresql and activate the process_data function.
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()