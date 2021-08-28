from telegram import ParseMode, Bot
from TikTokApi import TikTokApi
from fake_useragent import FakeUserAgent
import requests
import re

from ..constants import Message


def get_tiktok_video_id(url: str):
    first_pattern = r'.*tiktok\.com\/@[a-zA-Z0-9-_]+\/video\/([1-9]+).*'
    second_pattern = r'.*tiktok\.com\/v\/([0-9]+).html.*'

    if result := re.search(first_pattern, url):
        return result.group(1)

    headers = {'User-Agent': FakeUserAgent().random}
    response = requests.get(url, headers=headers)

    if result := re.search(first_pattern, response.url):
        return result.group(1)

    elif result := re.search(second_pattern, response.url):
        return result.group(1)


def send_tiktok_video(tiktok_api: TikTokApi, did: str, video_data: dict, chat_id: int, bot: Bot):
    download_url = video_data['itemInfo']['itemStruct']['video']['downloadAddr']
    video = tiktok_api.get_video_by_download_url(download_url, custom_device_id=did)

    caption = Message.tiktok_video_caption.format(
        views=video_data['itemInfo']['itemStruct']['stats']['playCount'],
        likes=video_data['itemInfo']['itemStruct']['stats']['diggCount'],
        caption=video_data['itemInfo']['itemStruct']['desc'] + '\n\n' or ' ',
        username1=bot.get_me().username, username2=bot.get_me().username
    )

    bot.send_video(
        chat_id=chat_id, video=video,
        caption=caption, parse_mode=ParseMode.HTML
    )
