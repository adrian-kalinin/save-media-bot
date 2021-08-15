from telegram import Message
from telegram.ext import MessageFilter

import validators


class LinkFilter(MessageFilter):
    def filter(self, message: Message):
        if message.text:
            result = validators.url(message.text)

            if isinstance(result, validators.ValidationFailure):
                return False

            return result


link_filter = LinkFilter()
