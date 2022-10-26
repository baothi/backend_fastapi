from typing import Optional
from fastapi import APIRouter, status, Response, Depends
from enum import Enum
from router.blog_post import required_functionlity


router = APIRouter(
  prefix="/blog",
    tags=["blog"],
)

# @app.get('/blog/all')
# def get_all_blogs():
#   return {'message': 'All blogs'}


@router.get(
    '/all',
    summary='Retrive all blog',
    description='This api call simulates fetching all blog',
    response_description='The list of available blogs.'    
)
def get_all_blogs(page = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionlity)):
  return {'message': f'All {page_size} blogs on page {page}', 'req': req_parameter}

@router.get('/{id}/comments/{comment_id}', tags =['comments'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None, req_parameter: dict = Depends(required_functionlity)):
  """
  Simulates rettrieving a comment of a blog
  - **id**: mandatory path parameter
  - **comment_id**: mandatory path parameter
  - **valid**: mandatory path parameter
  - **username**: mandatory path parameter
  """
  return {'message': f'blog_id {id}, Comment {comment_id}, valid {valid} by {username} on page {id}'}


class BlogType(str,Enum):
  short= 'short'
  story= 'story'
  howto= 'howto'

@router.get('/type/{type}')
def get_blog_type(type : BlogType, req_parameter: dict = Depends(required_functionlity)):
  return {'message': f'Blog with type {type}' }

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id : int, req_parameter: dict = Depends(required_functionlity)):
  if id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': f'Blog {id} not found' }
  else:
    response.status_code = status.HTTP_200_OK
    return {'message': f'Blog with id {id}' }