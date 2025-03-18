import psycopg2
import json
from psycopg2 import sql

def load(id):
    e = cursor.execute('SELECT * from rakultcev_vagel.car WHERE car_id = %s',(id,))
    print(cursor.fetchall())
    # print(type(cursor.fetchall()))
    # itog = json.dumps(cursor.fetchall()) ------не удавшийся эксперимент
    # print(itog)

def save(id,model,year,color,number,type ):
    cursor.execute('INSERT INTO rakultcev_vagel.car VALUES (%s, %s, %s, %s, %s, %s)', (id,model, year,color,number,type))
    conn.commit()

def delete(id):
    cursor.execute('DELETE FROM rakultcev_vagel.car WHERE car_id = %s',(id,))
    conn.commit()


host = '79.174.88.238'
port = 15221
db_name = 'school_db'
user = 'school'
password = 'School1234*'


conn = psycopg2.connect(
    dbname=db_name,
    host=host,
    port=port,
    user=user,
    password=password
)

migrations = ''
with open('commands.sql') as f:
    migrations = f.read()

with conn.cursor() as cursor:
    for st in migrations.split(';'):
        if st.strip():
            e = cursor.execute(st.strip())
            print(f"Executed: {e}")
    conn.commit()

    a = input("что вы хотите сделать? delete(удалить) load(показать информацию) save(сохранить информацию)")
    if a == "delete":
        delete(input("укажите id машины, которую хотите удалить:"))
    else:
        if a == "load":
            load(input("Укажите id машины:"))

        else:
            if a == "save":
                save(input("id , модель, год, цвет, номер машины, тип машины:" ), input(), input(),input(),input(),input())

    # если что-то пойдет не так:
    # load(input())
    # delete(input())
    # save(input(),input(),input(),input(),input(),input())



if __name__ == '__main__' :
    print('GG WP')
