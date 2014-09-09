from sqlalchemy import exc

from application.dal.model import *
from application.dal.db_functions import insert_item


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


def fill_dictionaries():
    _fill_sample_types()


def _fill_sample_types():
    insert_item(SampleType(1, u'Утро'))
    insert_item(SampleType(2, u'День'))
    insert_item(SampleType(3, u'Вечер'))


def initialize_database():
    session = Session()
    create_scheme()
    fill_dictionaries()