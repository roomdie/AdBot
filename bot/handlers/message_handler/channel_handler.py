import requests

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher

from states.token import UserToken, ChannelId
# from bot_db import add, update, select_all, channel_db.select_row, delete_bot, first_try
from datebase import bot_db

import logging
import aiohttp
import time
import datetime

from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

db = bot_db.DBCommands()


async def new_channel(message: types.Message):
    chat_id = message.from_user.id

    db.add_channel()

async def channel_handler(message: types.Message):
    # user id of bot
    chat_id = message.from_user.id
    channel = await db.check_channel()
    print(channel)
    markup = types.InlineKeyboardMarkup()
    if channel is None:
        add_button = types.InlineKeyboardButton(text="+", callback_data="add_channel")
        markup.row(add_button)
    else:
        first_channel_button = types.InlineKeyboardButton(
            text="@{}".format(channel), callback_data="about_first_channel"
        )
        markup.row(first_channel_button)

    await message.answer(
        "Your Channel's", reply_markup=markup
    )


async def channel_id_handler(message: types.Message, state: FSMContext):
    id = message.text
    await db.add_channel(id, 0)
    await state.finish()
# next callback handler
