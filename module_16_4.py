from fastapi import FastAPI, HTTPException, Path, Body
from pydantic import BaseModel
from typing import Annotated, Set, List, Tuple, Union, Any

app = FastAPI()

'''Создадим список (живёт до перезагрузки)'''

users = []


class User(BaseModel):
    id: int  # номер
    username: Annotated[str, Path(min_length=5,
                                  max_length=22,
                                  regex="^[A-Za-z0-9\\s]+$",
                                  description='Enter username',
                                  example='Urbanuser')]
    age: Annotated[int, Path(ge=18,
                             le=120,
                             description="Enter age",
                             example=24)]  # возраст


@app.get('/users', response_model=List[User])
async def get_page() -> List[User]:
    return users


'''Создание новой записи пользователя.'''
@app.post(path='/user/{username}/{age}')
async def create_id(username: str, age: int) -> str:
    User.username = username
    User.age = age
    new_id = max((i.id for i in users), default=0) + 1  #  Создаём индекс
    new_user = User(id=new_id, username=username, age=age)  # Конфигурация списка (база)
    users.append(new_user)
    return f'Добавлен {new_id} пользователь.'


'''Обновление данных записи.'''
@app.put('/user/{id}/{username}/{age}')
async def update_id(id: int, username: str, age: int) -> set:
    try:
        edit_user = users[id - 1]
        edit_user.username = username
        edit_user.age = age
        return {f"The user <{id}> is updated"}
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def dict_page(id: int):
    '''Подсчёт количества итераций списка'''
    calls = 0
    for i in list(users):
        calls += 1
        for key, value in i:
            # try:
            if key == 'id' and value == id:
                del users[calls - 1]
                return {f'Delet: {id}'}
    raise HTTPException(status_code=404, detail="User was not found")
