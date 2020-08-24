import requests

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher

from states.token import UserToken
# from bot_db import add, bot_db.update, select_all, bot_db.select_column, delete_bot, first_try
from datebase import bot_db

import logging
import aiohttp
import time
import datetime

from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

PROXY_URL = 'socks5://45.89.19.2:9313'
PROXY_AUTH = aiohttp.BasicAuth(login='xH6y1z', password='871xvl90fD')


async def bot_handler(message: types.Message, state:FSMContext):
    # user
    user_id = message.from_user.id
    username_user = message.from_user.username
    # db
    row = bot_db.select_row(user_id)
    # user bot
    username_bot = row[3]
    date_time = row[4]
    # inline keyboard
    markup = types.InlineKeyboardMarkup()
    if username_bot == '':
        add_button = types.InlineKeyboardButton(text="+", callback_data="add_bot")
        markup.row(add_button)
        # UserToken.set.token()
    else:
        info_button = types.InlineKeyboardButton(text="@{}".format(username_bot), callback_data="about_bot")
        markup.row(info_button)

    await message.answer(
        "Your Bot", reply_markup=markup
    )


async def token_handler(message: types.Message, state: FSMContext):
    # bot
    user_token = message.text
    # user
    user_id = message.from_user.id
    username_user = "{}".format(message.from_user.username)
    # db
    row = bot_db.select_row(user_id)
    all_row = bot_db.select_all()
    # date time
    date_time = datetime.datetime.now().date()
    # response = requests.post("https://api.telegram.org/bot{}/getMe".format(token))
    if len(user_token) >= 46 and ":" in user_token:
        # await state.bot_db.update_data(token1=user_token)
        user_bot = Bot(token=user_token, parse_mode=types.ParseMode.HTML, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
        getting_username_bot = await user_bot.get_me()
        username_bot = getting_username_bot["username"]
        for i in all_row:
            if (username_bot or user_token) in i:
                await message.answer("Бот уже добавлен другим пользователем.")
                await state.finish()
                break
            else:
                bot_db.update("username_bot", username_bot, "user_id", user_id)
                bot_db.update("username_user", username_user, "user_id", user_id)
                bot_db.update("token", user_token, "user_id", user_id)
                bot_db.update("date_time", date_time, "user_id", user_id)
                await message.answer(
                        "Бот добавлен. Нажмите снова на кнопку 🤖 Bot, чтобы узнать информацию про вашего бота. "
                    )
                await state.finish()
                break
    else:
        await message.answer("Ваш токен не валидный.")
        await state.finish()