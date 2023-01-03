from fastapi import APIRouter, status, Depends, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from services.user_service import UserService

from schemas.user_profile_schema import UserProfileSchema
from utils.user_handler import format_profile_by_usermodel

router = APIRouter()


@router.get(
    '/user/{username}',
    tags=['user'],
    response_model=UserProfileSchema,
    dependencies=[Depends(JWTBearer())],
    summary="Get the user profile data by their username",
    description="This route receives a username of type str, and returns the information in a UserProfileSchema object."
)
def get_user_by_username(username: str = Path(min_length=3)):
    profile: UserProfileSchema = format_profile_by_usermodel(
        UserService(Session()).get_user_by_email_or_username("", username)
    )

    if not profile:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "User not found"})

    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(profile))
