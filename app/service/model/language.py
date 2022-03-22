from sqlalchemy.orm import Session
from typing import List

from app.dto.model.language import LanguageDTO, LanguageDTOs
from app.utils.session import session_hook


class LanguageLib:

    @staticmethod
    @session_hook
    def find_by(db: Session, where: dict, get_all: bool = False):
        from app.models.language import Language

        record = db.query(Language).filter_by(**where)
        record = record.all() if get_all else record.first()

        if not record:
            return None

        return LanguageDTOs.from_orm(record).__root__ if get_all else LanguageDTO.from_orm(record)

    @staticmethod
    @session_hook
    def bulk_create(db: Session, records: [dict]):
        from sqlalchemy.exc import IntegrityError
        from app.models.language import Language

        list_to_be_updated: list = []

        for data in records:
            try:
                db.bulk_insert_mappings(Language, [data])
            except IntegrityError:
                db.rollback()
                record = LanguageLib.find_by(where={"code": data.get("code")})
                data['id'] = record.id
                list_to_be_updated.append(data)

        if list_to_be_updated:
            db.bulk_update_mappings(Language, list_to_be_updated)

        db.flush()

    @staticmethod
    @session_hook
    def update(db: Session, data: dict) -> LanguageDTO:
        from app.models.language import Language
        record = db.query(Language).filter_by(code=data.get("code")).first()

        for key, value in data.items():
            record.__setattr__(key, value)
        db.flush()
        return LanguageDTO.from_orm(record)

    @staticmethod
    @session_hook
    def get_all(db: Session) -> List[LanguageDTO]:
        from app.models.language import Language
        records = db.query(Language).all()
        return LanguageDTOs.from_orm(records).__root__
