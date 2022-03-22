from typing import List
from sqlalchemy.orm import Session

from app.dto.model.language_setting import LanguageSettingDTO, LanguageSettingDTOs
from app.utils.session import session_hook


class LanguageSettingLib:

    @staticmethod
    @session_hook
    def find_by(db: Session, where: dict, get_all: bool = False):
        from app.models.language_setting import LanguageSetting

        record = db.query(LanguageSetting).filter_by(**where)
        record = record.all() if get_all else record.first()

        if not record:
            return None if not get_all else []

        return LanguageSettingDTOs.from_orm(record).__root__ if get_all else LanguageSettingDTO.from_orm(record)

    @staticmethod
    @session_hook
    def bulk_create(db: Session, records: List[dict]):
        from sqlalchemy.exc import IntegrityError
        from app.models.language_setting import LanguageSetting

        list_to_be_updated: list = []

        for data in records:
            try:
                db.bulk_insert_mappings(LanguageSetting, [data])
            except IntegrityError:
                db.rollback()
                list_to_be_updated.append(data)

        if list_to_be_updated:
            db.bulk_update_mappings(LanguageSetting, list_to_be_updated)

        db.flush()
