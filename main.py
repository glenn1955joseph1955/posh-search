from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse
import pymysql
import pymysql.cursors
from config import host, user, password, db_name

app = FastAPI()

@app.get("/")
def new():
    return RedirectResponse("https://poshmark.com/dasdasd")


@app.get("/order/{itemid}")
def old(itemid: int):
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
)
    with connection.cursor() as cursor:
        sqlite_select_query = f"""SELECT * from allbase where id = {itemid}"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
    connection.close()
    if len(records) > 0:
        return RedirectResponse(records[0]['link'])
    else:
        return RedirectResponse("https://poshmark.com/dasdasd")

