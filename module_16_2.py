from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated
from fastapi import Path


# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def main_page() -> str:
    return "Главная страница"

'''GET-запрос — маршрут к страницe администратора'''
@app.get('/user/admin')
async def user_page() -> str:
    return "Вы вошли как администратор"

'''GET-запрос — маршрут к страницам пользователей: Имя: <username>, Возраст: <age>.
    вводить типа ->  user?username=Vovan&age=55'''
@app.get('/user/{username}/{age}')
async def user_info(username: Annotated[str, Path(min_length=5,
                                                  max_length=20,
                                                  regex="^[A-Za-z0-9\\s]+$",
                                                  description='Enter username',
                                                  example='UrbanUser')],
                    age:     Annotated[int, Path(ge=18,
                                                 le=120,
                                                 description="Enter age",
                                                 example=24)]
                    ) -> str:

    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

'''GET-запрос — маршрут к страницe пользователя'''
@app.get("/user/{user_id}")
async def user_page(user_id: Annotated[int, Path(ge=1,
                                                 le=100,
                                                 description="Enter User ID",
                                                 example=1)]
                    ) -> str:
    return f"Вы вошли как пользователь № {user_id}"
