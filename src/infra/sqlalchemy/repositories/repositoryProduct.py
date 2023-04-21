from sqlalchemy.orm import Session
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

    def getOne(self):
        pass

    def remove(self):
        pass
