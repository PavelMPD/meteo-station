import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Date, DateTime, Float, ForeignKey
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
    samples = relationship('samples')


class Sample(Base):
    __tablename__ = 'samples'

    id = Column(UUID, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    air_temperature = Column(Float, nullable=False)
    water_temperature = Column(Float, nullable=False)
    water_level = Column(Integer, nullable=False)
    day_sample_id = Column(UUID, ForeignKey('day_samples.id'))