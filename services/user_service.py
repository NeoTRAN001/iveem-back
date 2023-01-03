from bcrypt import hashpw, gensalt, checkpw
from models.user_model import UserModel
from schemas.user_account_register_schema import UserAccountRegisterSchema
from schemas.user_account_schema import UserAccountSchema


class UserService:
    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        return self.db.query(UserModel).all()

    def get_user_by_email_or_username(self, email: str, username: str):
        return self.db.query(UserModel).filter(
            (UserModel.email == email) | (UserModel.username == username)
        ).first()

    def validate_user_credentials(self, account: UserAccountSchema):
        user = self.db.query(UserModel).filter(UserModel.email == account.email).first()

        return checkpw(account.password.encode(), user.password.encode())

    def create_user(self, user: UserAccountRegisterSchema):

        try:
            new_user = UserModel(**user.dict())
            new_user.password = hashpw(user.password.encode(), gensalt())

            self.db.add(new_user)
            self.db.commit()

            return True

        except Exception:
            return False
