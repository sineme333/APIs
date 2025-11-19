from fastapi import FastAPI
from pydantic import BaseModel
a = FastAPI
class d(BaseModel):
@a.get("/Hello_world")
def s():
    return{"make me happy": "i`m happy now"}