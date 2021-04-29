## ETL Pipline For Music Data Analyze.


 
The project is about developing an ETL Pipline for data analysis. 
It's aimed for a music app that stores its activity and song data in JSON log Files.
The ETL pipeline was designed to extract  data from JSON files and  develop a star-schema data base.


Star Schema - 
The star schema contains the fact table and the dimension tables that are used to  aggregate calculations and filter data. 


Fact Table - 
contains the records from the log data, every row discribes a songs usage: 
 songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Dimension Tables - 
responsible for the storage of all the properties of the model.

Time - contains the time in diffrent units- start_time, hour, day, week, month, year, weekday.

Songs- all the songs in the music app - song_id, title, artist_id, year, duration.

Users - the users that use the app - ser_id, first_name, last_name, gender, level.

Artists - The artists that published the song - artist_id, name, location, lattitude, longitude



The Project Includes 3 scripts: 

1.Create_tables.py - creates a database and creates tables

2.Sql_Queries.py - contains all the sql queries that the etl script uses. 

3.etl.py - script that extracts data from the log files and song directories, transforms the data and inserts it into a star-schema.

To run the ETl Pipeline simply first  run the 'create_tables.py' script and afterwards run 'etl.py' script.




