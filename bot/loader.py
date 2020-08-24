import logging
import aiohttp
import pymysql
import config

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config.token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(
    level=logging.INFO,
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s'
)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())