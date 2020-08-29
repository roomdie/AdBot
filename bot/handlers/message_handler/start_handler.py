from datebase import bot_db
from loader import dp, bot
from aiogram import types

db = bot_db.DBCommands()


async def start(message: types.Message):
    referral = message.get_args()
    id = await db.add_new_user(referral=referral)
    count_users = await db.count_users()
    text = ""
    if not id:
        id = await db.get_id()
    else:
        text += "Записал в базу! "

    # channel_db.first_try(user_id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('🤖 Bot')
    # itembtn2 = types.KeyboardButton('🔍 Search')
    # itembtn3 = types.KeyboardButton('🌐 Language')
    itembtn4 = types.KeyboardButton('⚙ Settings')
    itembtn5 = types.KeyboardButton('💳 Subscription')
    itembtn2 = types.KeyboardButton('1148665047:AAGSO2XzvBIxC3Vz_sWruiMYHC3IRb7_5lQ')
    itembtn3 = types.KeyboardButton('🔸 Referral\'s')
    itembtn6 = types.KeyboardButton('🆘 Help')
    itembtn7 = types.KeyboardButton('📢 Channel')
    markup.row(itembtn1, itembtn7)
    markup.row(itembtn2, itembtn3)
    markup.row(itembtn4, itembtn5, itembtn6)

    await message.answer("Hi", reply_markup=markup)


async def check_referral(message: types.Message):
    referral = await db.check_referrals()
    text = "Ваши рефералы: {}".format(referral)
    await message.answer(text)


async def add_chanel(message: types.Message):
    channel = message.text
    await db.add_channel()