import aiomysql
import pymysql
import time
import asyncio
from aiogram import types
import logging
from loader import bot, dp

loop = asyncio.get_event_loop()


async def query(command, fetchall):
    pool = await aiomysql.create_pool(
        host='127.0.0.1', port=3306,
        user='root', password='',
        db='channel_bot', loop=loop
    )

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            try:
                if "SELECT" in command:
                    await cur.execute(command)
                    await conn.commit()
                    if fetchall:
                        record = await cur.fetchall()
                    else:
                        record = await cur.fetchone()
                        record = record[0]
                    return record
                else:
                    await cur.execute(command)
                    await conn.commit()
            except pymysql.IntegrityError:
                pass
    pool.close()
    await pool.wait_closed()


class DBCommands:

    ADD_NEW_USER_REFERRAL = "INSERT INTO users(chat_id, username, full_name, referral) " \
                            "VALUES ('{}', '{}', '{}', '{}')"
    ADD_NEW_USER = "INSERT INTO users(chat_id, username, full_name) VALUES ('{}', '{}', '{}')"
    COUNT_USERS = "SELECT COUNT(*) FROM users"
    GET_ID = "SELECT id FROM users WHERE chat_id = {}"
    CHECK_REFERRALS = "SELECT chat_id FROM users WHERE referral=" \
                      "(SELECT id FROM users WHERE chat_id={})"
    CHECK_BALANCE = "SELECT balance FROM users WHERE chat_id = {}"
    ADD_MONEY = "UPDATE users SET balance=balance+{} WHERE chat_id = {}"

    ADD_CHANNEL = "UPDATE users SET channel={}, subs={} WHERE chat_id = {}"
    CHECK_CHANNEL = "SELECT `channel` FROM `users` WHERE `chat_id` = {}"

    async def add_new_user(self, referral=None):
        user = types.User.get_current()
        chat_id = user.id
        username = user.username
        full_name = user.full_name
        args = chat_id, username, full_name

        if referral:
            args += (int(referral),)
            command = self.ADD_NEW_USER_REFERRAL.format(*args)
        else:
            command = self.ADD_NEW_USER.format(*args)

        await query(command, None)

    async def add_channel(self, channel, subs):
        chat_id = types.User.get_current().id
        command = self.ADD_CHANNEL.format(channel, subs, chat_id)
        await query(command, None)

    async def check_channel(self):
        chat_id = types.User.get_current().id
        command = self.CHECK_CHANNEL.format(chat_id)
        # here check just ONE channel
        record = await query(command, False)
        return record

    async def count_users(self):
        command = self.COUNT_USERS
        record = await query(command, False)
        return record

    async def get_id(self):
        chat_id = types.User.get_current().id
        command = self.GET_ID.format(chat_id)
        record = await query(command, False)
        return record

    async def check_referrals(self):
        chat_id = types.User.get_current().id
        command = self.CHECK_REFERRALS.format(chat_id)
        rows = await query(command, True)
        return ", ".join([
            f"{num + 1}. " + (await bot.get_chat(user[0])).get_mention(as_html=True)
            for num, user in enumerate(rows)
        ])

    async def check_balance(self):
        chat_id = types.User.get_current().id
        command = self.CHECK_BALANCE.format(chat_id)
        record = await query(command, False)
        return record


if __name__ == '__main__':
    loop.run_until_complete(create_connection())
