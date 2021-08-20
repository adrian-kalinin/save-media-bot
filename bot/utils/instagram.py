from telegram import Bot, InputMediaPhoto, InputMediaVideo, ParseMode, ChatAction
from instaloader import Post
import requests
import re

from ..constants import Message


def get_shortcode(url: str):
    if result := re.search(r'https:\/\/www.instagram.com\/p\/([a-zA-Z0-9-_]+)\/.*', url):
        return result.group(1)


def send_instagram_post(post: Post, bot: Bot, chat_id: int):
    caption = Message.instagram_post_caption.format(str(post.likes), post.caption)

    if post.is_video:
        video = requests.get(post.video_url).content

        bot.send_video(
            chat_id=chat_id, video=video,
            caption=caption, parse_mode=ParseMode.HTML
        )

    else:
        photo = requests.get(post.url).content

        bot.send_photo(
            chat_id=chat_id, photo=photo,
            caption=caption, parse_mode=ParseMode.HTML
        )


def send_instagram_carousel(post: Post, bot: Bot, chat_id: int):
    media_entities = []

    for node in post.get_sidecar_nodes():
        if node.is_video:
            video = requests.get(node.video_url).content
            media_entities.append(InputMediaVideo(video))
        else:
            media_entities.append(InputMediaPhoto(node.display_url))

    bot.send_media_group(
        chat_id=chat_id,
        media=media_entities
    )

    if post.caption:
        bot.send_message(
            chat_id=chat_id,
            text=Message.instagram_post_caption.format(str(post.likes), post.caption),
            parse_mode=ParseMode.HTML
        )
