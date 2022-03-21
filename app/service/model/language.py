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
                record = db.query(Language).filter_by(code=data.get("code")).first()
                for key, value in data.items():
                    record.__setattr__(key, value)
                list_to_be_updated.append(LanguageDTO.from_orm(record))

        if list_to_be_updated:
            db.bulk_update_mappings(Language, list_to_be_updated)

        db.flush()

    @staticmethod
    @session_hook
    def update(db: Session, data: dict) -> LanguageDTO:

        record = db.query(Language).filter_by(code=data.get("code")).first()
        for key, value in data.items():
            record.__setattr__(key, value)
        db.flush()
        return LanguageDTO.from_orm(record)
