class EmailLib:
    from typing import List, Any

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

    # noinspection PyBroadException
    @staticmethod
    async def send_emails(subject: str, recipients: str, body: Any):
        from fastapi_mail import MessageSchema
        from fastapi_mail import FastMail

        message = MessageSchema(
            subject=subject,
            recipients=[recipients],
            body=body
        )

        fm = FastMail(EmailLib.conf)
        from app.logs import logger
        try:
            await fm.send_message(message)
            logger.error(f'Successfully sent email to {recipients}')
        except Exception:
            logger.error(f'Failed sending email to {recipients}')
