from database import db

def save(pais):
    db.session.add(pais)
    db.session.commit()
    return pais