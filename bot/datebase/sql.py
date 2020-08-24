import asyncio
import asyncpg
import logging

from config import host, pg_user, pg_pass

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def create_db():
    create_db_command = open("create_db.sql", "r").read()
    logging.info("Connecting to DB.")
    conn: asyncpg.Connection = await asyncpg.connect(
        user=pg_user,
        password=pg_pass,
        host=host

    )
    await conn.execute(create_db_command)
    logging.info("Table has been created.")
    await conn.close()


async def create_pool():
    return await asyncpg.create_pool(
        user=pg_user,
        password=pg_pass,
        host=host
    )

if __name__ == '__main__':
    # asyncio.run(create_db())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
