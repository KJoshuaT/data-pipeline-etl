# Data Pipeline ETL using python/sql

Simple ETL pipeline that extracts data from a CSV file into a SQL Server.

##Pipeline Steps

###Extract
- Reads data from a CSV file using pandas

###Transform
- Removes unnecessary columns
- Cleans text fields
- Prepares data for database insertion

##Loads
- Inserts data into SQL Server using SQLAlchemy

  ## Tech Stack
  - Python
  - pandas
  - SQLAlchemy
  - SQL Server

 ## How to Run

1. Install dependencies, run: pip install -r requirements.txt
2. Update database connection string in pipeline.py
3. Run script: python pipeline.py
