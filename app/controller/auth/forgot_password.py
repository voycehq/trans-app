from fastapi import APIRouter, Body

from app.dto.controller.auth import ResendVerificationCodeDTO

router = APIRouter(prefix="/api/v1/auth", tags=['Auth'])


@router.post("/forgot-password")
async def forgot_code(data: ResendVerificationCodeDTO = Body(...)):
    from app.service.model.customer import CustomerLib
    from app.config.success_response import SuccessResponse
    from fastapi import status

    # check if email exist
    code = status.HTTP_400_BAD_REQUEST
    customer = CustomerLib.find_by(where={"email": data.email})
    if not customer:
        message: str = "Customer with this email doesn't Exist"
        return SuccessResponse(data=None).set_message(message).set_status_code(code).response()

    from app.service.model.verification import VerificationLib
    from app.service.email import EmailLib
    from app.utils.utils import Utils

    # check verification code
    code: str = Utils.generate_code()
    verification_type: str = "ForgotPassword"
    verification_info = VerificationLib.find_by(where={"customer_id": customer.id, "verification_type": verification_type})

    data = {"customer_id": customer.id, "code": code, "verification_type": verification_type}
    if not verification_info:
        VerificationLib.create(data=data)
    else:
        VerificationLib.update(data=data)

    # send email
    email_body: str = f"Use this code to reset your account password: {code}"
    await EmailLib.send_emails(subject="Email Verification", recipients=customer.email, body=email_body)

    message: str = f"Password reset code sent to {customer.email}"
    return SuccessResponse(data=None).set_message(message).response()