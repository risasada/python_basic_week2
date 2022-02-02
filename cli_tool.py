import os

from dotenv import load_dotenv

import psycopg2

load_dotenv()


def delete_one(name):
    dsh = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsh)
    cur = conn.cursor()
    sql = f"DELETE  FROM users1 WHERE name = '{name}'"
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


def search_name(name):
    dsh = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(dsh)
    cur = conn.cursor()
    sql = f"SELECT * FROM users1 WHERE name LIKE '{name}'"
    cur.execute(sql)
    search_result = cur.fetchall()
    conn.commit()
    conn.close()
    return search_result


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


def update_users(b_name, af_name, af_age):
    dsh = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsh)
    cur = conn.cursor()
    sql = f"UPDATE users1 SET name = '{af_name}', age = {af_age} WHERE name = '{b_name}'"
    cur.execute(sql)
    conn.commit()
    conn.close()


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
    while True:
        user_list = list_all()
        choices_fun = input('Your command > ')

        if choices_fun == 's' or choices_fun == 'S':
            for i in range(len(user_list)):
                print(f'NAME: {user_list[i][0]}  AGE: {user_list[i][1]}')
        elif choices_fun == 'A' or choices_fun == 'a':
            new_name = input('New user name > ')
            new_age = input('New user age > ')
            for count in range(len(user_list)):
                if user_list[count][0] == new_name:
                    print(f"Duplicated user name {new_name}")
                    break
                else:
                    continue
            if len(new_name) > 20:
                print("User name is too long(maximum is 20 characters)")
                pass

            elif len(new_name) == 0:
                print("User name can't be blank")
                pass
            elif 0 > int(new_age):
                print("age can/'t be blank")
                pass
            elif int(new_age) > 120:
                print('Age is grater than 120')
                pass
            elif isinstance(new_age, float):
                print('Age is not positive integer')
                pass
            else:
                register_user(new_name, new_age)
        elif choices_fun == 'q' or choices_fun == 'Q':
            print('bye!')
            break
        elif choices_fun == 'f' or choices_fun == 'F':
            s_name = input('User name >')
            result = search_name(s_name)
            for p in range(len(result)):
                print(f'NAME: {result[p][0]}  AGE: {result[p][1]}')
        elif choices_fun == 'D' or choices_fun == 'd':
            dn = input('User name > ')
            delete_one(dn)
        elif choices_fun == 'E' or choices_fun == 'e':
            b_name = input('User name >')
            bf_info = search_name(b_name)
            af_name = input(f'New user name({bf_info[0][0]}) >')
            af_age = input(f'New user name({bf_info[0][1]}) >')
            update_users(b_name, af_name, af_age)

        else:
            print(f"{choices_fun}: command not found")


if __name__ == '__main__':

    main()
#ksksksksksk




