
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title":"title of post 1", "content": "content of post 1", "id": 1}, {"title": "favourite food", "content": "i like pizza", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"]== id:
            return p


@app.get('/')
def root():
    return{"Hello": "Welcome to my API"}

@app.get('/posts')
def get_posts():
    return{"data": my_posts} # getting posts from the array (retrieving)

@app.post('/posts')
def create_posts(post: Post):
#def create_posts(payload: dict = Body(...)):# extracting post request 1st extraction
    #print(new_post.published) this is for published
  #  print(new_post.rating) #if you try "hello" its validate and gives an error
   # print(post)
   # print(post.dict()) #converting your pydentic model to a dictionary
   post_dict = post.model_dump()
   post_dict['id'] = randrange(0, 10000000)
   my_posts.append(post_dict)
   return {"data": post_dict}
    #return {"new_post": f"title: {payload['title']} content: {payload['content']}"} 1st  extraction

# retrieving individual post
@app.get('/posts/{id}')
def get_post(id: int):
    post = find_post(id)
    print(post)
    return{"post_detail": post}

# 1hr : 50 mins


