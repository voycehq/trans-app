from app.dto.model.verification import VerificationDTO, VerificationDTOs


class VerificationLib:
    from app.utils.session import session_hook
    from sqlalchemy.orm import Session

    @staticmethod
    @session_hook
    def create_verification(db: Session, data: dict):
        from app.models.verification import Verification

        verification = Verification(**data)

        db.add(verification)
        db.flush()

        return VerificationDTO.from_orm(verification)

    @staticmethod
    @session_hook
    def update(db: Session, data: dict) -> VerificationDTO:
        from app.models.verification import Verification

        record = db.query(Verification).filter_by(customer_id=data.get("customer_id")).first()
        for key, value in data.items():
            record.__setattr__(key, value)
        db.flush()
        return VerificationDTO.from_orm(record)

    @staticmethod
    @session_hook
    def find_by(db: Session, where: dict, get_all: bool = False):
        from app.models.verification import Verification

        record = db.query(Verification).filter_by(**where)
        record = record.all() if get_all else record.first()

        if not record:
            return None

        return VerificationDTOs.from_orm(record).__root__ if get_all else VerificationDTO.from_orm(record)

    @staticmethod
    @session_hook
    def verify_code(db: Session, verification_info: VerificationDTO):
        from app.models.verification import Verification

        record = db.query(Verification).filter_by(code=verification_info.code, customer_id=verification_info.customer_id).first()
        record.code = None
        db.flush()
        return
