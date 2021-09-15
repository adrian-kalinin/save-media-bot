from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


USER_AGENT = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
    ' AppleWebKit/605.1.15 (KHTML, like Gecko) '
    'Version/14.1.1 Safari/605.1.15'
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
        '<b>TikTok</b>: видео.'
    )

    how_to_use = (
        'Для скачивания фото, видео или карусели из Instagram пришлите ссылку следующего вида:\n\n'
        '<code>https://www.instagram.com/p/BYvh3Yel9iL/</code>\n\n'
        'Для скачивания видео из TikTok пришлите ссылку следующего вида:\n\n'
        '<code>https://vm.tiktok.com/ZSJvpWXK4/</code> или '
        '<code>https://www.tiktok.com/@therock/video/6824918631965576454</code>'
    )

    not_subscribed = 'Чтобы пользоваться ботом, нужна подписка на канал — {}'

    instagram_post_caption = (
        '<b>Лайки: {likes}</b>\n\n{caption}'
        'Рад был помочь! Ваш, <a href="https://t.me/{username1}?start=share">@{username2}</a>'
    )

    tiktok_video_caption = (
        '<b>Просмотры: {views}\nЛайки: {likes}</b>\n\n{caption}'
        'Рад был помочь! Ваш, <a href="https://t.me/{username1}?start=share">@{username2}</a>'
    )

    invalid_instagram_post = '💬 Не удалось получить пост в Instagram'

    invalid_tiktok_video = '💬 Не удалось получить видео в TikTok'

    invalid_link = '💬 Вы прислали нерабочую ссылку, убедитесь в правильности ввода'

    admin = 'Добро пожаловать в админскую панель!'

    statistics = (
        '💬 <b>Статистика бота</b>\n\n'
        'Активных пользователей: <b>{active_users}</b>\n'
        'Всего пользователей: <b>{total_users}</b>\n\n'
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
