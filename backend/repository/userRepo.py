from repository.base import BaseRepository
from tables import *
from schema import *
class UserRepository(BaseRepository) :
    def create_user(self, user_data: UserCreate) :
        newUser = User(**user_data.model_dump(exclude_none=True))


        self.session.add(instance=newUser)
        self.session.commit()
        self.session.refresh(instance=newUser)

        return newUser
    

    def user_exist_by_username(self, username : str) -> bool:
        user = self.session.query(User).filter_by(username=username).first()

        return bool(user)
    
    def get_user_by_username(self, username : str) -> User:
        user = self.session.query(User).filter_by(username=username).first()

        return user 

    def get_user_by_id(self, user_id: int) :
        user = self.session.query(User).filter_by(id=user_id).first()

        return user 

