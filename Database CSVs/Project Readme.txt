README

The database backup is inside of the database CSV files as you can just restore this backup and run it, however, if it is missing data, please restore the data using the commands below. Users are to input 


Command to copy over directors.csv. keep them in chronological order as order matters. 


\copy directors(id, name) FROM '/Users/userName/Desktop/Database CSVs/directors.csv' WITH (FORMAT csv, HEADER true);

Command to copy over shows.csv

finalProject=# \copy shows(show_id, title, description, date_added) FROM '/Users/userName/Downloads/shows_corrected.csv' WITH (FORMAT csv, HEADER true, QUOTE '"');

Command to copy over movies.csv

finalProject=# \copy shows(show_id, title, description, date_added) FROM '/Users/userName/Downloads/movies' WITH (FORMAT csv, HEADER true, QUOTE '"');

Command to copy tv_shows.cdv 

finalProject=# \copy shows(show_id, title, description, date_added) FROM '/Users/jamesbiser/Downloads/tv_shows.csv' WITH (FORMAT csv, HEADER true, QUOTE '"');


Etc. 


