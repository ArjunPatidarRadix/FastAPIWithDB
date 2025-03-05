from fastapi import FastAPI
from . import  models
from .database import engine
from .routers import authentication, blog, user

app = FastAPI()


models.Base.metadata.create_all(engine)



@app.get("/")   
def welcome():
    return {"Hello": "World"}

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
# Compare this snippet from blog/routers/blog.py:

