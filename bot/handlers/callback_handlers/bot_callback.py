from aiogram import types
from aiogram.dispatcher import FSMContext
from date_base import bot_db
from states.token import UserToken


async def bot(callback_query: types.CallbackQuery, state: FSMContext):
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

    await state.finish()

