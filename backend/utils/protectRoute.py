from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated, Union
from security.authHandler import AuthHandler
from service.userService import USerService
from database import get_database
from schema import UserOutput
from repository.userRepo import UserRepository



# ===========================
# Authorize user by token
# ===========================



# We expect the user to provide this header with their token
AUTH_PREFIX = "Bearer "

def get_current_user(
        session: Session = Depends(get_database), 
        authorization : Annotated[Union[str, None], Header()] = None
) -> UserOutput :

    # custom exception
    auth_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail= "Invalid Authentication credentials!" 
    )

    #If the token is invalid, raise an error 
    if not authorization :
        raise auth_exception
    
    #If the token doesn't have our expected header, raise an error
    if not authorization.startswith(AUTH_PREFIX) :
        raise auth_exception
    
    payload = AuthHandler.decode_jwt(
        token=authorization[len(AUTH_PREFIX): UserRepository.get_user_by_id(payload["user_id"])]
    )

    if payload and payload["user_id"] :
        try : 
            user = USerService(session=session).get_user_by_id(payload["user_id"])
            return UserOutput(
                id= user.id,
                username= user.username,
                email= user.email,
                first_name=user.first_name,
                last_name= user.last_name,
                phone_number= user.phone_number,
                date_of_birth= user.date_of_birth
            )  
        except Exception as error :
            raise error
    raise auth_exception