from sqlalchemy.orm import Session

from app.dto.model.language import LanguageDTO, LanguageDTOs
from app.models.language import Language
from app.utils.session import session_hook


class LanguageLib:

    def __init__(self):
        self.languages = [{'name': 'English', 'code': 'en', 'html_code': 'translator-lang-option-en-US'},
                          {'name': 'French', 'code': 'fr', 'html_code': 'translator-lang-option-fr-FR'},
                          {'name': 'Spanish', 'code': 'es', 'html_code': 'translator-lang-option-es-ES'}]

    def run(self):
        from app.logs import logger

        LanguageLib.create(records=self.languages)

        logger.info(f"Done Creating customer Languages")

    @staticmethod
    @session_hook
    def find_by(db: Session, where: dict, get_all: bool = False):
        record = db.query(Language).filter_by(**where)
        record = record.all() if get_all else record.first()

        if not record:
            return None

        return LanguageDTOs.from_orm(record).__root__ if get_all else LanguageDTO.from_orm(record)

    @staticmethod
    @session_hook
    def create(db: Session, records: [dict]):
        from sqlalchemy.exc import IntegrityError

        for data in records:
            try:
                db.bulk_insert_mappings(Language, [data])
            except IntegrityError:
                db.rollback()
                db.bulk_update_mappings(Language, data)

        db.flush()
