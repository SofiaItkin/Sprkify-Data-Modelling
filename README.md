## ETL Pipline For Music Data Analyze.


 
The project is about developing an ETL Pipline for a music startup company named Sparkify that wants to analyze their data. 
Sparkify's product is a music app that stores its activity and song data in JSON log Files.
The ETL pipeline was designed to extract  data from JSON files and  develop a star-schema data base.


Star Schema - 
The star schema contains fact tables and dimension tables that used to  aggregate calculations and filter data. 


Fact Table - 
The table contains the records from the log data, every row discribes a songs usage: 
 songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Dimension Tables - 
The Diminsion tables are responsible for the storage of all the properties of the model.

Time - contains the time in diffrent units- start_time, hour, day, week, month, year, weekday.

songs- all the songs in the music app - song_id, title, artist_id, year, duration.

users - the users that use the app - ser_id, first_name, last_name, gender, level.

artists - The artists that published the song - artist_id, name, location, lattitude, longitude



The Project Includes 3 scripts: 

1.Create_tables.py - create a database and creates tables
2.Sql_Queries.py - contains all the sql queries that the etl script uses. 
3.etl.py - script that extracts data from the log files and song directories,transforms the data and inserts it into star-schema.

To run the ETl Pipeline simply first  run the 'create_tables.py' script and afterwards run 'etl.py' script.




