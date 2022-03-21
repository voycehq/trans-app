from app.utils.utils import Utils


class EmailLib:
    from app.dto.model.customer import CustomerDTO

    from fastapi_mail import ConnectionConfig
    from config import config

    conf = ConnectionConfig(
        MAIL_USERNAME=config.MAIL_USERNAME,
        MAIL_PASSWORD=config.MAIL_PASSWORD,
        MAIL_FROM=config.MAIL_FROM,
        MAIL_PORT=config.MAIL_PORT,
        MAIL_SERVER=config.MAIL_SERVER,
        MAIL_FROM_NAME=config.MAIL_FROM_NAME,
        MAIL_TLS=True,
        MAIL_SSL=False
    )

    @staticmethod
    async def send_emails(customer: CustomerDTO):
        from fastapi_mail import MessageSchema
        from fastapi_mail import FastMail
        from app.service.model.verification import VerificationLib

        code = Utils.generate_code()

        body = f"To verify your email use the code: {code}"

        # create and send email verification email
        message = MessageSchema(
            subject="testing",
            recipients=[customer.email],
            body=body
        )

        fm = FastMail(EmailLib.conf)
        await fm.send_message(message)

        # Save verification credentials
        data = {
            "customer_id": customer.id,
            "code": code,
            "verification_type": "EmailVerification"
        }
        verification = VerificationLib.create_verification(data=data)

        return verification
