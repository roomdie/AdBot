from loader import bot, storage
from aiogram import executor
from config import admin_id


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


async def on_startup(dp):
    await bot.send_message(admin_id, "Я запущен!")

if __name__ == '__main__':
    from handlers.main import dp
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)

