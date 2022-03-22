from sqlalchemy.orm import Session

from app.dto.model.text import TextDTO
from app.utils.session import session_hook


class TextLib:
    @staticmethod
    @session_hook
    def create(db: Session, data: dict) -> TextDTO:
        from app.models.text import OriginalText
        from app.service.model.date import DateLib

        record = OriginalText(**data)

        # get date_id
        date_info = DateLib.get_today_date()
        record.date_id = date_info.id

        # write to database
        db.add(record)
        db.flush()

        return TextDTO.from_orm(record)

    @staticmethod
    @session_hook
    def find_by(db: Session, where: dict, get_all: bool = False):
        from app.models.text import OriginalText
        from app.dto.model.text import TextDTO, TextDTOs

        record = db.query(OriginalText).filter_by(**where)
        record = record.all() if get_all else record.first()

        if not record:
            return None

        return TextDTOs.from_orm(record).__root__ if get_all else TextDTO.from_orm(record)
