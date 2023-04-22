from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from src.schemas import schemas as s
from src.infra.sqlalchemy.models import models as m


class RepositoryProduct():
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: s.Product):
        db_product = m.Product(
            name=product.name, description=product.description, price=product.price, avaivable=product.avaivable
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def getAll(self):
        products = self.db.query(m.Product).all()
        return products

    def getOne(self, product_id: int):
        statement = select(m.Product).filter_by(id=product_id)
        product = self.db.execute(statement).one()

        return product

    def remove(self, product_id: int):
        statement = self.getOne(product_id).where(m.Product.id == product_id)

        self.db.delete(statement)
        self.db.commit()
