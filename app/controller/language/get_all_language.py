from fastapi import APIRouter, Depends

from app.config.authorization import Authorization

router = APIRouter(tags=["Language"])


@router.get('/api/v1/language/get-all-language')
def get_all_languages():
    from app.service.model.language import LanguageLib
    from app.config.success_response import SuccessResponse

    # check default language if exist
    languages = LanguageLib.get_all()

    return SuccessResponse(data=languages).response()
