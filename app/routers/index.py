from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import select
from app.database import SessionDep
from app.models import *
from app.auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import status

index_router = APIRouter()

@index_router.get("/", response_class=HTMLResponse)
async def index(
    request: Request, 
):
    try:
        logged_in_user = await get_current_user()
        return RedirectResponse("/dashboard")
    except Exception:
        print("User not logged in, carrying them to the login page instead")
        return RedirectResponse("/login")