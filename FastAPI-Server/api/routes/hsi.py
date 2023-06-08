"""
"""
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from repositories.hsiRepository import HSIRepository
from domain.schemas.hsi import BaseHSI, HSI
from repositories.sqlwh_session import get_db
# from api.dependencies import get_hsi_repository
from datetime import datetime

# our HSI repository dependency 
def get_hsi_repository(db:Session=Depends(get_db)):
    return HSIRepository(db)

router = APIRouter()

# dependency to get 
@router.get("/")
async def root():
    return {"Message": "SCADA HSI Data"}

@router.get("/get-all-data/", response_model=list[BaseHSI])
async def get_all_data(hsi_repository:HSIRepository = Depends(get_hsi_repository), skip:int=0, limit:int=100):
    hsi_data = hsi_repository.get_all(skip, limit)
    if hsi_data is None:
        raise HTTPException(status_code=404, detail=f"HSI data not found")
    return [HSI.from_db(hsi) for hsi in hsi_data]

@router.get("/get-id-data/{id}", response_model=BaseHSI)
async def get_hsi_data(id:int, hsi_repository:HSIRepository = Depends(get_hsi_repository)):
    hsi_data = hsi_repository.get_id(id)
    print(hsi_data)
    print(hsi_data.Id)
    print(hsi_data.Value)
    if hsi_data is None:
        raise HTTPException(status_code=404, detail=f"HSI data not for id: {id} found")
    return HSI.from_db(hsi_data) 

@router.get("/get-data-by-range/", response_model=list[BaseHSI])
async def get_hsi_timerange(start_date:datetime, end_date:datetime, hsi_repository:HSIRepository = Depends(get_hsi_repository)):
    hsi_data = hsi_repository.get_between_timestamps(start_date, end_date)
    if hsi_data is None:
        raise HTTPException(status_code=404, detail=f"HSI data not for time range not found")
    return [HSI.from_db(hsi) for hsi in hsi_data] 

@router.get("/get-below-limit/", response_model=list[BaseHSI])
async def get_hsi_below_limit(threshold:int=5.0, hsi_repository:HSIRepository = Depends(get_hsi_repository)):
    hsi_data = hsi_repository.get_below_threshold(threshold)
    if hsi_data is None:
        raise HTTPException(status_code=404, detail=f"No data below this limit")
    return [HSI.from_db(hsi) for hsi in hsi_data]

@router.get("/get-above-limit/", response_model=list[BaseHSI])
async def get_hsi_above_limit(threshold:int=25.0, hsi_repository:HSIRepository = Depends(get_hsi_repository)):
    hsi_data = hsi_repository.get_above_threshold(threshold)
    if hsi_data is None:
        raise HTTPException(status_code=404, detail=f"No data above this limit")
    return [HSI.from_db(hsi) for hsi in hsi_data]

@router.get("/get-last-n-hours/", response_model=list[BaseHSI])
async def get_last_n_hours(n:int=24, hsi_repository:HSIRepository = Depends(get_hsi_repository)):
    hsi_data = hsi_repository.get_last_n_hours(n)
    if hsi_data is None:
        raise HTTPException(status_code=404, detail=f"No data for last {n} hours")
    return [HSI.from_db(hsi) for hsi in hsi_data]
