from sqlalchemy import Column, BigInteger, String, Date
from config.database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(50))
    lastname = Column(String(50))
    username = Column(String(50))
    birthday = Column(Date)
    picture = Column(String(500))
    email = Column(String(100))
    password = Column(String(300))
