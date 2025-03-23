from fastapi import APIRouter, HTTPException, Path, Request
from typing import List
from datetime import datetime as dt

router = APIRouter()


@router.post("/", status_code=201)
async def create_item():
    return "ok"


@router.get("/{id}/")
async def read_item(id: int = Path(..., gt=0), ):
    return "ok"


@router.get("/")
async def read_all_item(request: Request):
    return "ok"


@router.put("/{id}/")
async def update_item(id: int = Path(..., gt=0)):  # Ensures the input is greater than 0
    return "ok"


# DELETE route
@router.delete("/{id}/")
async def delete_item(id: int = Path(..., gt=0)):
    return "ok"

