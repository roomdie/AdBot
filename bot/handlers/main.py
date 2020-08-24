import requests
# import channel_handler as x

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from states.token import UserToken

# callback
# from bot.handlers.callback_handlers.bot_callback import bot
# from bot.handlers.callback_handlers.channel_callback import channel
# from bot.handlers.callback_handlers.callback_handler import callback_handler

# message
from .message_handler.start_handler import start, check_referral
from .message_handler.bot_handler import bot_handler, token_handler
from .message_handler.channel_handler import channel_handler

dp.register_message_handler(start, commands='start')
dp.register_message_handler(check_referral, commands='referrals')
# dp.register_message_handler(bot_handler, regexp="🤖 Bot")
# dp.register_callback_query_handler(bot)
# dp.register_message_handler(token_handler, state=UserToken.token)
dp.register_message_handler(channel_handler, regexp="📢 Channel")
# dp.register_callback_query_handler(callback_handler)

