from sqlalchemy import Column, Integer, func
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:
    """
    Подготовительный класс для ORM-моделей.
    Устанавливает название таблиц в формате `lowercase`
    и автоматическое добавление столбца `id` с типом `int`.
    """
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.database_url)

AsyncSessionLocal = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)


datetime_func = None
if settings.database_url.startswith('sqlite'):
    datetime_func = func.julianday
else:
    raise Exception(
        'Не определена функция извлечения времени из БД!'
    )


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
