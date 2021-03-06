from typing import Any, Dict, List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.dto.model.translated_text import TranslatedTextDTO, TranslatedTextDTOs

from app.utils.session import session_hook


class TranslatedTextLib:

    @staticmethod
    @session_hook
    def bulk_save(db: Session, payload: List[Dict[str, Any]]) -> None:
        from app.models.translated_text import TranslatedText

        scripts_to_be_updated: list = []
        
        for script in payload:
            try:
                db.bulk_insert_mappings(TranslatedText, [script])
            except IntegrityError:
                db.rollback()
                scripts_to_be_updated.append(script)

        if scripts_to_be_updated:
            db.bulk_update_mappings(TranslatedText, scripts_to_be_updated)

        db.flush()
        return

    @staticmethod
    @session_hook
    def get_all_by_text_id(db: Session, text_id: int) -> None:
        from app.models.translated_text import TranslatedText

        records = db.query(TranslatedText).filter_by(text_id=text_id).all()
        
        return TranslatedTextDTOs.from_orm(records).__root__ if records else []
    
    @staticmethod
    @session_hook
    def update(db: Session, data: dict) -> TranslatedTextDTO:
        from app.models.translated_text import TranslatedText

        record = db.query(TranslatedText).filter_by(text_id=data.get("text_id"),
                                               language_id=data.get("language_id")).first()

        for key, value in data.items():
            record.__setattr__(key, value)

        db.flush()
        return TranslatedTextDTO.from_orm(record)
