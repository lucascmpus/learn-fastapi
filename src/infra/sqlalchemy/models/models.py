from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from src.infra.sqlalchemy.config.database import Base

class Product():

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    avaivable = Column(Boolean)
