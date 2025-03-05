'''
Reference: 
FastAPI:           https://fastapi.tiangolo.com/tutorial/first-steps/
Youtube Tutorial:  https://www.youtube.com/watch?v=7t2alSnE2-I&t=2s
'''

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "unpublished blogs"}  


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}

@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"data": {"1", "2"}} 

@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"Blog is created with title as {blog.title}"} 

# if __name__ == "__main__":
#     # insead of this command uvicorn main:app --reload 
#     # we can use this code to run the app
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=9000)


# intall modules using the requirements.txt run the below command
# pip install -r requirements.txt

# to save the all the modules in requirements.txt
# pip freeze > requirements.txt 

