from fastapi import APIRouter, Body

from app.dto.model.customer import SignupDTO, EmailVerificationDTO

router = APIRouter(prefix="/api/v1/auth")


@router.post('/signup')
async def signup(data: SignupDTO = Body(...)):
    from app.service.model.customer import CustomerLib
    from fastapi.encoders import jsonable_encoder
    from app.config.success_response import SuccessResponse, CustomException

    # check email exist
    customer = CustomerLib.find_by(where={"email": data.email})
    if customer:
        from fastapi import status

        return CustomException(error="email Already Exist", status_code=status.HTTP_400_BAD_REQUEST)

    # create user account (includes password hashing)
    new_customer = CustomerLib.signup_user(data=jsonable_encoder(data))

    print(new_customer)

    # send email
    await CustomerLib.send_emails(new_customer)

    return SuccessResponse(data=new_customer)


@router.post("/verify-email")
def verify_email(data: EmailVerificationDTO = Body(...)):
    from app.service.model.customer import CustomerLib
    from app.service.model.verification import VerificationLib
    from app.config.success_response import SuccessResponse, CustomException
    from fastapi import status

    try:
        # check if email exist
        customer = CustomerLib.find_by(where={"email": data.email})
        if not customer:
            return CustomException(error="customer with this email doesn't Exist, Try signing up",
                                   status_code=status.HTTP_400_BAD_REQUEST)

        # check verification code
        verification_info = VerificationLib.find_by(where={"code": data.code})
        if not verification_info:
            if customer.is_verified:
                return CustomException(error="user is already verified",
                                       status_code=status.HTTP_400_BAD_REQUEST)
            return CustomException(error="invalid code", status_code=status.HTTP_400_BAD_REQUEST)

        #
        CustomerLib.set_is_verified_true(email=customer.email)
        VerificationLib.verify_code(verification_info=verification_info)

        return SuccessResponse(data={})
    except Exception as e:
        raise e
