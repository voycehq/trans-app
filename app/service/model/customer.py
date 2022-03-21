class CustomerLib:
    from app.utils.session import session_hook
    from sqlalchemy.orm import Session
    from app.dto.model.customer import CustomerDTO

    @staticmethod
    @session_hook
    def find_by(db: Session, where: dict, get_all: bool = False):
        from app.dto.model.customer import CustomerDTOs, CustomerDTO
        from app.models.customer import Customer

        record = db.query(Customer).filter_by(**where)
        record = record.all() if get_all else record.first()

        if not record:
            return None

        return CustomerDTOs.from_orm(record).__root__ if get_all else CustomerDTO.from_orm(record)

    @staticmethod
    @session_hook
    def create(db: Session, data: dict) -> CustomerDTO:
        from app.models.customer import Customer
        from app.service.model.date import DateLib
        from app.dto.model.customer import CustomerDTO
        from app.utils.utils import Utils

        new_customer = Customer(**data)

        # hash password
        new_customer.password = Utils.hash_string(data.get("password"))

        # get date_id
        date_info = DateLib.get_today_date()
        new_customer.date_id = date_info.id

        # write to database
        db.add(new_customer)
        db.flush()

        return CustomerDTO.from_orm(new_customer)

    @staticmethod
    @session_hook
    def set_is_verified_true(db: Session, email: str):
        from app.models.customer import Customer

        customer = db.query(Customer).filter_by(email=email).first()
        customer.is_verified = True

        db.flush()

        return customer
