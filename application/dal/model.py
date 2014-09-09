import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Date, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

from application.dal.db_config import DB_SERVER, DB_NAME


engine = create_engine(DB_SERVER + '/' + DB_NAME, echo=True)
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


class DaySample(Base):
    __tablename__ = 'day_samples'

    id = Column(UUID, primary_key=True)
    date = Column(Date, nullable=False, default=datetime.date)
    samples = relationship('Sample')

class Sample(Base):
    __tablename__ = 'samples'

    id = Column(UUID, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    air_temperature = Column(Float, nullable=False)
    water_temperature = Column(Float, nullable=False)
    water_level = Column(Integer, nullable=False)
    #one to many
    day_sample_id = Column(UUID, ForeignKey('day_samples.id'))
    #many to one
    sample_type_id = Column(Integer, ForeignKey('sample_types.id'))
    sample_type = relationship("SampleType")


class SampleType(Base):
    __tablename__ = 'sample_types'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Post(Base):
    __tablename__ = 'posts'

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    employees = relationship('Employee')


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(UUID, primary_key=True)
    fio = Column(String, nullable=False)


class PostEmployee(Base):
    __tablename__ = 'post_employee'

    post_id = Column(UUID, ForeignKey('posts.id'))
    employee_id = Column(UUID, ForeignKey('employees.id'))
    posts = relationship('post')