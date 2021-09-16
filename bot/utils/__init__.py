from telegram import Update, ChatAction
from telegram.ext import CallbackContext
from functools import wraps
import locale
import logging

from ..models import User


locale.setlocale(locale.LC_ALL, 'en_US')


def log_request(user_id):
    query = User.update(requests=User.requests + 1).where(User.user_id == user_id)
    query.execute()

    logging.info(f'User {user_id} made a request')


def separate_thousand(number):
    local_number = locale.format_string('%d', number, grouping=True)
    return local_number.replace(',', ' ')


def typing(func):
    @wraps(func)
    def wrapper(update: Update, context: CallbackContext):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action=ChatAction.TYPING
        )
        func(update, context)
    return wrapper


def sending_photo(func):
    @wraps(func)
    def wrapper(update: Update, context: CallbackContext):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action=ChatAction.UPLOAD_PHOTO
        )
        func(update, context)
    return wrapper


def sending_video(func):
    @wraps(func)
    def wrapper(update: Update, context: CallbackContext):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action=ChatAction.UPLOAD_VIDEO
        )
        func(update, context)
    return wrapper


def sending_document(func):
    @wraps(func)
    def wrapper(update: Update, context: CallbackContext):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action=ChatAction.UPLOAD_DOCUMENT
        )
        func(update, context)
    return wrapper
