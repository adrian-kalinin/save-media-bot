from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


class States:
    prepare_mailing = 1
    received_mailing = 2


class CallbackData:
    statistics = 'statistics'
    mailing = 'mailing'
    backup = 'backup'


class ReplyButtons:
    send_mailing = 'Отправить'
    preview_mailing = 'Предпросмотр'
    cancel_mailing = 'Отмена'


class Keyboard:
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
        '<b>Instagram</b>: .\n'  # фото, видео, карусели и сторис
        '<b>TikTok</b>: '  # видео и музыка.
    )

    invalid_link = 'Вы прислали нерабочую ссылку, убедитесь в правильности ввода'

    admin = 'Добро пожаловать в админскую панель!'

    statistics = (
        '✨ <b>Статистика бота</b> ✨\n\n'
        'Количество пользователей: <b>{total_users}</b>\n'
        'Из них активных: <b>{active_users}</b>\n\n'
        'Запросов за всё время: <b>{total_requests}</b>'
    )

    sources = 'Статистика по источникам:\n\n'

    mailing = 'Отправьте сообщение для рассылки'

    received_mailing = 'Сообщение получено. Что дальше?'

    mailing_canceled = 'Рассылка отменена'

    mailing_started = 'Рассылка началась'

    mailing_finished = (
        'Сообщение отправлено успешно:\n\n'
        'Получившие пользователи: {sent_count}'
    )

    unexpected_error = '<code>Telegram Error: {error}.\n\n{update}</code>'

    backup = 'Бэкап базы данных ({})'

    database_not_found = 'База данных не найдена'
