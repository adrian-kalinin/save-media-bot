from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from instaloader import Instaloader

from settings import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD


USER_AGENT = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
    ' AppleWebKit/605.1.15 (KHTML, like Gecko) '
    'Version/14.1.1 Safari/605.1.15'
)

instaloader = Instaloader(user_agent=USER_AGENT)
instaloader.login(
    user=INSTAGRAM_USERNAME,
    passwd=INSTAGRAM_PASSWORD
)


class States:
    prepare_mailing = 1
    received_mailing = 2


class CallbackData:
    statistics = 'statistics'
    mailing = 'mailing'
    backup = 'backup'


class ReplyButtons:
    how_to_use = '💬 Как использовать бота'

    send_mailing = 'Отправить'
    preview_mailing = 'Предпросмотр'
    cancel_mailing = 'Отмена'


class Keyboard:
    main = ReplyKeyboardMarkup([
        [ReplyButtons.how_to_use]
    ], resize_keyboard=True)

    admin = InlineKeyboardMarkup([
        [InlineKeyboardButton('Посмотреть статистику', callback_data=CallbackData.statistics)],
        [InlineKeyboardButton('Создать рассылку', callback_data=CallbackData.mailing)],
        [InlineKeyboardButton('Копировать базу данных', callback_data=CallbackData.backup)]
    ])

    mailing = ReplyKeyboardMarkup([
        [ReplyButtons.send_mailing],
        [ReplyButtons.preview_mailing, ReplyButtons.cancel_mailing]
    ], resize_keyboard=True)


class Message:
    start = (
        'Привет! Отправь мне ссылку на то, что надо скачать, и через мгновение я тебе всё отправлю. Сейчас '
        'поддерживается:\n\n'
        '<b>Instagram</b>: фото, видео и карусели.\n'
        # '<b>TikTok</b>: видео.'
    )

    how_to_use = (
        'Для скачивания фото, видео или карусели из Instagram пришлите ссылку следующего вида:\n\n'
        '<code>https://www.instagram.com/p/BYvh3Yel9iL/</code>'
    )

    not_subscribed = 'Чтобы пользоваться ботом, нужна подписка на канал — @{}'

    instagram_post_caption = '<b>Лайки: {}</b>\n\n{}'

    invalid_instagram_post = '💬 Вы прислали недоступный пост в Instagram, убедитесь в правильности ввода'

    invalid_link = '💬 Вы прислали нерабочую ссылку, убедитесь в правильности ввода'

    admin = 'Добро пожаловать в админскую панель!'

    statistics = (
        '💬 <b>Статистика бота</b>\n\n'
        'Количество пользователей: <b>{total_users}</b>\n'
        'Из них активных: <b>{active_users}</b>\n\n'
        'Запросов за всё время: <b>{total_requests}</b>'
    )

    sources = '💬 Статистика по источникам:\n\n'

    mailing = 'Отправьте сообщение для рассылки'

    received_mailing = 'Сообщение получено. Что дальше?'

    mailing_canceled = 'Рассылка отменена'

    mailing_started = 'Рассылка началась'

    mailing_finished = (
        '💬 Сообщение отправлено успешно:\n\n'
        'Получившие пользователи: {sent_count}'
    )

    unexpected_error = '<code>Telegram Error: {error}.\n\n{update}</code>'

    backup = 'Бэкап базы данных ({})'

    database_not_found = '💬 База данных не найдена'
