from fastapi import APIRouter

from ECommerceAPI.models.post import Comment, UserPost,UserPostIn

router=APIRouter()
post_table={}


@router.post("/",response_model=UserPost)
async def create_post(post:UserPostIn):  # noqa: F821
    post=post.model_dump()
    last_record_id=len(post_table)
    new_post={**post,"id":last_record_id}
    post_table[last_record_id]=new_post
    return new_post


@router.get("/post/{post_id}/comment",response_model=list[Comment])