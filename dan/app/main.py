from typing import Optional
from fastapi import FastAPI,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
 
app = FastAPI()


class post(BaseModel):
    title:str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_post = [{"title":"title of post 1","content": "content of post 1","id":1},{"title":"favourite foods","content":"i  like pizza","id": 2}]

def get_post_for_id(id):
 for p in my_post:
  if p["id"] == id:
   return id
  
def deleteam_post(id):
   for i,p in enumerate(my_post):     
      if p["id"] == id:
         return i
   




@app.get("/")
def root():
    return {"message":"hello world"}

@app.get("/posts")
def get_post():
    return {"data":my_post}

@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post = post):
    post_dict = post.model_dump()
    post_dict["id"]=randrange(0,10000000)
    my_post.append(post_dict)
    return{"data":post_dict}

@app.get("/posts/latest")
def get_latest_post():
   post = my_post[len(my_post)+1]
   return {"detail": post}

@app.get("/posts/{id}")
def get_post(id: int):
  post = get_post_for_id(id)
  if not post:
     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,  detail = f"post with this is {id} was not found: ")
  return {f"this is the post {post} for your id"}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
  #delete post
  # find the index in the array that is required ID
  #my_post.pop(index)

  index = deleteam_post(id)
  if not index:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
     
  my_post.pop(index)
  return { "message":"post was sucessfully deleted" }


@app.put("/posts/{id}")
def update_post(id: int, post: post):
  index = deleteam_post(id)
  
  if not index:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail= f"post with id {id} does  not exist: ") 
  

  post_dict = post.dict()
  post_dict["id"]= id
  post_dict = my_post[index]
  return{"data":post_dict}

