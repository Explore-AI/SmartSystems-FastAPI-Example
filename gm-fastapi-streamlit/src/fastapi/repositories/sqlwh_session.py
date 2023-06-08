# Inits a session for SQL warehouse in Databricks 
from databricks import sql 
from databricks.sql.client import Connection
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from dotenv import load_dotenv
load_dotenv()


def init_sql_connection(sqlURI: dict):
    """_summary_
    create a connection to the desired sql warehouse
    
    Args:
        sqlURI (_type_): _description_

    Returns:
        _type_: _description_
    """
    try: 
        sql_connection = sql.connect(sqlURI['server_hostname'], access_token=sqlURI['token'], http_path=sqlURI['http_path'])
        return sql_connection
    except Exception as e:
        print(f"Error connecting to SQL Database: {e}")
        

def init_sqlwh_engine(host, token, http_path, port, database):
    sql_alchemy_url= f"databricks://token:{token}@{host}:{port}/{database}?http_path={http_path}"
    engine = create_engine(sql_alchemy_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    

def main(): 
    print("Connecting to SQL Warehouse")
    sqlURI = {
        "hostname": os.environ.get("DB_SQLWH_HOST"), 
        "token": os.environ.get("DB_SQLWH_TOKEN"), 
        "http_path": os.environ.get("DB_SQLWH_HTTP_PATH"),
        "port": 443,
    }