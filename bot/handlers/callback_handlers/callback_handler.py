from aiogram import types
from aiogram.dispatcher import FSMContext
from datebase import bot_db
from states.token import UserToken
from bot.handlers.message_handler.categories import markup


async def callback_handler(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    username_user = callback_query.from_user.username
    row = bot_db.select_row(user_id)
    # user bot
    username_bot = row[3]
    date_time = row[4]

    user_id = callback_query.from_user.id
    username_user = callback_query.from_user.username
    row = bot_db.select_row(user_id)
    # user bot
    username_bot = row[3]
    date_time = row[4]

    if callback_query.data == "add_bot":
        await callback_query.message.answer(
            "Please write your token of the Bot (created by @BotFather):"
        )
        await callback_query.answer(text="")
        await UserToken.token.set()
    elif callback_query.data == "delete_bot":
        rows = bot_db.select_all()
        # print(rows)
        for i in rows:
            if username_bot in i:
                markup_delete = types.InlineKeyboardMarkup()
                button_yes = types.InlineKeyboardButton(text="Yes", callback_data="yes_delete_bot")
                button_no = types.InlineKeyboardButton(text="No", callback_data="about_bot")
                markup_delete.insert(button_yes)
                markup_delete.insert(button_no)
                await callback_query.message.edit_text(
                    "Delete your Bot?", reply_markup=markup_delete
                )
                await callback_query.answer(text="")
                break

    elif callback_query.data == "yes_delete_bot":
        bot_db.delete_bot(user_id, username_user, username_bot)
        await callback_query.message.answer(
            "Bot deleted."
        )
        await callback_query.answer(text="")
        await state.finish()

    elif callback_query.data == "about_bot":
        markup_about = types.InlineKeyboardMarkup()
        delete_button = types.InlineKeyboardButton(text="Delete the Bot", callback_data="delete_bot")
        back_button = types.InlineKeyboardButton(text="←", callback_data="bot")
        markup_about.insert(back_button)
        markup_about.insert(delete_button)
        await callback_query.message.edit_text(
            "<b>Information</b>\n\n<i>Username:</i> @{}\n"
            "<i>Added:</i> {}".format(username_bot, date_time),
            reply_markup=markup_about, parse_mode="HTML"
        )
        await callback_query.answer(text="")
    elif callback_query.data == "bot":
        markup_bot = types.InlineKeyboardMarkup()
        button_bot = types.InlineKeyboardButton(text="@{}".format(username_bot), callback_data="about_bot")
        markup_bot.insert(button_bot)
        await callback_query.message.edit_text(
            "Your Bot", reply_markup=markup_bot
        )
        await callback_query.answer(text="")

    elif callback_query.data == "add_channel":
        await callback_query.message.answer(
            "Please change your category:  [<b>1</b> / <b>5</b>]",
            reply_markup=markup(1)
        )
        # await callback_query.message.answer(
        #     "Please write your channel id:"
        # )
        await callback_query.answer(text="")
    elif callback_query.data == "yes_delete_channel":
        delete_channel(user_id, username_user, username_bot)
        await callback_query.message.answer(
            "Channel deleted."
        )
        await callback_query.answer(text="")
        await state.finish()

    elif callback_query.data == "cancel_delete_bot":
        await callback_query.message.answer(
            "Cancel."
        )
        await callback_query.answer(text="")
        await state.finish()
    elif callback_query.data == "delete_bot":
        rows = channel_db.select_all()
        for i in rows:
            if username_bot in i:
                markup_delete = types.InlineKeyboardMarkup()
                button_yes = types.InlineKeyboardButton(text="Yes", callback_data="delete_bot_real_1")
                button_no = types.InlineKeyboardButton(text="No", callback_data="about_channel")
                markup_delete.insert(button_yes)
                markup_delete.insert(button_no)
                await callback_query.message.answer(
                    "Delete your Channel?", reply_markup=markup_delete
                )
                await callback_query.answer(text="")

    # category
    elif callback_query.data == "first_page":
        await callback_query.message.edit_text(
            "Please change your category:  [<b>1</b> / <b>5</b>]",
            reply_markup=markup(1)
        )
        await callback_query.answer(text="")
    elif callback_query.data == "second_page":
        await callback_query.message.edit_text(
            "Please change your category:  [<b>2</b> / <b>5</b>]",
            reply_markup=markup(2)
        )
        await callback_query.answer(text="")
    elif callback_query.data == "third_page":
        await callback_query.message.edit_text(
            "Please change your category:  [<b>3</b> / <b>5</b>]",
            reply_markup=markup(3), parse_mode="HTML"
        )
        await callback_query.answer(text="")
    elif callback_query.data == "fourth_page":
        await callback_query.message.edit_text(
            "Please change your category:  [<b>4</b> / <b>5</b>]",
            reply_markup=markup(4), parse_mode="HTML"
        )
        await callback_query.answer(text="")
    elif callback_query.data == "five_page":
        await callback_query.message.edit_text(
            "Please change your category:  [<b>5</b> / <b>5</b>]",
            reply_markup=markup(5)
        )
        await callback_query.answer(text="")
