"""
This schema is responsible for sending the data over API
"""
from pydantic import BaseModel
from pydantic.dataclasses import dataclass

class NetworkMeter(BaseModel):
    gisid: int 


@dataclass
class NMDataClass: 
    GISID: int 
    METERTYPE: str 
    METERSTATUS: str 
    DATEPOSTED: str
    DATECREATED: str
    NETWORKCODE1: str 
    NETWORKCODE2: str 
    GENID: str
    FMZ1CODE:str 