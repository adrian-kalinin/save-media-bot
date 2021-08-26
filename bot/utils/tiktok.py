from fake_useragent import FakeUserAgent
import requests
import re


def get_tiktok_video_id(url):
    pattern = r'https:\/\/www\.tiktok\.com/@[a-zA-Z0-9-_]+/video/([1-9]+).*'

    if result := re.search(pattern, url):
        return result.group(1)

    headers = {'User-Agent': FakeUserAgent(use_cache_server=False).random}
    response = requests.get(url, headers=headers)

    pattern = r'https:\/\/m\.tiktok\.com/v/([1-9]+).html'
    result = re.search(pattern, response.url)

    return result.group(1)

