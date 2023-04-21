from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):
    id: Optional[str] = None
    name: str
    tel: str
    my_products: List[Product]
    sales: List[Order]
    orders: List[Order]

    class Config:
        orm_mode = True


class Product(BaseModel):
    id: Optional[str] = None
    name: str
    user: User
    description: str
    price: float
    avaivable: bool = False

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    quantity: int
    delivery: bool = True
    address: str
    obs: Optional[str] = 'No Obs'

    class Config:
        orm_mode = True
