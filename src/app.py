from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, List
from src.schemas.schemas import Product
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repositories.repositoryProduct import RepositoryProduct

create_db()

app = FastAPI()


@app.post('/products')
async def create_product(product: Product, db: Session = Depends(get_db)):
    created_product = RepositoryProductd(db).create(self, product)
    return created_product


@app.get('/products')
async def listProducts():
    products = RepositoryProduct(db).getAll()
    return products


@app.get('/user')
async def create_user(user: User, db: Session = Depends(get_db)):
    created_user = RepositoryUser(db).create(self, user)
