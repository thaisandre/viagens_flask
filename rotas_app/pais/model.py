from run import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property

class Pais(db.Model):

    _id = Column('id', Integer(), primary_key=True)
    _nome = Column('nome', String(255), nullable=False, unique=True)

    def __init__(self, nome, id=None):
        self._nome = nome
        self._id = id

    @hybrid_property
    def id(self):
        return self._id

    @hybrid_property
    def nome(self):
        return self._nome