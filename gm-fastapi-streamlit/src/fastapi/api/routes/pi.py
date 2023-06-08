"""
_summary_

"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"Message": "OSI Pi Data"}