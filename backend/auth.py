from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

router = APIRouter()

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)

SECRET_KEY = "fraud_detection_secret_key_2026"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


@router.post("/login")
def login(user: dict):

    username = user.get("username")
    password = user.get("password")

    if (
        username == "admin"
        and password == "admin123"
    ):

        token = create_access_token(
            {"sub": username}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )