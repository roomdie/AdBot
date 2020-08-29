from aiogram import types
from aiogram.dispatcher import FSMContext
from datebase import bot_db
from states.token import UserToken, ChannelId
from bot.handlers.message_handler.categories import markup

db = bot_db.DBCommands()

async def func(callback):
    await db.add_channel()


async def callback_handler(callback_query: types.CallbackQuery, state: FSMContext):

    if callback_query.data == "add_channel":

        # await callback_query.message.answer(
        #     "Please change your category:  [<b>1</b> / <b>5</b>]",
        #     reply_markup=markup(1)
        # )
        await callback_query.message.answer(
            "Please write your channel id:"
        )

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
