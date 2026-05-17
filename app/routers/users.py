from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from typing import Annotated

from fastapi import FastAPI, Depends

from app.models.user import User
from app.db.session import get_db

SessionDep = Annotated[AsyncSession, Depends(get_db)]

app = FastAPI()


@app.get("/users")
async def get_users(session: SessionDep, page=0, page_size=20):
    filtered_users = await session.execute(
        select(User.username, User.id)
        .where(User.deleted_at.is_(None))
        .limit(page_size)
        .offset(page * page_size)
    )

    return filtered_users.all()
