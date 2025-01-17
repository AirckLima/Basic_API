from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(pwd_context: CryptContext, plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)