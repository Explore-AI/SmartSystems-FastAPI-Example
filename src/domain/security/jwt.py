from passlib.context import CryptContext
from datetime import timedelta
from datetime import datetime, timedelta
from typing import Any, Dict, Optional
import jwt
from fastapi import HTTPException
from domain.schemas.identityUser import IdentityUser as User
from domain.security.password import pwd_generator
from repositories.models.identityUser import IdentityUser


class JWTGenerator:
    def __init__(self):
        self._jwt_algorithm = "HS256"
        self._jwt_secret_key = "mysecretkey"

    def create_access_token_for_user(
        self,
        user: IdentityUser,
        expires_delta: Optional[timedelta] = None,
    ) -> str:
        """
        Creates an access token for a user.
        """
        to_encode = self._get_user_data_for_token(user)
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=60)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            self._jwt_secret_key,
            algorithm=self._jwt_algorithm,
        )
        return encoded_jwt

    def _get_user_data_for_token(self, user: IdentityUser) -> Dict[str, Any]:
        """
        Generates user data to include in the JWT token.
        """
        return {
            "userId": user.Id,
            "sub": user.email,
            "name": user.username,
            "password_hash": user.PasswordHash,
            "password_salt": user.PasswordSalt,
        }

    def get_user_from_token(self, token: str) -> Optional[IdentityUser]:
        """
        Decodes the JWT token to obtain the user information and returns the user.
        """
        try:
            payload = jwt.decode(token, self._jwt_secret_key, algorithms=[self._jwt_algorithm])
            userId = payload.get('userId')
            email = payload.get("sub")
            username = payload.get("name")
            exp = payload.get("exp")
            password_hash = payload.get("password_hash"),
            password_salt = payload.get("password_salt"),
            if email is None or username is None:
                raise HTTPException(status_code=401, detail="Could not validate credentials")
            user_dict = {
                "Id": userId,
                "email": email,
                "username": username,
                "PasswordHash": password_hash,
                "PasswordSalt": password_salt,
            }
            return IdentityUser(**user_dict)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return None


def get_jwt_generator() -> JWTGenerator:
    return JWTGenerator()


jwt_generator: JWTGenerator = get_jwt_generator()