from fastapi import FastAPI
from models import Product


app = FastAPI()
@app.get("/")
def welcome():
    return "Hi welcome to fastapi"

products = [Product(id=1,name="phone",price="9999"),Product(id=2,name="laptop",price="55999")]


@app.get("/viewp{id}")
def get_all_products(id:int):
    for i in products:
        if i.id == id:
            return i
    return "You got scammed"


@app.post("/product")
def add_products(p:Product):
    products.append(p)
    return p


