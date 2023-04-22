from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Product, ProductSimple
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repositories.repositoryProduct import RepositoryProduct


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProductSimple)
async def create_product(product: Product, db: Session = Depends(get_db)):
    created_product = RepositoryProductd(db).create(self, product)
    return created_product


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[Product])
async def listProducts(db: Session = Depends(get_db)):
    products = RepositoryProduct(db).getAll()
    return products


@router.delete('/{id}')
async def deleteProduct():
    pass
