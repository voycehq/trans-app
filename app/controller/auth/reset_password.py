from fastapi import APIRouter, Body

from app.dto.controller.auth import ResetPasswordDTO

router = APIRouter(prefix="/api/v1/auth", tags=['Auth'])


@router.post("/reset-password")
async def forgot_code(data: ResetPasswordDTO = Body(...)):
    from app.service.model.customer import CustomerLib
    from app.config.success_response import SuccessResponse
    from fastapi import status

    # check if email exist
    code = status.HTTP_400_BAD_REQUEST
    customer = CustomerLib.find_by(where={"email": data.email})
    if not customer:
        message: str = "Customer with this email doesn't exist"
        return SuccessResponse(data=None).set_message(message).set_status_code(code).response()

    from app.service.model.verification import VerificationLib

    # check verification code
    verification_type: str = "ForgotPassword"
    verification_info = VerificationLib.find_by(where={"customer_id": customer.id, "verification_type": verification_type, "code": data.code})

    if not verification_info:
        return SuccessResponse(data=None).set_message("Invalid code").set_status_code(code).response()

    from app.utils.utils import Utils
    from app.service.model.customer import CustomerLib

    # update customer account
    hash_password: str = Utils.hash_string(data.password)
    update: dict = {"password": hash_password, "email": customer.email}
    CustomerLib.update(data=update)

    message: str = f"Password changed!. Redirecting you to login in 5 second"
    return SuccessResponse(data=None).set_message(message).response()
