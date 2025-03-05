from fastapi import APIRouter
from fastapi import Depends, status
from .. import schemas, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog

router = APIRouter(tags=["blogs"], prefix="/blog")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user= Depends(oauth2.get_current_user)):
    return blog.create_blog(request, db)

@router.get("/", response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(get_db), current_user= Depends(oauth2.get_current_user)):
    blogs = blog.get_all(db)
    return blogs

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog(id, db: Session = Depends(get_db), current_user= Depends(oauth2.get_current_user)):
    return blog.get_by_id(id, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user= Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user= Depends(oauth2.get_current_user)):
    return blog.update_blog(id, request, db)
