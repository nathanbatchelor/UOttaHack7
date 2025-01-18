from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base

class Users(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True)
  hashed_password = Column(String)