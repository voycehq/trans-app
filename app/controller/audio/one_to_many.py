from fastapi import APIRouter, Depends, Body

from app.config.authorization import Authorization
from app.dto.controller.audio import OneToManyDTO

router = APIRouter(dependencies=[Depends(Authorization.authenticate)], tags=["Audio"])


@router.post('/api/v1/audio/one-to-many')
def one_to_many_in_audio(data: OneToManyDTO = Body(...)):
    from fastapi import status
    from app.service.model.text import TextLib
    from app.dto.model.customer import CustomerDTO
    from app.service.model.language import LanguageLib
    from app.service.model.workspace import WorkspaceLib
    # from app.engineering.translator import Translator
    from app.config.success_response import SuccessResponse
    from app.engineering.audio import AudioGenerator

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

    # Update text record
    text_data: dict = {
        "id": data.text_id,
        "language_id": raw_text_language.id,
        "body": data.raw_text,
        "customer_id": customer.id,
        "workspace": data.workspace_id,
    }
    text_record = TextLib.update(data=text_data)
    AudioGenerator(workspace_id=data.workspace_id, raw_text_id=data.raw_text_id)

    # translation = Translator(text_record.id, [translation_text_language.id]).translate()

    return SuccessResponse(data=translation).response()
