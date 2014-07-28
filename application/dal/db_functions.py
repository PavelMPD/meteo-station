from sqlalchemy import exc

from application.dal.model import *


def insert_item(item):
    """
    Insert item into database
    """

    session = Session()

    result = False
    try:
        session.add(item)
        session.commit()
        result = True
    except exc.SQLAlchemyError:
        session.rollback()

    return result


def update_item(item):
    """
    Update item into database
    """

    result = False
    session = Session()
    try:
        exist_item = session.query(type(item)).filter_by(id=item.id)
        exist_item = item
        session.commit()
        result = True
    except exc.SQLAlchemyError:
        session.rollback()

    return result


def get_item(type, id):
    """
    Get item from database via fid
    """

    session = Session()
    item = None
    try:
        item = session.query(type).get(id)
    except exc.SQLAlchemyError:
        item = None

    return item


def get_items(type):
    """
    Get all items from table
    """

    session = Session()
    items = None
    try:
        items = session.query(type).filter_by(deleted=False)
    except exc.SQLAlchemyError:
        items = None

    return items


def delete_item(item):
    """
    Delete this item
    """
    result = False
    session = Session()
    try:
        session.delete(item)
        session.commit()
        result = True
    except exc.SQLAlchemyError:
        session.rollback()
    return result


def delete_item_by_id(type, id):
    """
    Delete item by id
    """

    result = False
    session = Session()
    try:
        item = session.query(type).get(id)
        session.delete(item)
        session.commit()
        result = True
    except exc.SQLAlchemyError:
        session.rollback()

    return result