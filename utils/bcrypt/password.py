from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashedPassword:
    @staticmethod
    def encode(password):
        return bcrypt_context.hash(password)

    @staticmethod
    def verify(entered_password, actual_password):
        return bcrypt_context.verify(entered_password, actual_password)
