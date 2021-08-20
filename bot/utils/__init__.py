from telegram import Update, ChatAction
from telegram.ext import CallbackContext
from functools import wraps
import logging

from ..models import User


def log_request(user_id):
    query = User.update(requests=User.requests + 1).where(User.user_id == user_id)
    query.execute()

    logging.info(f'User {user_id} made a request')


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
            action=ChatAction.UPLOAD_PHOTO
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
