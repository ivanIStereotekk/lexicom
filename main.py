import uvicorn
from starlette import status
from fastapi import FastAPI
import redis
from pydantic import BaseModel


class Item(BaseModel):
    phone: str
    address: str



title = "LEXICOM - Тестовая работа Ивана Гончарова"
description = "Веб сервис реализованный при помощи Redis и FastAPI"

app = FastAPI(title=title, description=description)


redis_conn = redis.Redis(host='redis', port=6379, decode_responses=True)




@app.post("/write_data/", tags=["Write Data To DB"],description='Запись в базу данных')
async def write_data(item:Item):
    """Запись данных в базу данных """
    try:
        res = redis_conn.set(item.phone, item.address)
        return res
    except BaseException:
        return {"Details:": f"BAD_REQUEST {status.HTTP_400_BAD_REQUEST}"}



@app.get("/check_data", tags=["Check Data From DB "],description='Ивлечение из базы данных')
async def retrieve_data(phone: str):
    """Извлечение данных из базы по ключу phone"""
    try:
        res = redis_conn.get(phone)
    except BaseException:
        return {"Details:": f"BAD_REQUEST {status.HTTP_400_BAD_REQUEST}"}
    return {"Address": res}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

