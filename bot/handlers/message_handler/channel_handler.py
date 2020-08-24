import requests

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher

from states.token import UserToken, ChannelId
# from bot_db import add, update, select_all, channel_db.select_row, delete_bot, first_try
from datebase import bot_db
from datebase import channel_db

import logging
import aiohttp
import time
import datetime

from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


async def channel_handler(message: types.Message):
    # user id of bot
    user_id = message.from_user.id
    channel_row = channel_db.select_row(user_id)
    count_subs = 0
    # add bot check
    bot_row = bot_db.select_row(user_id)
    user_bot = bot_row[3]
    # channels
    first_channel = channel_row[3]
    # just inline keyboard
    markup = types.InlineKeyboardMarkup()
    if first_channel == '':
        add_button = types.InlineKeyboardButton(text="+", callback_data="add_channel")
        markup.row(add_button)
    else:
        # first channel
        first_channel_button = types.InlineKeyboardButton(
            text="@{}".format(first_channel), callback_data="about_first_channel"
        )
        markup.row(first_channel_button)

    await message.answer(
        "Your Channel's", reply_markup=markup
    )

