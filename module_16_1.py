from fastapi import FastAPI
from pydantic import BaseModel

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def main_page() -> dict:
    return {'message': 'Главная страница'}

'''GET-запрос — маршрут к страницe администратора'''
@app.get('/user/admin')
async def admin_page() -> dict:
    return {'message': 'Вы вошли как администратор'}

'''GET-запрос — маршрут к страницe пользователя'''
@app.get("/user/{user_id}")
async def user_page(user_id: int):
    return {'message': f"Вы вошли как пользователь № <{user_id}>"}

'''GET-запрос — маршрут к страницам пользователей: Имя: <username>, Возраст: <age>.
    вводить типа ->  user?username=Vova&age=55'''
@app.get("/user")  #/{username}/{age}
async def user_info(username: str, age: int) -> dict:
    return {'messege': f"Информация о пользователе. Имя: <{username}>, Возраст: <{age}>"}

