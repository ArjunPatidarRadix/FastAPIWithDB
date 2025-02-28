'''
Reference: 
FastAPI:           https://fastapi.tiangolo.com/tutorial/first-steps/
Youtube Tutorial:  https://www.youtube.com/watch?v=7t2alSnE2-I&t=2s
'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}