from telegram import Bot, InputMediaPhoto, InputMediaVideo, ParseMode
from instaloader import Instaloader, Post
import requests
import re

from settings import USE_SESSION, INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD
from ..constants import Message, USER_AGENT
from ..utils import separate_thousand


# set up instaloader
instaloader = Instaloader(user_agent=USER_AGENT)

if USE_SESSION:
    instaloader.load_session_from_file(INSTAGRAM_USERNAME, f'sessions/session-{INSTAGRAM_USERNAME}')

instaloader.login(user=INSTAGRAM_USERNAME, passwd=INSTAGRAM_PASSWORD)


def get_inst_post_shortcode(url: str):
    if result := re.search(r'https:\/\/www.instagram.com\/p\/([a-zA-Z0-9-_\.]+)\/.*', url):
        return result.group(1)


def send_instagram_post(post: Post, bot: Bot, chat_id: int):
    if post.is_video:
        bot.send_video(chat_id=chat_id, video=requests.get(post.video_url).content)

    else:
        bot.send_photo(chat_id=chat_id, photo=requests.get(post.url).content)

    if caption := post.caption:
        caption += '\n\n'

    caption = Message.instagram_post_caption.format(
        likes=separate_thousand(post.likes), caption=caption or ' ',
        username1=bot.get_me().username, username2=bot.get_me().username
    )

    bot.send_message(
        chat_id=chat_id, text=caption,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def send_instagram_carousel(post: Post, bot: Bot, chat_id: int):
    media_entities = []

    for node in post.get_sidecar_nodes():
        if node.is_video:
            video = requests.get(node.video_url).content
            media_entities.append(InputMediaVideo(video))
        else:
            photo = requests.get(node.display_url).content
            media_entities.append(InputMediaPhoto(photo))

    bot.send_media_group(
        chat_id=chat_id,
        media=media_entities
    )

    if caption := post.caption:
        caption += '\n\n'

    text = Message.instagram_post_caption.format(
        likes=separate_thousand(post.likes), caption=caption or ' ',
        username1=bot.get_me().username, username2=bot.get_me().username
    )

    bot.send_message(
        chat_id=chat_id, text=text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )
