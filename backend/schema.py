from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# specify the type of data we're looking to accept
from pydantic import BaseModel, constr, EmailStr, field_validator
from datetime import datetime, timedelta, date
from typing import Optional
from jose import JWSError, jwt
from passlib.context import CryptContext
from database import get_database





# ===========================
# User
# ===========================

class UserBase(BaseModel) :
    username : str
    email : EmailStr 
    first_name : str
    last_name : str
    bio :  str | None = None
    phone_number : str
    date_of_birth : date

    @field_validator("phone_number")
    @classmethod
    def phone_num_pattern(cls, phone: str) :
        if not phone.startswith("09") or not phone.isdigit() or len(phone) != 11 :
            raise ValueError("Phone number is invalid!")
        
        return phone

    @field_validator("bio")
    @classmethod
    def check_bio_length(cls, bio: str) :
        if len(bio) > 500 :
            raise ValueError("Bio should have 500 or less characters!")
        return bio

class UserOutput(BaseModel) :
    id : int
    username : str
    email : EmailStr 
    first_name : str
    last_name : str
    bio :  str
    phone_number : str
    date_of_birth : date


class UserCreate(UserBase) :
    password: str

    @field_validator("password")
    @classmethod
    def check_password(cls, pwd: str) :
        if len(pwd) < 8 :
            raise ValueError("Password should have at least 8 characters!")
        if pwd.isdigit() :
            raise ValueError("Password cannot be only numbers!")
    
        if not any(char.isdigit() for char in pwd):
                raise ValueError("Password must contain at least one number!")
        return pwd


class UserLogin(BaseModel) :
    username: str
    password: str

class UserUpdate(BaseModel) :
    id: int
    username : str | None = None
    email : EmailStr | None = None
    first_name : str | None = None
    last_name : str | None = None
    bio :  str | None = None
    phone_number : str | None = None
    date_of_birth : date | None = None
    password: str | None = None

    



# ===========================
# Password
# ===========================

#Request reset code
class PasswordResetRequest(BaseModel):
    email: EmailStr


# Step 2: Verify the code
class PasswordResetVerify(BaseModel):
    email: EmailStr
    code: constr(min_length=6, max_length=6)


# Step 3: Confirm password change
class PasswordResetConfirm(BaseModel):
    email: EmailStr
    code: constr(min_length=6, max_length=6)
    new_password: constr(min_length=6)



# ===========================
# Token
# ===========================

# defining the type of data we're tyring to accept in our request body
# pydantic : will automatically do the validatin for us
class Token(BaseModel) :
    access_token : str
    token_type: str 

# the data that's going to be encoded by our token
class TokenData(BaseModel) :
    username : str | None = None

# send token to user
class UserWithToken(BaseModel) :
    token : str

