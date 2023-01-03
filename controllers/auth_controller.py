from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas.jwt_schema import JWTSchema
from schemas.user_account_schema import UserAccountSchema
from schemas.user_account_register_schema import UserAccountRegisterSchema

from utils.jwt_handler import create_token

router = APIRouter()


@router.post(
    '/sign-in',
    tags=['auth'],
    status_code=status.HTTP_200_OK,
    response_model=JWTSchema,
    summary="Login for users (Email, Password)",
    description="This path receives a UserAccount object with the email and password, if everything is correct it returns a JWT token."
)
def sign_in(account: UserAccountSchema = Body(...)):
    jwt_schema = JWTSchema(token=create_token(account.dict()))

    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(jwt_schema))


@router.post(
    '/sign-up',
    tags=['auth'],
    status_code=status.HTTP_200_OK,
    response_model=JWTSchema,
    summary="Sign Up for users (Email, Password)",
    description="This path receives a UserAccountRegister object with the user's account data, if everything is correct it returns a JWT token."
)
def sign_up(account: UserAccountRegisterSchema = Body(...)):
    jwt_schema = JWTSchema(token=create_token(account.dict()))

    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(jwt_schema))
