from time import sleep


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __repr__(self):
        return self.nickname

class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title


class UrTube:

    def __init__(self):
        self.users: list[User] = []
        self.videos: list[Video] = []
        self.current_user = None

    """
    Методы для работы с пользователем - класс User
    """

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')
                return  # Пользователь уже существет => выход из регистрации
        # В противном случае => добавить нового пользователя в users[]
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        # Автоматический вход после регистрации
        self.log_in(new_user.nickname, new_user.password)

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname and hash(user.password) == hash(password):
                self.current_user = user

    def log_out(self):
        self.current_user = None
        print('Выход выполнен успешно.')

    """
        Методы для работы с видео - класс Video
    """

    def add(self, *new_videos):
        for new_video in new_videos:
            self.videos.append(new_video)

    def get_videos(self, post_request: str):
        found_videos: list[Video] = []
        for video in self.videos:
            if post_request.lower() in video.title.lower():
                found_videos.append(video)
        return found_videos

    def watch_video(self, video_title):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == video_title:
                if self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу.')
                    return
                while (video.time_now <= video.duration):
                    #sleep(1)
                    print(video.time_now)
                    video.time_now += 1
                print("Конец видео")





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
