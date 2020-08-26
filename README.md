# sparkify
Data Engineering project for mocked up music streaming service

# sparkify
## Data Engineering project for mocked up music streaming service

This a Udacity project to create a database schema and an ETL pipline for mocked out data for a music streaming service.  
The data for the project comes from two different sources:
1) data/song contains jason files with song data
2) data/log contains jason files for users listening to songs

The data was put into a Postgre SQL database so that analytical queries could be performed on it.

The database has the following tables:
1) songplays - data for users listening to songs
2) users - data on the user profiles
3) songs - song data
3) artists - artist data
4) time - time data for when songs were listened to

The project uses the following python scripts:
1) sql_queries.py - sql queries to drop tables, create  tables, and insert data
2) create_tables.py - a script to set up the database
3) etl.ipynb - a jupyter notebook used to create the ETL process
4) etl.py - a python script to process all of the json data files and populate the database tables
5) test.ipynb - a script to test the ETL process


The project uses Python 3.6
All of the Python dependencies can be installed by running
```pip install -r requirements.txt```





