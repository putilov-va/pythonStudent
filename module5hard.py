class User:
    """
    Содержит атрибуты: логин и пароль.
    """
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname              # имя пользователя, строка
        self.password = password              # в хэшированном виде, число
        self.age = age                        # возраст, число

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __hash__(self):
        return hash(self.password)

class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title                    # заголовок, строка
        self.duration = duration              # продолжительность, секунды
        self.time_now = time_now              # секунда остановки (изначально 0)
        self.adult_mode = adult_mode          # ограничение по возрасту, bool (False по умолчанию)

    def str_(self):
        return f"{self.title}"

import time
import hashlib

class UrTube:

    def __init__(self):
        self.users = []                 # список объектов User
        self.videos = []               # список объектов Video
        self.current_user = None        # текущий пользователь, User
    def log_in(self, nickname: str, password: str):
        hash_password = hashlib.sha512(password.encode('utf-8')).digest()   # Усиленное хеширование
        # print(hash_password)
        for user in self.users:                             # проверка на зарегестрированный login
            if nickname == user.nickname and hash_password == user.password:
                self.current_user = user

    def register(self, nickname: str, password: str, age: int):
        hash_password = hashlib.sha512 (password.encode('utf-8')).digest()  # Усиленное хеширование
        new_user = User(nickname, hash_password, age)

        if new_user not in self.users:                       # проверка на свободность login
            self.users.append(new_user)
            self.log_in(nickname, password)                 # присвоение logina
        else:
            print(f"Пользователь {nickname} уже существует")


    def log_out(self):
        self.current_user = None

    def get_titels_videos(self):                    # список видео в базе
        list_titels = []
        for video in self.videos:
            list_titels.append(video.title)
        return list_titels

    def add(self, *args):                           # добовление видео
        for movie in args:
              if movie.title not in self.get_titels_videos():
                 self.videos.append(movie)

    def get_videos(self, text: str):          # поисковик по слову
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie: str):        # просмотр видео
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if movie == video.title:
                    if video.adult_mode and self.current_user.age<18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for i in range(video.time_now+1, video.duration+1):
                            print(i, end=' ')
                            time.sleep(1)           # модуль time, с задержкой 1 сек
                        print('Конец видео')        # print(i, end=' ')


    def str(self):
        return f"{self.videos}"


#_______________
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# if __name__ == '__main__':
#     print_hi('PyCharm')