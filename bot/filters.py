from telegram import Message
from telegram.ext import MessageFilter

import validators


class LinkFilter(MessageFilter):
    def filter(self, message: Message):
        result = validators.url(message.text)

        if isinstance(result, validators.ValidationFailure):
            return False

        return result


class InstagramPostFilter(MessageFilter):
    def filter(self, message: Message):
        return message.text.startswith('https://www.instagram.com/p/')


link_filter = LinkFilter()
instagram_post_filter = InstagramPostFilter()
