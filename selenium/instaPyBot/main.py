from instapy import InstaPy


session = InstaPy(
    username='motorolets',
    password='tyktyktyk1999',
    headless_browser=True
)

# Бот будет комментировать, пока не достигнет своего часового и дневного лимита.
# Он возобновит комментирование после истечения периода квоты.
session.set_quota_supervisor(
    enabled=True,
    peak_comments_daily=240,
    peak_comments_hourly=21
)

# Боту не понравится или не прокомментирует любое изображение, которое ClarifAI считает NSFW.
session.set_use_clarifai(enabled=True, api_key='1b3b2f8e820040ccb907987e6d219d77')
session.clarifai_check_img_for(['nsfw'])

# Бот не будет взаимодействовать с сообщениями пользователей, у которых более 8500 подписчиков.
session.set_relationship_bounds(enabled=True, max_followers=8500)

session.login()

# Понравятся 5 лучших постов из списка тегов
session.like_by_tags(['programming', 'MMA'], amount=5)

# С этим изменением посты, в которых есть слова naked или nsfw описания, не понравятся.
session.set_dont_like(["naked", "nsfw"])

# Бот будет следить за пятьдесят процентами пользователей, чьи посты ему понравились.
#session.set_do_follow(True, percentage=50)

# Комментирование. Бот оставит один из этих трех комментариев
# на половине сообщений, с которыми он взаимодействует.
#session.set_do_comment(True, percentage=50)
#session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])

# Закроет браузер, сохранит журналы и подготовит отчет,
# который вы можете увидеть в выводе консоли.
session.end()