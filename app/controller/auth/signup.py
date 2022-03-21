from fastapi import APIRouter, Body

from app.dto.controller.auth import SignupDTO


router = APIRouter(prefix="/api/v1/auth", tags=['Auth'])


@router.post('/signup')
async def signup(data: SignupDTO = Body(...)):
    from app.service.model.customer import CustomerLib
    from fastapi.encoders import jsonable_encoder
    from app.config.success_response import SuccessResponse, CustomException
    from app.logs import logger
    from app.service.email import EmailLib
    from app.service.model.verification import VerificationLib
    from app.utils.utils import Utils

    # check email exist
    customer = CustomerLib.find_by(where={"email": data.email})
    if customer:
        from fastapi import status

        return CustomException(error="Email already exist", status_code=status.HTTP_400_BAD_REQUEST)

    # create user account (includes password hashing)
    new_customer = CustomerLib.create(data=jsonable_encoder(data))
    code: str = Utils.generate_code()

    # Save verification credentials
    data = {"customer_id": new_customer.id, "code": code, "verification_type": "EmailVerification"}
    VerificationLib.create_verification(data=data)

    # send email
    email_body: str = f"Use this code to verify your account: {code}"
    await EmailLib.send_emails(subject="Email Verification", recipients=new_customer.email, body=email_body)

    logger.info("new customer created")
    return SuccessResponse(data=new_customer).set_message("account created").response()
