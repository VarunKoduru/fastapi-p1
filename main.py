from fastapi import FastAPI
from models import Product


app = FastAPI()
@app.get("/")
def welcome():
    return "Hi welcome to fastapi"

products = [Product(id=1,name="phone",price=9999),Product(id=2,name="laptop",price=55999)]


@app.get("/viewp{id}")
def get_all_products(id:int):
    for i in products:
        if i.id == id:
            return i
    return "You got scammed"

@app.get("/product")
def get_all():
    return products


@app.post("/product")
def add_products(p:Product):
    products.append(p)
    return p


@app.put("/product")
def update_products(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Updated successfully"
    return "Not found"


@app.delete("/product")
def delete_product(id:int):
    for j in range(len(products)):
        if products[j].id == id:
            del products[j]
            return "product deleted"

    return "Not found"

