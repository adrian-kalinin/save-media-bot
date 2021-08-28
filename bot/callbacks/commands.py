from telegram import Update, ParseMode, ReplyKeyboardRemove
from telegram.ext import CallbackContext
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
    user, created = User.get_or_create(user_id=update.effective_user.id)

    if created:
        logging.info(f'User {update.effective_user.id} started bot ')

        if args := context.args:
            source, _ = Source.get_or_create(name=args[0])
            source.users += 1
            source.save()

    if not user.active:
        user.active = True
        user.save()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.start, parse_mode=ParseMode.HTML,
        reply_markup=Keyboard.main
    )

