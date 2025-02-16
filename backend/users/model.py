# describle table structure in DB
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column

db = SQLAlchemy()
Base = db.Model

class User(Base):
    __tablename__ = 'user'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(100), nullable=False)
    address = Column(db.String(200), nullable=False)
