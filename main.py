from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def welcome():
    return "Hi welcome to fastapi"