from telegram import Update, ParseMode
from telegram.ext import CallbackContext

from instaloader import Post, BadResponseException

from settings import CHANNEL
from ..constants import Message, instaloader
from ..utils.instagram import get_shortcode, send_instagram_post, send_instagram_carousel
from ..utils import typing, sending_photo, log_request


@typing
def not_subscribed_callback(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.not_subscribed.format(CHANNEL)
    )


@typing
def how_to_use_callback(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.how_to_use,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


@sending_photo
def instagram_post_callback(update: Update, context: CallbackContext):
    shortcode = get_shortcode(update.message.text)

    try:
        post = Post.from_shortcode(instaloader.context, shortcode)

    except BadResponseException:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Message.invalid_instagram_post
        )
        return

    log_request(update.effective_user.id)

    if post.mediacount == 1:
        send_instagram_post(
            post=post, bot=context.bot,
            chat_id=update.effective_chat.id,
        )

    else:
        send_instagram_carousel(
            post=post, bot=context.bot,
            chat_id=update.effective_chat.id,
        )


@typing
def invalid_link_callback(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.invalid_link
    )
