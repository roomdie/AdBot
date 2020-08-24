import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
admin_id = os.getenv("ADMIN_ID")
host = os.getenv("PG_HOST")
pg_user = os.getenv("PG_USER")
pg_pass = os.getenv("PG_PASS")