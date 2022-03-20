
class DateLib:
    """DateLib for Generating dates (from present year to 5years plus)
        and dates details and writes to the database

    Args:
        No Args

    Returns:
        None

    Usage:
        DateLib().run()
    """
    from sqlalchemy.orm import Session
    from app.utils.session import session_hook

    def __init__(self):
        self.names_of_days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        self.names_of_months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]

    def __create_dates__(self, start_year: int, stop_year: int):
        import pandas as pd

        # check if start year is not greater than stop year
        if start_year > stop_year:
            raise Exception(f"start_year cannot be greater than stop year")

        start_date = f"{start_year}-01-01"
        stop_date = f"{stop_year}-12-31"

        # create a pd datetime object
        start_date_ts = pd.to_datetime(start_date)
        stop_date_ts = pd.to_datetime(stop_date)

        # generate date from start and stop date timestamp and rename index
        date_df = pd.DataFrame(index=pd.date_range(start_date_ts, stop_date_ts))
        date_df.index.name = "full_date"

        # generate and create other columns
        days_names = {index: index + 1 for index, name in enumerate(self.names_of_days)}

        date_df["date_full_name"] = date_df.index.strftime("%B %d %Y")
        date_df["date_key"] = date_df.index.strftime('%Y%m%d')

        date_df["year"] = date_df.index.year
        date_df["is_leap_year"] = date_df.index.is_leap_year

        date_df["month_number"] = date_df.index.month
        date_df["month_name"] = date_df.index.strftime('%B')

        date_df["year_week"] = date_df.index.isocalendar().week
        date_df["day_of_week"] = date_df.index.dayofweek.map(days_names.get)

        date_df["day_of_month"] = date_df.index.day
        date_df["day_of_year"] = date_df.index.dayofyear

        date_df["day_name"] = date_df.index.strftime("%A")
        date_df["is_working_day"] = date_df["day_of_week"].apply(lambda day: True if day <= 5 else False)

        date_df["quarter"] = date_df.index.quarter
        date_df["year_half"] = date_df.index.month.map(lambda mth: 1 if mth < 7 else 2)

        date_df.reset_index(inplace=True)

        return list(date_df.T.to_dict().values())

    def run(self):
        from app.logs import logger
        from datetime import datetime

        start_year = datetime.utcnow().year
        if DateLib.check_present_year(year=start_year):
            return

        stop_year = start_year + 5
        dates: list = self.__create_dates__(start_year, stop_year)

        DateLib.bulk_create(records=dates)
        logger.info(f"Done Creating dates From {start_year}-01-01 to {stop_year}-12-31")
        return

    @staticmethod
    @session_hook
    def bulk_create(db: Session, records: list):
        from app.models.date import Date

        for record in records:
            db.bulk_insert_mappings(Date, [record])

    @staticmethod
    @session_hook
    def check_present_year(db: Session, year: int):
        from app.models.date import Date

        return True if db.query(Date).filter_by(year=year).first() else False

    @staticmethod
    @session_hook
    def get_current_day_from_record(db: Session):
        from datetime import datetime
        from app.models.date import Date

        full_date = datetime.utcnow().date()

        record = db.query(Date).filter_by(full_date=full_date).first()

        return record if record else None
