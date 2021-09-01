from telegram import Message, Update, Bot
from telegram.ext import MessageFilter, UpdateFilter

import validators
import re

from settings import BOT_TOKEN, CHANNEL, DEBUG


bot = Bot(BOT_TOKEN)


class SubscribedFilter(UpdateFilter):
    def filter(self, update: Update):
        if not DEBUG:
            chat_member = bot.get_chat_member(
                chat_id=CHANNEL,
                user_id=update.effective_user.id
            )
            return chat_member.status in ('member', 'creator', 'administrator')

        return True


class LinkFilter(MessageFilter):
    def filter(self, message: Message):
        result = validators.url(message.text)

        if isinstance(result, validators.ValidationFailure):
            return False

        return result


class InstagramPostFilter(MessageFilter):
    def filter(self, message: Message):
        return re.search(r'https:\/\/www\.instagram\.com\/p\/[a-zA-Z0-9-_]+\/.*', message.text)


class TikTokVideoFilter(MessageFilter):
    def filter(self, message: Message):
        short_link_result = re.search(r'https:\/\/vm\.tiktok\.com\/[a-zA-Z0-9-_]+\/.*', message.text)
        full_link_result = re.search(r'https:\/\/www\.tiktok\.com\/@[a-zA-Z0-9-_\.]+\/video\/([1-9]+).*', message.text)
        return short_link_result or full_link_result


subscribed = SubscribedFilter()
link = LinkFilter()
instagram_post = InstagramPostFilter()
tiktok_video = TikTokVideoFilter()
