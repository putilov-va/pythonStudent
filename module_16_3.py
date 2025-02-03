from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated, Set
from fastapi import Path


app = FastAPI()

'''Создадим словарь (живёт до перезагрузки)'''
users = {'1': 'Имя: Example, возраст: 18'}

'''CRUD запросы'''
@app.get("/")
async def main_page() -> str:
    return "Главная страница"

@app.get('/users')
async def dict_page():
    return users

'''Создание новой записи пользователя.'''
@app.post('/user/{username}/{age}')
async def create_id(username: Annotated[str, Path(min_length=5,
                                                  max_length=22,
                                                  regex="^[A-Za-z0-9\\s]+$",
                                                  description='Enter username',
                                                  example='UrbanUser')],
                    age:     Annotated[int, Path(ge=18,
                                                 le=120,
                                                 description="Enter age",
                                                 example=24)]
                    ) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = [username], [age]
    return f'"User {user_id} is registered"'

'''Обновление данных записи.'''
@app.put('/user/{user_id}/{username}/{age}')
# async def update_id(user_id: int, username: str, age: int) -> dict:
async def update_id(user_id: Annotated[str, Path(min_length=1,
                                                  max_length=20,
                                                  regex="^[0-9]",
                                                  description='Enter id',
                                                  example='1')],
                    username: Annotated[str, Path(min_length=5,
                                                  max_length=22,
                                                  regex="^[A-Za-z0-9\\s]+$",
                                                  description='Enter username',
                                                  example='UrbanProfi')],
                    age:   Annotated[int,   Path(ge=18,
                                                 le=120,
                                                 description="Enter age",
                                                 example=28)]
                    ) -> str:
    users[user_id] = [username], [age]
    return f'"The user {user_id} is updated"'

@app.delete('/user/{user_id}')
async def dict_page(user_id: str) -> str:
    users.pop(user_id)
    return f'"User {user_id} has been deleted."'
