"""
_summary_

"""
import asyncio
import json
import uuid
# from api.dependencies import get_hsi_repository
from datetime import datetime, date
from typing import Generator

from core.utils.event_generator import (status_stream_delay,
                                        status_stream_retry_timeout)
from fastapi import APIRouter, Depends, HTTPException, Request, status
from repositories.piRepository import PiRepository
from repositories.session import get_db
from schemas.pi import BasePi, Pi
from sqlalchemy.orm import Session


def get_pi_repository(db: Session = Depends(get_db)):
    return PiRepository(db)


router = APIRouter()


@router.get("/")
async def root():
    return {"Message": "OSI Pi Data"}


@router.get("/get-tag-name/")
async def get_tag_name(tag_name: str, pi_repository: PiRepository = Depends(get_pi_repository)) -> BasePi:
    pi_data = pi_repository.get_tag_name(tag_name)
    if pi_data is []:
        raise HTTPException(status_code=404, detail="Tag Name Not Found")
    return Pi.from_db(pi_data)


@router.get("/get-all-for-tag/")
async def get_all_for_tag(tag_name: str, pi_repository: PiRepository = Depends(get_pi_repository)):
    pi_data = pi_repository.get_all_data_for_tag(tag_name)
    if pi_data is []:
        raise HTTPException(status_code=404, detail="Tag Name Not Found")

    return [Pi.from_db(pi) for pi in pi_data]


@router.get("/get-data-by-range/")
async def get_data_by_range(start_date: str, end_date: str, pi_repository: PiRepository = Depends(get_pi_repository)):
    pi_data = pi_repository.get_data_between_timerange(
                    datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S'), 
                    datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S'))
    if pi_data is []:
        raise HTTPException(status_code=404, detail="No data in time range")
    return [Pi.from_db(pi) for pi in pi_data]


@router.get("/last-n-hours/")
async def get_last_n_hours(hours: int, pi_repository: PiRepository = Depends(get_pi_repository)):
    pi_data = pi_repository.get_last_n_hours(hours)
    if pi_data is []:
        raise HTTPException(status_code=404, detail="No Data found")
    return [Pi.from_db(pi) for pi in pi_data]


@router.get("/get-all/")
async def get_all(pi_repository: PiRepository = Depends(get_pi_repository), skip: int = 0, limit: int = 100):
    pi_data = pi_repository.get_all(skip, limit)
    if pi_data is []:
        raise HTTPException(status_code=404, detail="No Data found")
    return [Pi.from_db(pi) for pi in pi_data]


@router.get("/get-from-date/")
async def get_from_start_date(start_date: date, pi_repository: PiRepository = Depends(get_pi_repository)):
    """
    Summary: 
        Returns the latest data from a specified start date.

    Args:
        start_date (datetime): 
            _description_
        pi_repostiory: (PiRepository), optional): 
            _description_. Defaults to Depends(get_pi_repository).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: pi data
    """
    pi_data = pi_repository.get_from_start_date(start_date)
    if pi_data is []:
        raise HTTPException(
            status_code=404, detail=f"No data from this date onwards")
    return [Pi.from_db(pi) for pi in pi_data]
