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
        return self.db.query(UserModel).filter(
            (UserModel.email == account.email) & (UserModel.password == account.password)
        ).first()

    def create_user(self, user: UserAccountRegisterSchema):
        try:
            new_movie = UserModel(**user.dict())

            self.db.add(new_movie)
            self.db.commit()

            return True

        except Exception:
            return False
