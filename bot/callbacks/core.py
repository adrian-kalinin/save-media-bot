from telegram import Update
from telegram.ext import CallbackContext

from ..constants import Message


def instagram_post_callback(update: Update, context: CallbackContext):
    print('instagram post')


def invalid_link_callback(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.invalid_link
    )
