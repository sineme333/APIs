from pydantic import BaseModel
class a(BaseModel):
    name : str
    age : int
s = a(name="saeed", age=35)
print(s)