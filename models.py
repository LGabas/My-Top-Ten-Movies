from sqlalchemy import Column, Integer, String, Float
from extensions import db

class Base(db.Model):
    __abstract__ = True


class Movie(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(250), unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    description = Column(String(1000), nullable=False)
    rating = Column(Float)
    ranking = Column(Integer)
    review = Column(String(1000))
    img_url = Column(String(1000), nullable=False)