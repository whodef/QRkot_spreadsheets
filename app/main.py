from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings
from app.core.init_db import create_first_superuser

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description)

app.include_router(main_router)


@app.on_event('startup')
async def startup() -> None:
    """
    Выполнение задач при запуске приложения.

    Эта функция выполняется при запуске приложения FastAPI. Вызывается
    `create_first_superuser()` для создания начального суперпользователя.

    ### Raises:
         Любые исключения, вызванные `create_first_superuser()`, могут
         привести к сбою процесса запуска.
    """
    await create_first_superuser()


@app.get('/')
def read_root() -> dict:
    """
    Корневой endpoint, который приветствует пользователя.

    ### Gets:
    Получает приветственное сообщение.

    ### Returns:
    Словарь, содержащий приветственное сообщение.

        dict: {"Hello, Human":"Let's go to the docs"}
    """
    return {'Hello, Human': 'Let\'s go to the docs'}

