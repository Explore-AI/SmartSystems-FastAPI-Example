"""
Connect to Azure Databricks platform
Use this to return data from databricks file system
"""
import os 
import sys
from pathlib import Path
import json 

from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.dbfs.api import DbfsApi
from databricks_api import DatabricksAPI


from dotenv import load_dotenv
load_dotenv()

def main(): 
    mains_layer_fpath = "dbfs:/mnt/dpsn_dataproducts/SmartSystemsPOC/WD-Mains-Layer.csv"
    mains_layer_dir = "dbfs:/mnt/dpsn_dataproducts/SmartSystemPOC/"
    db_api=DatabricksAPI(host=os.getenv('AZ_DB_HOST'), token=os.getenv('AZ_DB_TOKEN'))
    print(f"Databricks API Type: {type(db_api)}")
    status = db_api.dbfs.get_status(mains_layer_fpath)
    print(status)
    file_info = db_api.dbfs.read(path=mains_layer_fpath)
    print(f"File Info: {file_info}")
    
if __name__ == "__main__":
    print("Connecting to Azure Databricks")
    main()
    
    pass 