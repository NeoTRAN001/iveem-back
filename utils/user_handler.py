from datetime import date

from schemas.user_profile_schema import UserProfileSchema
from schemas.user_account_register_schema import UserAccountRegisterSchema


def format_profile_by_usermodel(user):
    user_dict = {
        "email": user.email,
        "name": user.name,
        "lastname": user.lastname,
        "username": user.username,
        "birthday": user.birthday.strftime('%Y-%m-%d'),
        "picture": user.picture,
        "rol": user.rol
    }
    profile: UserProfileSchema = UserProfileSchema(**user_dict)

    return profile
