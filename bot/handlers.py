from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters

from .constants import CallbackData, States, ReplyButtons
from .filters import link, instagram_post, subscribed
from .callbacks import *
from settings import ADMINS


# command handlers
admin_handler = CommandHandler(
    command='admin', callback=admin_command_callback,
    filters=Filters.private & Filters.user(user_id=ADMINS)
)

start_handler = CommandHandler(
    command='start', callback=start_command_callback,
    filters=Filters.private
)

# admin handlers
statistics_handler = CallbackQueryHandler(
    pattern=CallbackData.statistics,
    callback=statistics_callback
)

backup_handler = CallbackQueryHandler(
    pattern=CallbackData.backup,
    callback=backup_callback
)

# mailing handlers
mailing_conversation_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(pattern=CallbackData.mailing, callback=mailing_callback)],
    states={
        States.prepare_mailing: [MessageHandler(callback=mailing_message_callback, filters=Filters.all)],
        States.received_mailing: [
            MessageHandler(filters=Filters.text(ReplyButtons.preview_mailing), callback=preview_mailing_callback),
            MessageHandler(filters=Filters.text(ReplyButtons.cancel_mailing), callback=cancel_mailing_callback),
            MessageHandler(filters=Filters.text(ReplyButtons.send_mailing), callback=send_mailing_callback)
        ]
    },
    fallbacks=[]
)

# core handlers
how_to_use_handler = MessageHandler(
    filters=Filters.private & Filters.text(ReplyButtons.how_to_use),
    callback=how_to_use_callback
)

not_subscribed_handler = MessageHandler(
    filters=Filters.private & Filters.text & link & ~subscribed,
    callback=not_subscribed_callback
)

instagram_post_handler = MessageHandler(
    filters=Filters.private & Filters.text & link & instagram_post & subscribed,
    callback=instagram_post_callback

)

invalid_link_handler = MessageHandler(
    filters=Filters.private & Filters.text & ~link,
    callback=invalid_link_callback
)
