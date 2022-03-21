from fastapi import APIRouter, Body
from app.dto.controller.auth import LoginDTO

router = APIRouter(prefix="/api/v1/auth", tags=['Auth'])


@router.post("/login")
async def login(data: LoginDTO = Body(...)):
    from app.utils.utils import Utils
    from app.service.model.customer import CustomerLib
    from app.config.success_response import CustomException
    from fastapi import status
    from app.logs import logger

    # Get user by email
    where: dict = {"email": data.email}
    customer = CustomerLib.find_by(where=where, get_all=False)
    if not customer or Utils.verify_hash(data.password, customer.password) is False:
        error: str = "Invalid user credentials"
        return CustomException(status_code=status.HTTP_400_BAD_REQUEST, error=error)

    # check if user is verified
    if not customer.is_verified:
        from app.service.model.verification import VerificationLib
        from app.service.email import EmailLib

        code: str = Utils.generate_code()
        data = {"customer_id": customer.id, "code": code}
        VerificationLib.update(data=data)

        # send email
        email_body: str = f"Use this code to verify your account: {code}"
        await EmailLib.send_emails(subject="Email Verification", recipients=customer.email, body=email_body)

        error: str = "Account not verified"
        logger.log(f"{customer.email} not verified")
        return CustomException(status_code=status.HTTP_403_FORBIDDEN, error=error)

    # Generate api-key
    api_key: str = Utils.generate_api_key()
    customer = CustomerLib.update(data={"email": data.email, "api_key": api_key})
    from app.config.success_response import SuccessResponse
    return SuccessResponse(data=customer).set_message("Login successful").response()
