from fake_useragent import FakeUserAgent
import requests
import re


def get_tiktok_video_id(url):
    first_pattern = r'https:\/\/www\.tiktok\.com/@[a-zA-Z0-9-_]+/video/([1-9]+).*'
    second_pattern = r'https:\/\/m\.tiktok\.com/v/([1-9]+).html'

    if result := re.search(first_pattern, url):
        return result.group(1)

    headers = {'User-Agent': FakeUserAgent().random}
    response = requests.get(url, headers=headers)

    if result := re.search(first_pattern, response.url):
        return result.group(1)

    elif result := re.search(second_pattern, response.url):
        return result.group(1)
