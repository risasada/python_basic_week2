import os

from dotenv import load_dotenv

import psycopg2

load_dotenv()


def init_db():
    dsh = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsh)
    cur = conn.cursor()
    sql = """CREATE TABLE users1 (
            name text,
            age integer
        );"""
    cur.execute(sql)
    conn.commit()
    conn.close()


def register_user(names, ages):
    dsh = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(dsh)
    cur = conn.cursor()
    sql = f"INSERT INTO users1 (name, age) VALUES ('{names}', {ages})"
    cur.execute(sql)
    conn.commit()
    conn.close()


def list_all():
    dsh = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsh)
    cur = conn.cursor()
    sql = "SELECT * FROM users1"
    cur.execute(sql)
    user_list = cur.fetchall()
    conn.commit()
    conn.close()
    return user_list


def printer_enter():
    print('===== Welcome to CRM Application =====')
    print('[S]how: Show all users info')
    print('[A]dd: Add new user')
    print('[Q]uit: Quit The Application')
    print('======================================')
    print()
    print()


def main():
    printer_enter()
    choices_fun = input('Your command > ')
    user_list = list_all()
    while True:
        if choices_fun == 's' or choices_fun ='S':
            for i in range(len(user_list)):


    user_list = list_all()
    print(user_list[0][0])


if __name__ == '__main__':
        main()




