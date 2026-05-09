import jwt
from decouple import config
import time
from typing import Any

JWT_SECRET_KEY = config("JWT_SECRET_KEY")
JWT_ALGORITHM = config("JWT_ALGORITHM")


class AuthHandler(object) :

    @staticmethod
    def sign_jwt(user_id : int) -> str:
        payload : dict[str, Any] = {
            "user_id" : user_id,
            "expire_time" : time.time() + 900
        }

        token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

        return token
    
    @staticmethod
    def decode_jwt(token: str) -> dict :
        try :
            decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            return decoded_token if decoded_token["expire_time"] >= time.time() else None
        except :
            print("Unable to decode the token!")
            return None

