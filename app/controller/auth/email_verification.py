from fastapi import APIRouter, Body

from app.dto.controller.auth import EmailVerificationDTO

router = APIRouter(prefix="/api/v1/auth", tags=['Auth'])


@router.post("/verify-email")
def verify_email(data: EmailVerificationDTO = Body(...)):
    from app.service.model.customer import CustomerLib
    from app.service.model.verification import VerificationLib
    from app.config.success_response import SuccessResponse, CustomException
    from fastapi import status

    # check if email exist
    customer = CustomerLib.find_by(where={"email": data.email})
    if not customer:
        return SuccessResponse(data=None).set_message("customer with this email doesn't exist") \
            .set_status_code(status.HTTP_400_BAD_REQUEST).response()

    # check verification code
    verification_info = VerificationLib.find_by(where={"code": data.code})
    if not verification_info:
        if customer.is_verified:
            return CustomException(error="user is already verified",
                                   status_code=status.HTTP_400_BAD_REQUEST)
        return SuccessResponse(data=None).set_message("invalid code").set_status_code(status.HTTP_400_BAD_REQUEST) \
            .response()

    #
    CustomerLib.set_is_verified_true(email=customer.email)
    VerificationLib.verify_code(verification_info=verification_info)

    return SuccessResponse(data=None).set_message("Account verified. Redirecting you to login in 5 second").response()

