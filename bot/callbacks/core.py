from telegram import Update, ParseMode
from telegram.ext import CallbackContext

from TikTokApi import TikTokApi
from instaloader import Post, BadResponseException
import logging

from settings import CHANNEL
from ..constants import Message
from ..utils.instagram import instaloader, get_inst_post_shortcode, send_instagram_post, send_instagram_carousel
from ..utils.tiktok import get_tiktok_video_id, send_tiktok_video
from ..utils import typing, sending_photo, sending_video, log_request


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
    shortcode = get_inst_post_shortcode(update.message.text)

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


@sending_video
def tiktok_video_callback(update: Update, context: CallbackContext):
    if video_id := get_tiktok_video_id(update.message.text):
        tiktok_api: TikTokApi = TikTokApi.get_instance()
        did = tiktok_api.generate_device_id()
        video_data = tiktok_api.get_tiktok_by_id(video_id, custom_device_id=did)

        if video_data.get('statusCode') == 0:
            send_tiktok_video(tiktok_api, did, video_data, update.effective_chat.id, context.bot)
            log_request(update.effective_user.id)

            return

        tiktok_url = update.effective_message.text.split('?')[0]
        status_code = video_data.get('statusCode')

        logging.warning(f'Could not get TikTok video at {tiktok_url} (status code: {status_code})')

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.invalid_tiktok_video
    )


@typing
def invalid_link_callback(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.invalid_link
    )
