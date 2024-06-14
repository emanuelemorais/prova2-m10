from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List
import logging

app = FastAPI()

logger = logging.getLogger(__name__)
logging.basicConfig(filename='systemlog.log', encoding='utf-8', level=logging.WARNING)

class BlogPost(BaseModel):
    id: int
    title: str
    content: str

blog_posts: List[BlogPost] = []

@app.post("/blog", status_code=201)
async def create_blog_post(post: BlogPost):
    try:
        blog_posts.append(post)
        logging.info('create_blog_post: Post created successfully!') 
        return {"status": "success"}
    except KeyError:
        logging.error('create_blog_post: Invalid request')
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception as e:
        logging.error('create_blog_post: '+ str(e))
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/blog", response_model=List[BlogPost])
async def get_blog_posts():
    logging.info('get_blog_posts: Post created successfully!') 
    if len(blog_posts) == 0:
        logging.warning('get_blog_posts: No posts found')
        raise HTTPException(detail="No posts found")
    logging.info('get_blog_posts: Successfully get posts!') 
    return blog_posts

@app.get("/blog/{id}", response_model=BlogPost)
async def get_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            logging.info('get_blog_post: Post found: '+ str(post))
            return post
    logging.warning('get_blog_post: Post not found')
    raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/blog/{id}", status_code=200)
async def delete_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            logging.info('delete_blog_post: Post deleted successfully: '+ str(post))
            return {"status": "success"}
    logging.warning('delete_blog_post: Post not found')
    raise HTTPException(status_code=404, detail="Post not found")

@app.put("/blog/{id}", status_code=200)
async def update_blog_post(id: int, updated_post: BlogPost):
    for post in blog_posts:
        if post.id == id:
            post.title = updated_post.title
            post.content = updated_post.content
            logging.info('update_blog_post: Post updated successfully: '+ str(post))
            return {"status": "success"}
    logging.warning('update_blog_post: Post not found')
    raise HTTPException(status_code=404, detail="Post not found")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")