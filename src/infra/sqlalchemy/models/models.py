from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship


class Product():

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    avaivable = Column(Boolean)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref=backref("user", uselist=False))


class User():

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    tel = Column(String)


class Order():

    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref=backref("user", uselist=False))
    quantity = Column(Integer)
    delivery = Column(Boolean)
    address = Column(String)
    obs = Column(String, nullable=True)


class Sales():

    __tablename__ = 'sales'
