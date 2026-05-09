from sqlalchemy.orm import Session

class BaseRepository :

    # create a session so that the repository can communicate with database
    def __init__(self, session: Session) -> None:
        self.session = session