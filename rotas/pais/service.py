from database import db
from rotas.pais.model import Pais

def save(pais):
    db.session.add(pais)
    db.session.commit()
    return pais

def list_all():
    return Pais.query.all()