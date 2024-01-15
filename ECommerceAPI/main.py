from fastapi import FastAPI
from pydantic import BaseModel

from ECommerceAPI.models.post import UserPost, UserPostIn





app = FastAPI()
post_table={}

@app.get("/post",response_model=UserPost)
async def get_all_posts():
    return list(post_table.values())
@app.get("/")
async def root():
    return {"message": "Hello , World"}
