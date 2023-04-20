from sqlalchemy.orm import Session
from src.schemas import schemas as s
from src.infra.sqlalchemy.models import models as m


class RepositoryProduct():
    def __init__(self, db: Session):
        self.db = db

    def create(self, produto: s.Product):
        db_product = m.Product(
            name=produto.name, description=produto.description, price=produto.price, avaivable=produto.avaivable
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def getAll(self):
        products = self.db.query(m.Product()).all()
        return products

    def getOne(self):
        pass

    def remove(self):
        pass
