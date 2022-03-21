from fastapi import APIRouter, Body

from app.dto.controller.auth import ResendVerificationCodeDTO

router = APIRouter(prefix="/api/v1/auth", tags=['Auth'])


@router.post("/resend-verification-code")
async def resend_verification_code(data: ResendVerificationCodeDTO = Body(...)):
    from app.service.model.customer import CustomerLib
    from app.config.success_response import SuccessResponse
    from fastapi import status

    # check if email exist
    code = status.HTTP_400_BAD_REQUEST
    customer = CustomerLib.find_by(where={"email": data.email})
    if not customer:
        message: str = "Customer with this email doesn't Exist, Try signing up"
        return SuccessResponse(data=None).set_message(message).set_status_code(code).response()

    # check if customer is verified
    if customer.is_verified:
        message: str = "user is already verified"
        return SuccessResponse(data=None).set_message(message).set_status_code(code).response()

    from app.service.model.verification import VerificationLib
    from app.service.email import EmailLib
    from app.utils.utils import Utils

    code: str = Utils.generate_code()
    data = {"customer_id": customer.id, "code": code}
    VerificationLib.update(data=data)

    # send email
    email_body: str = f"Use this code to verify your account: {code}"
    await EmailLib.send_emails(subject="Email Verification", recipients=customer.email, body=email_body)

    message: str = f"Code sent to {customer.email}"
    return SuccessResponse(data=None).set_message(message).response()

