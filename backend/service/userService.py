from repository.userRepo import UserRepository
from schema import *
from security.hashHelper import HashHelper
from security.authHandler import AuthHandler
from sqlalchemy.orm import Session
from fastapi import HTTPException


class USerService :
    def __init__(self, session : Session):
        self.__userRepository = UserRepository(session=session)
    
    def signup(self, user_details : UserCreate) -> UserOutput :
        if self.__userRepository.user_exist_by_username(username=user_details.username) :
            raise HTTPException(status_code=400, detail="An account with this username already exists! Please login.") 
        
        hashed_password = HashHelper.turn_pwd_into_hash(plain_password=user_details.password) 
        user_details.password = hashed_password

        return self.__userRepository.create_user(user_data=user_details)
    

    def login(self, login_details: UserLogin) -> UserWithToken:
        if not self.__userRepository.user_exist_by_username(username=login_details.username) :
            raise HTTPException(status_code=400, detail="There are no accounts with this username! Please signup.")
        
        user = self.__userRepository.get_user_by_username(username=login_details.username)
        if HashHelper.verify_password(plain_password=login_details.password, hashed_password=user.password) :
            token = AuthHandler.sign_jwt(user_id=user.id) 
            if token :
                return UserWithToken(token=token)
            else :
                # if for any reason you can't sign a jwt token, raise an error.
                raise HTTPException(status_code=500, detail="Unable to process the request!")
            
        raise HTTPException(status_code=400, detail="Please check your credentials!") 

    def get_user_by_id(self, user_id : int) :
        user = self.__userRepository.get_user_by_id(user_id=user_id)
        if user : 
            return user 
        raise HTTPException(status_code=400, detail="User is not available!")


