from sqlalchemy.orm import Session
from src.schemas import schemas as s
from src.infra.sqlalchemy.models import models as m


class RepositoryUser():
    def __init__(self, db: Session):
        self.db = db

    def create(self):
        db_user = m.User
        return

    def getAll(self):
        return

    def getOne(self):
        return

    def remove(self):
        return
