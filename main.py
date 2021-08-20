from telegram.ext import Updater

import logging

from bot.models import database, User, Source
from bot.callbacks import error_callback

from bot.handlers import (
    start_handler, admin_handler,
    statistics_handler, backup_handler, mailing_conversation_handler,
    how_to_use_handler, not_subscribed_handler,
    instagram_post_handler, invalid_link_handler
)

from settings import BOT_TOKEN


# set up logger
logging.basicConfig(
    format='%(asctime)s – %(levelname)s – %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO
)


# create updater
updater = Updater(BOT_TOKEN)
dispatcher = updater.dispatcher


# bound handlers to dispatcher
def bound_handlers():
    # noinspection PyTypeChecker
    dispatcher.add_error_handler(error_callback)

    # command handlers
    dispatcher.add_handler(admin_handler)
    dispatcher.add_handler(start_handler)

    # admin handlers
    dispatcher.add_handler(statistics_handler)
    dispatcher.add_handler(backup_handler)

    # mailing handlers
    dispatcher.add_handler(mailing_conversation_handler)

    # core handlers
    dispatcher.add_handler(how_to_use_handler)
    dispatcher.add_handler(not_subscribed_handler)
    dispatcher.add_handler(instagram_post_handler)
    dispatcher.add_handler(invalid_link_handler)


# set up database
def configure_database():
    database.connect()
    database.create_tables([User, Source])
    database.close()
    logging.info('Database has been configured')


# set up webhook
def configure_webhook():
    pass


def main():
    # setting up application
    bound_handlers()
    configure_database()
    configure_webhook()

    # start bot
    updater.start_polling()
    logging.info('Bot has started')


if __name__ == '__main__':
    main()
