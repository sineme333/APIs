# mading new server in /FastAPI address name by FastAPI

from fastapi import FastAPI
a = FastAPI()
@a.get("/address")
def s():
    return{"my first FastAPI" : "is working"}

# in last just write uvicorn x(name of folder and file without .py) :y(name of address like a in here) --reload