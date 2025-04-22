import psycopg2
import json
import uvicorn
from fastapi import FastAPI, APIRouter
from psycopg2 import sql
router = APIRouter()
app=FastAPI()
from server import router

DB_HOST = '79.174.88.238'
DB_PORT = 15221
DB_NAME = 'school_db'
DB_USER = 'school'
DB_PASSWORD = 'School1234*'

connect = psycopg2.connect(
    dbname=DB_NAME,
    host = DB_HOST,
    port = DB_PORT,
    user = DB_USER,
    password = DB_PASSWORD
)


if __name__ == '__main__':

    migrations = ''
    with open('commands.sql') as f:
        migrations = f.read()

    with connect.cursor() as cursor:
        for st in migrations.split(';'):
            if st.strip():
                e = cursor.execute(st.strip())
                print(f"Executed: {e}")
        connect.commit()
    print('GG WP')
    app.include_router(router)
    uvicorn.run(app, host="0.0.0.0", port=8080)


