from bcrypt import checkpw, hashpw, gensalt


class HashHelper(object) :

    @staticmethod
    def verify_password(plain_password: str, hashed_password : str) :

        if checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8")) :
            return True
        
        return False
    
    @staticmethod
    def turn_pwd_into_hash(plain_password : str) :
        return hashpw(plain_password.encode("utf-8"), gensalt()).decode("utf-8")
    
