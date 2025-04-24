from fastapi import APIRouter
from pydantic import BaseModel
from random import randint
import psycopg2
from psycopg2 import sql
router = APIRouter()

DB_HOST = '79.174.88.238'
DB_PORT = 15221
DB_NAME = 'school_db'
DB_USER = 'school'
DB_PASSWORD = 'School1234*'

conn = psycopg2.connect(
    dbname=DB_NAME,
    host = DB_HOST,
    port = DB_PORT,
    user = DB_USER,
    password = DB_PASSWORD
)


class Accidents(BaseModel):
    accident_date: str
    description: str

class Cars(BaseModel):
    model: str
    car_year: int
    color: str
    car_number: str
    car_type : str


@router.post("/car/create")
async def add_car(car: Cars):
    cur = conn.cursor()
    id = randint(1,99999999)
    cur.execute(
        'INSERT INTO rakultcev_vagel.car VALUES (%s, %s, %s, %s, %s, %s)',
        (id,car.model, car.car_year,car.color,car.car_number,car.car_type))
    conn.commit()
    text = "ДОБАВЛЕНО. ваш id - {id}"
    itog = text.format(id = id)
    return itog

@router.post("/accident/add/{id}")
async def add_accident(id, acci:Accidents):
    cur = conn.cursor()
    accident_id = randint(1,9999999)
    cur.execute(
        'INSERT INTO rakultcev_vagel.accident VALUES (%s, %s, %s, %s)',
        (accident_id, id, acci.accident_date, acci.description))
    conn.commit()
    return "ДОБАВЛЕНО"

@router.delete("/car/delete/{id}")
async  def delete_car(id):
    cur = conn.cursor()
    cur.execute(
        'DELETE FROM rakultcev_vagel.car WHERE car_id = %s',
        (id,))
    conn.commit()
    return "УДАЛЕНО"

@router.get("/car/{id}")
async def get_car(id):
    cur = conn.cursor()
    cur.execute(
        'SELECT * from rakultcev_vagel.car WHERE car_id = %s',
        (id,))
    itog1 = cur.fetchall()
    cur.execute(
        'SELECT * from rakultcev_vagel.accident WHERE car_id = %s',
        (id,))
    itog2 = cur.fetchall()
    return itog1 + itog2
