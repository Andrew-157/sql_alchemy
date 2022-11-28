from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "mysql+mysqlconnector://root:password@127.0.0.1:3306/users", echo=True)

session = sessionmaker(bind=engine)()

Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(56))


class Contact(Base):

    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    user_id = Column(None, ForeignKey('users.id'))
    email = Column(String(50))


Base.metadata.create_all(engine)
Base.metadata.bind = engine

user_1 = User(name="Arnold")
session.add(user_1)

user_2 = User(name="Barry")
session.add(user_2)

session.commit()

for user in session.query(User).all():
    print(f"{user}--{user.id}--{user.name}")
