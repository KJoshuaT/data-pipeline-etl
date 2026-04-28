import pandas as pandas
import pyodbc as pyodbc
from sqlalchemy import create_engine

df = pandas.read_csv("data_for_preprocessing.csv")

df = df.drop(columns=["Unnamed: 0"])

df["Text"] = df["Text"].str.strip()

print(df.head())
print(df.columns)


engine = create_engine(
    "mssql+pyodbc://JDTOP\\MSSQLSERVER01/DataPipelineDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

df.to_sql(
    "ai_vs_human",
    engine,
    if_exists="append",
    index=False
)

print("Data inserted")