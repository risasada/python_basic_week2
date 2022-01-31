import os

from dotenv import load_dotenv

import psycopg2

load_dotenv()

def init_db(url):
    dsh = os.enviroment.get(DATABASE_URL)