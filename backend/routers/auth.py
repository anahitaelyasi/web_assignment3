from fastapi import APIRouter, Depends, Request
from typing import Any
from schema import *
from database import get_database
from sqlalchemy.orm import Session
from service.userService import *
from utils.protectRoute import get_current_user
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.responses import HTMLResponse




BASE_DIR = Path(__file__).resolve().parent.parent.parent


router1 = APIRouter(prefix="/api/auth", tags=["auth"])
router2 = APIRouter(prefix="/api/admin", tags=["admin"])


templates = Jinja2Templates(directory= BASE_DIR / "frontend/templates")


# ===========================
# Authentication
# ===========================


# Register 

@router1.get("/register", include_in_schema=False)
def show_register_page(request : Request) :
    return templates.TemplateResponse(request, "signUp.html")

@router1.post("/register", status_code=201, response_model=UserOutput)

def register(signup_details: UserCreate, session: Session = Depends(get_database)) :
    try :
        return USerService(session=session).signup(user_details=signup_details)
    except Exception as error :
        print(error)
        raise error
     


# Login 

@router1.get("/login", include_in_schema=False)
def show_login_page(request : Request) :
    return templates.TemplateResponse(request, "login.html")


@router1.post("/login", status_code=200, response_model=UserWithToken)

def login(login_details: UserLogin, session: Session = Depends(get_database)):

    try : 
        return USerService(session=session).login(login_details=login_details)
    except Exception as error:
        print(error) 
        raise error 



# Logout

@router1.get("/logout", include_in_schema=False)
def get_logout_page(request : Request) :
    return templates.TemplateResponse(request, "login.html")

@router1.post("/logout")

def logOut() -> dict[str, Any] :
    return {
        "message" : "Logged out successfully."
    }


# Home

@router1.get("/home")
def get_home_page(request : Request) :
    return templates.TemplateResponse(request, "main.html")


# ===========================
# User account
# ===========================


@router1.get("/me")

def get_profile() -> dict[str, Any] :
    pass

@router1.put("/me")

def change_profile() -> dict[str, Any] :
    pass

@router1.post("/change-password")

def change_password() -> dict[str, Any] :
    pass


# ===========================
# Password reset
# ===========================

@router1.post("/forgot-password")

def forgot_password() -> dict[str, Any] :
    pass

@router1.post("/reset-password")

def reset_password() -> dict[str, Any] :
    pass

# ===========================
# Admin
# ===========================

@router2.get("/users")

def reset_password() -> dict[str, Any] :
    pass


@router2.get("/users/{id}")

def reset_password() -> dict[str, Any] :
    pass


# @router2.put("/users/{id}")

# def reset_password() -> dict[str, Any] :
#     pass


@router2.patch("/users/{id}/toggle-active")

def activate() -> dict[str, Any] :
    pass





