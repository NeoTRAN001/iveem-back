from fastapi import APIRouter, status, Body, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session

from schemas.jwt_schema import JWTSchema
from schemas.user_account_schema import UserAccountSchema
from schemas.user_account_register_schema import UserAccountRegisterSchema
from schemas.user_jwt_schema import UserJWTSchema

from services.user_service import UserService

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
    user = UserService(Session()).validate_user_credentials(account)

    if not user:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "The email or the password are incorrect"})

    jwt_schema = JWTSchema(token=create_token({'email': user.email, 'rol': user.rol}))

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

    user_service = UserService(Session())
    account.rol = "user"

    if user_service.get_user_by_email_or_username(account.email, account.username):
        return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"message": "Email or Username already exists"})

    if not user_service.create_user(account):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to register account")

    user_jwt: UserJWTSchema = UserJWTSchema(username=account.username, rol=account.rol)
    jwt_schema = JWTSchema(token=create_token(user_jwt.dict()))

    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(jwt_schema))
