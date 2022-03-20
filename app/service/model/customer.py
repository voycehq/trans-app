class CustomerLib:
    from app.utils.session import session_hook
    from sqlalchemy.orm import Session
    from app.dto.model.customer import CustomerDTO

    @staticmethod
    @session_hook
    def find_by(db: Session, where: dict, get_all: bool = False):
        from app.dto.model.customer import CustomerDTOs, CustomerDTO
        from app.models.customer import Customer

        record = db.query(Customer).filter_by(**where)
        record = record.all() if get_all else record.first()

        if not record:
            return None

        return CustomerDTOs.from_orm(record).__root__ if get_all else CustomerDTO.from_orm(record)

    @staticmethod
    @session_hook
    def signup_user(db: Session, data: dict):
        from app.models.customer import Customer
        from app.service.model.date import DateLib
        from app.dto.model.customer import CustomerDTO

        new_customer = Customer(**data)

        # hash password
        new_customer.password = CustomerLib.hash_string(data.get("password"))

        # get date_id
        date_ = DateLib.get_current_day_from_record()
        new_customer.date_id = date_.id

        # write to database
        db.add(new_customer)
        db.flush()

        return CustomerDTO.from_orm(new_customer)

    @staticmethod
    @session_hook
    def set_is_verified_true(db: Session, email: str):
        from app.models.customer import Customer

        customer = db.query(Customer).filter_by(email=email).first()
        customer.is_verified = True

        db.flush()

        return customer

    @staticmethod
    def hash_string(string: str):
        from passlib.context import CryptContext

        context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return context.hash(string)

    @staticmethod
    def verify_password(password: str, hashed_password: str):
        from passlib.context import CryptContext

        context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        return context.verify(password, hashed_password)

    @staticmethod
    async def send_emails(customer: CustomerDTO):
        from fastapi_mail import MessageSchema
        from app.utils.mail_configurations import conf
        from fastapi_mail import FastMail
        from app.service.model.verification import VerificationLib

        code = CustomerLib.generate_code()

        body = f"To verify your email use the code: {code}"

        # create and send email verification email
        message = MessageSchema(
            subject="testing",
            recipients=[customer.email],
            body=body
        )

        fm = FastMail(conf)
        await fm.send_message(message)

        # Save verification credentials
        data = {
            "customer_id": customer.id,
            "code": code,
            "verification_type": "EmailVerification"
        }
        verification = VerificationLib.create_verification(data=data)

        return verification

    @staticmethod
    def generate_code():
        import string
        import random

        chars = string.ascii_letters + string.digits

        first_f = ''.join(random.choice(chars) for _ in range(4))
        sec_f = ''.join(random.choice(chars) for _ in range(4))

        return first_f + "-" + sec_f
