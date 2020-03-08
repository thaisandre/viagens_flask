from rotas.pais.model import Pais
from rotas.validator.validators import not_empty

def validate(value):
    not_empty(value)
    pais_existente(value)
    return value

def pais_existente(value):
    not_empty(value)
    pais_buscado = Pais.query.filter(Pais.nome == value).first()
    if pais_buscado:
        raise ValueError("pais com mesmo nome já existe no sistema.")
    return value