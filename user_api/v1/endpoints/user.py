from typing import List
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.user import UserModel
from schemas.user import UserSchema
from core.deps import get_session


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserSchema)
async def post_user(user: UserSchema, db: AsyncSession = Depends(get_session)):
    new_user = UserModel(
        name=user.name,
        cpf=user.cpf,
        email=user.email,
        phone_number=user.phone_number,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )
    db.add(new_user)
    await db.commit()
    return new_user


@router.get('/', response_model=List[UserSchema])
async def get_users(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel)
        result = await session.execute(query)
        users: List[UserModel] = result.scalars().all()
        return users


@router.get('/{user_id}', response_model=UserSchema, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        user = result.scalar_one_or_none()

        if user:
            return user
        else:
            raise HTTPException(dateil='User not found', status_code=status.HTTP_404_NOT_FOUND)


@router.put('/{user_id}', response_model=UserSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_user(user_id: int, user: UserSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        user_update = result.scalar_one_or_none()

        if user_update:
            user_update.name = user.name
            user_update.cpf = user.cpf
            user_update.email = user.email
            user_update.phone_number = user.phone_number
            user_update.created_at = user.created_at
            user_update.updated_at = user.updated_at

            await session.commit()

            return user_update
        else:
            raise HTTPException(dateil='User not found', status_code=status.HTTP_404_NOT_FOUND)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        user_delete = result.scalar_one_or_none()

        if user_delete:
            await session.delete(user_delete)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(dateil='User not found', status_code=status.HTTP_404_NOT_FOUND)
