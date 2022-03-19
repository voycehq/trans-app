from typing import Callable, Any


def session_hook(func: Callable) -> object:
    """Session hook for our Datasources Database

    Args:
        func (Callable): the function to inject the db session as the first param

    Returns:
        object: callable result
    """

    def run(*args, **kwargs):
        from app.utils.connection import SessionLocal
        import traceback

        db = SessionLocal()

        try:
            result: Any = func(db, *args, **kwargs)

            return result
        except Exception as exc:
            traceback.print_exc()
            raise Exception(exc)

        finally:
            db.close()

    return run
