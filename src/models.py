import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DATE,Table
from sqlalchemy.orm import relationship, declarative_base,backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class FollowersUser(Base):
    __tablename__ = 'FollowersUser'
    user_id = Column(Integer, ForeignKey(
        'user.id'), primary_key=True)
    follower_id = Column(Integer, ForeignKey('follower.id'), primary_key=True)

class User(Base):
    __tablename__ = 'user'
    id= Column(Integer,primary_key=True,autoincrement=True)
    username= Column(String(250),nullable=False)
    first_name= Column(String(250))
    last_name= Column(String(250))
    email= Column(String(100), unique=True)


    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer,primary_key=True,autoincrement=True)


    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user = relationship("User")
    user_id = Column(Integer,ForeignKey("user.id"),nullable=False)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer,primary_key=True,autoincrement=True)
    Comment = Column(String(500),nullable=False)

    user = relationship("User")
    author_id = Column(Integer,ForeignKey("user.id"), nullable=False)

    post = relationship("Post")
    post_id = Column(Integer,ForeignKey("post.id"), nullable=False)

class History(Base):
    __tablename__ = 'history'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user = relationship("User")
    id_user = Column(Integer,ForeignKey("user.id"), nullable=False)
    Init_Date = Column(DATE,nullable=False)
    def to_dict(self):
        return {}
    

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer,primary_key=True,autoincrement=True)
    type = Column(String(255),nullable=False)
    url = Column(String(250),nullable=False)
    post = relationship("Post")
    post_id = Column(Integer,ForeignKey("post.id"), nullable=False)
    history = relationship("history")
    history_id = Column(Integer,ForeignKey("history.id"), nullable=False)


class Like(Base):
    __tablename__ = 'Like'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user = relationship("User")
    id_user = Column(Integer,ForeignKey("user.id"), nullable=False)
    post = relationship("Post")
    id_post = Column(Integer,ForeignKey("post.id"), nullable=False)
    history = relationship("History")
    id_history = Column(Integer,ForeignKey("history.id"), nullable=False)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
