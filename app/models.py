from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Post(Base):
    __tablename__ = "Posts"
    

    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto") 
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    rating = Column(Integer, nullable=True)
    published = Column(Boolean, server_default='1', nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    owner_id = Column(Integer, ForeignKey("Users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto") 
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

class Vote(Base):
    __tablename__ = "Votes"
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False, primary_key=True)
    post_id = Column(Integer, ForeignKey("Posts.id"), nullable=False, primary_key=True)