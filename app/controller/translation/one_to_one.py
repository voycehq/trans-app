from fastapi import APIRouter, Depends, Body

from app.config.authorization import Authorization
from app.dto.controller.translation import OneToOneDTO

router = APIRouter(dependencies=[Depends(Authorization.authenticate)], tags=["Translator"])


@router.post('/api/v1/translation/one-to-one')
def one_to_one_translation(data: OneToOneDTO = Body(...)):
    from fastapi import status
    from app.service.model.text import TextLib
    from app.dto.model.customer import CustomerDTO
    from app.service.model.language import LanguageLib
    from app.service.model.workspace import WorkspaceLib
    from app.engineering.translator import Translator
    from app.config.success_response import SuccessResponse

    # check if workspace id exist
    workspace = WorkspaceLib.find_by(where={"id": data.workspace_id}, get_all=False)
    if not workspace:
        return SuccessResponse(data=None).set_message("workspace_id is invalid").set_status_code(
            status.HTTP_400_BAD_REQUEST).response()

    # check if language id exist
    raw_text_language = LanguageLib.find_by(where={"id": data.raw_text_language_id}, get_all=False)
    if not raw_text_language:
        return SuccessResponse(data=None).set_message("Source text id is invalid").set_status_code(status.HTTP_400_BAD_REQUEST).response()

    translation_text_language = LanguageLib.find_by(where={"id": data.translation_text_language_id}, get_all=False)
    if not translation_text_language:
        return SuccessResponse(data=None).set_message("Destination text id is invalid").set_status_code(status.HTTP_400_BAD_REQUEST).response()

    customer: CustomerDTO = Authorization.get_customer()

    # save data to db
    text_data: dict = {
        "language_id": raw_text_language.id,
        "title": "Example",
        "body": data.raw_text,
        "customer_id": customer.id,
        "workspace": data.workspace_id,
    }
    text_record = TextLib.create(data=text_data)
    translation = Translator(text_record.id, [translation_text_language.id]).translate()

    return SuccessResponse(data=translation).response()
