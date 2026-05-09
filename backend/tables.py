from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Date, func, ForeignKey
from datetime import datetime
from database import Base


class User(Base) :

    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    bio = Column(Text(500))
    phone_number = Column(String, index=True)  
    date_of_birth = Column(Date, index=True)

    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)



class PasswordResetCode(Base) :

    __tablename__ = "PasswordResetCode"

    id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(ForeignKey("User.id"))
    code = Column(String(6), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    is_used = Column(Boolean, default=False)
