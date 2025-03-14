from fastapi import HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from sqlalchemy.ext.asyncio import AsyncSession


class transaction:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type: Exception, exc_val: str, exc_tb: str):
        if not exc_type:
            await self.__session.commit()
            return
        
        await self.__session.rollback()
        await self.__session.close()
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{exc_type}: {exc_val}\n"
        )
