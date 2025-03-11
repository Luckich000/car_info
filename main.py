import psycopg2
from psycopg2 import sql

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
            cursor.execute(st.strip())
            print(f"Executed: {st.strip()}")

if __name__ == '__main__' :
    print('GG WP')
