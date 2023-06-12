import asyncio
import json
import uuid
# from api.dependencies import get_hsi_repository
from datetime import datetime, date
from typing import Generator, Optional

from core.utils.event_generator import (status_stream_delay,
                                        status_stream_retry_timeout)
from fastapi import (APIRouter,Depends, HTTPException,
                     Request, status)
from repositories.hsiRepository import HSIRepository
from repositories.session import get_db
from schemas.hsi import HSI, BaseHSI
from sqlalchemy.orm import Session
from sse_starlette.sse import EventSourceResponse
from starlette.responses import StreamingResponse

# our HSI repository dependency


def get_hsi_repository(db: Session = Depends(get_db)):
    return HSIRepository(db)


router = APIRouter()


@router.get("/")
async def root():
    return {"Message": "SCADA HSI Data"}


@router.get("/get-all-data/", response_model=list[BaseHSI])
async def get_all_data(hsi_repository: HSIRepository = Depends(get_hsi_repository), skip: int = 0, limit: int = 100):
    hsi_data = hsi_repository.get_all(skip, limit)
    if hsi_data is None:
        raise HTTPException(status_code=404, detail=f"HSI data not found")
    return [HSI.from_db(hsi) for hsi in hsi_data]


@router.get("/get-id-data/", response_model=BaseHSI)
async def get_hsi_data(id: int, hsi_repository: HSIRepository = Depends(get_hsi_repository)):
    hsi_data = hsi_repository.get_id(id)
    if hsi_data is None:
        raise HTTPException(
            status_code=404, detail=f"HSI data not for id: {id} found")
    return HSI.from_db(hsi_data)


@router.get("/get-data-by-range/", response_model=list[BaseHSI])
async def get_hsi_timerange(start_date: datetime, end_date: datetime, hsi_repository: HSIRepository = Depends(get_hsi_repository)):
    hsi_data = hsi_repository.get_between_timestamps(start_date, end_date)
    if hsi_data is None:
        raise HTTPException(
            status_code=404, detail=f"HSI data not for time range not found")
    return [HSI.from_db(hsi) for hsi in hsi_data]


@router.get("/get-below-limit/", response_model=list[BaseHSI])
async def get_hsi_below_limit(threshold: int = 5.0, hsi_repository: HSIRepository = Depends(get_hsi_repository)):
    hsi_data = hsi_repository.get_below_threshold(threshold)
    if hsi_data is None:
        raise HTTPException(
            status_code=404, detail=f"No data below this limit")
    return [HSI.from_db(hsi) for hsi in hsi_data]


@router.get("/get-above-limit/", response_model=list[BaseHSI])
async def get_hsi_above_limit(threshold: int = 25.0, hsi_repository: HSIRepository = Depends(get_hsi_repository)):
    hsi_data = hsi_repository.get_above_threshold(threshold)
    if hsi_data is None:
        raise HTTPException(
            status_code=404, detail=f"No data above this limit")
    return [HSI.from_db(hsi) for hsi in hsi_data]


@router.get("/get-last-n-hours/", response_model=list[BaseHSI])
async def get_last_n_hours(n: int = 24, hsi_repository: HSIRepository = Depends(get_hsi_repository)):
    hsi_data = hsi_repository.get_last_n_hours(n)
    if hsi_data is None:
        raise HTTPException(
            status_code=404, detail=f"No data for last {n} hours")
    return [HSI.from_db(hsi) for hsi in hsi_data]


@router.get("/get-most-recent-record/", response_model=BaseHSI)
async def get_most_recent(hsi_repository: HSIRepository = Depends(get_hsi_repository)):
    hsi_data = hsi_repository.get_most_recent()
    if hsi_data is None:
        raise HTTPException(status_code=404, detail=f"No data for most recent")
    return HSI.from_db(hsi_data)

# :TODO Configure the Endpoint so that it can perform SSE
"""
Create function to generate events
"""
@router.get("/stream-events-test/")
async def event_handler(request: Request):
    # generate an event for the client
    async def generate_event(request: Request):
        while True:
            event_data = "Event ID:" + str(uuid.uuid4())
            # create the event that is being streamed, from the spark dataframe
            if await request.is_disconnected():
                print("Disconnected")
                break
            yield {"data": event_data}
            # time.sleep(10)
            await asyncio.sleep(20)

    event = generate_event(request)
    return EventSourceResponse(event)


@router.get("/stream-last-event/")
async def stream_most_recent(request: Request, hsiRepository: HSIRepository = Depends(get_hsi_repository)) -> EventSourceResponse:
    async def my_event_generator(request: Request, hsiRepository: HSIRepository) -> Generator:
        # this is to be replaced with Event Grid Subscription
        while True:
            if await request.is_disconnected():
                print("Disconnected")
                break
            data_param = await get_most_recent(hsiRepository)
            # event = "" + str(uuid.uuid4())
            if data_param:
                response = {
                    "event": "stream_event",
                    "id": str(uuid.uuid4()),
                    "retry": status_stream_retry_timeout,
                    "data": {"Id": data_param.Id, "Value": float(data_param.Value), "time": str(data_param.enqueuedTime)}
                }
                yield json.dumps(response)

            await asyncio.sleep(status_stream_delay)
    try:
        # obtain the event notification
        event = my_event_generator(request, hsiRepository)
        response = StreamingResponse(
            content=event, status_code=status.HTTP_200_OK, media_type="application/json")
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}")

@router.get("/get-from-date/")
async def get_from_start_date(start_date: date, hsiRepository: HSIRepository = Depends(get_hsi_repository)):
    """
    Summary: 
        Returns the latest data from a specified start date.
    
    Args:
        start_date (datetime): 
            _description_
        hsiRepository (HSIRepository, optional): 
            _description_. Defaults to Depends(get_hsi_repository).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: list of HSI
    """
    hsi_data = hsiRepository.get_from_start_date(start_date)
    if hsi_data is None:
        raise HTTPException(
            status_code=404, detail=f"No data from this date onwards")
    return [HSI.from_db(hsi) for hsi in hsi_data]

