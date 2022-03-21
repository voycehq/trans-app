from sqlalchemy.orm import Session

from app.dto.model.language import LanguageDTO, LanguageDTOs
from app.models.language import Language
from app.utils.session import session_hook


class LanguageLib:

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
    def bulk_create(db: Session, records: [dict]):
        from sqlalchemy.exc import IntegrityError
        list_to_be_updated: list = []

        for data in records:
            try:
                db.bulk_insert_mappings(Language, [data])
            except IntegrityError:
                db.rollback()
                record = LanguageLib.find_by(where={"code": data.get("code")})
                list_to_be_updated.append(record)

        if list_to_be_updated:
            db.bulk_update_mappings(Language, list_to_be_updated)

        db.flush()
