from fastapi import APIRouter, Body

from app.dto.auth.auth import SignupDTO, EmailVerificationDTO


router = APIRouter(prefix="/api/v1/auth")


@router.post('/signup')
async def signup(data: SignupDTO = Body(...)):
    from app.service.model.customer import CustomerLib
    from fastapi.encoders import jsonable_encoder
    from app.config.success_response import SuccessResponse, CustomException
    from app.logs import logger
    from app.service.email import EmailLib

    # check email exist
    customer = CustomerLib.find_by(where={"email": data.email})
    if customer:
        from fastapi import status

        return CustomException(error="email Already Exist", status_code=status.HTTP_400_BAD_REQUEST)

    # create user account (includes password hashing)
    new_customer = CustomerLib.create(data=jsonable_encoder(data))

    # send email
    await EmailLib.send_emails(new_customer)

    logger.info("new customer created")
    return SuccessResponse(data=new_customer).set_message("account created").response()
