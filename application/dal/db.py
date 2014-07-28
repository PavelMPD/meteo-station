from sqlalchemy import exc

from application.dal.model import *


def create_scheme():
    """
    Create database scheme.
    """

    result = False
    try:
        Base.metadata.create_all(engine)
        result = True
    except exc.SQLAlchemyError:
        result = False

    return result


def initialize_database():
    session = Session()
    create_scheme()