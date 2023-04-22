from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import User
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repositories.repositoryUser import RepositoryUser

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user: User, db: Session = Depends(get_db)):
    created_user = RepositoryUser(db).create(self, user)
    return created_user


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[User])
async def listUsers(db: Session = Depends(get_db)):
    users = RepositoryUser(db).getAll()
    return users


@router.get('/{id_user}', status_code=status.HTTP_200_OK, response_model=Users)
async def getOne(id_user: int, db: Session = Depends(get_db)):
    user = RepositoryUser(db).getOne(id_user)
    return user


@router.delete('/{user_id}', status_code=status.HTTP_200_OK)
async def deleteUser(user_id: int, db: Session = Depends(get_db)):
    return 'ok'
