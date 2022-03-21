class Utils:

    @staticmethod
    def generate_code():
        import string
        import random

        chars = string.ascii_letters + string.digits

        first_f = ''.join(random.choice(chars) for _ in range(4))
        sec_f = ''.join(random.choice(chars) for _ in range(4))

        return first_f + "-" + sec_f

    @staticmethod
    def hash_string(string: str):
        from passlib.context import CryptContext

        context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return context.hash(string)

    @staticmethod
    def verify_hash(password: str, hashed_password: str):
        from passlib.context import CryptContext

        context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        return context.verify(password, hashed_password)


