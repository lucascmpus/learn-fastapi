from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from src.schemas import schemas as s
from src.infra.sqlalchemy.models import models as m


class RepositoryUser():
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: s.User):
        db_user = m.User(
            name=user.name, tel=user.tel
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def getAll(self):
        users = self.db.query(m.User).all()
        return users

    def getOne(self, user_id: int):
        statement = select(m.User).filter_by(id=user_id)
        user = self.db.execute(statement).one()

        return user

    def remove(self, user_id: int):
        statement = self.getOne(user_id).where(m.User.id == user_id)

        self.db.delete(statement)
        self.db.commit()
