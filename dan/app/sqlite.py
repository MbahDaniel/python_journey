from typing import Optional
from fastapi import FastAPI,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
 
app = FastAPI()


class post(BaseModel):
    Name:str
    phone_number: int
    saved: bool = True
    rating: Optional[int] = None

my_contacts = [{"name":"name of person 1","phone_number": "090876543555","id":1},{"name":" What your name","phone_number":"090878456378","id": 2}]


def get_post_for_id(id):
 number = input("Enter Your phone number")
 for i in my_contacts:
   if i["phone_number"] == number:
    return number
  

def get_contact_for_id(id):
 for i in my_contacts:
  if i["id"] == id:
   return id
  
def deleteam_post(id):
   for i,p in enumerate(my_contacts):     
      if p["id"] == id:
         return i

@app.get("/view_all_contacts")
def view_all_contacts():
   for c in my_contacts:
      return c
   
@app
   
@app.post("/new_contact", status_code = status.HTTP_201_CREATED)
def create_new_contact(post = post):
    post_dict = post.model_dump()
    post_dict["id"]=randrange(0,10000000)
    my_contacts.append(post_dict)
    return{"data":post_dict}

@app.get("/find_contact/{id}")
def get_post(id: int):
  post = get_post_for_id(id)
  if not post:
     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,  detail = f"post with this is {id} was not found: ")
  return {f"this is the contact {post} for your id"}


@app.put("/posts/{id}")
def update_post(id: int, post: post):
  index = deleteam_post(id)
  
  if not index:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail= f"post with id {id} does  not exist: ") 
  
  post_dict = post.dict()
  post_dict["id"]= id
  post_dict = my_contacts[index]
  return{"data":post_dict}
 
@app.get("/Contacts/New")
def get_latest_post():
   post = my_contacts[len(my_contacts)+1]
   return {"detail": post}

