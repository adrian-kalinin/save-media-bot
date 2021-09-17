from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from peewee import DoesNotExist
import logging

from ..models import User, Source
from ..constants import Message, Keyboard
from ..utils import typing


@typing
def admin_command_callback(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.admin, reply_markup=Keyboard.admin
    )


@typing
def start_command_callback(update: Update, context: CallbackContext):
    try:
        user = User.get(user_id=update.effective_user.id)

        if not user.active:
            user.active = True
            user.save()

    except DoesNotExist:
        User.create(user_id=update.effective_user.id)

        if args := context.args:
            source, _ = Source.get_or_create(name=args[0])
            source.users += 1
            source.save()

        logging.info(f'User {update.effective_user.id} started bot ')

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.start, parse_mode=ParseMode.HTML,
        reply_markup=Keyboard.main
    )

