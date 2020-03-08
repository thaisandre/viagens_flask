from flask_restplus import fields, Namespace, reqparse
from rotas.pais.validator import validate
from rotas.pais.model import Pais

class PaisDto:
    api = Namespace('pais', description='recursos paises')

class PaisInputDto(PaisDto):
    novo_pais = reqparse.RequestParser()\
        .add_argument('nome',
                      type=validate,
                      required=True,
                      location='json',
                      nullable=False)

    pais_editado = reqparse.RequestParser()\
        .add_argument('nome',
                      type=validate,
                      required=True,
                      location='json',
                      nullable=False)

    @classmethod
    def _nome(cls):
        return cls.novo_pais.parse_args()['nome']

    @classmethod
    def to_model(cls):
        return Pais(cls._nome())

class PaisOutputDto(PaisDto):
    api = PaisDto.api

    pais_criado = api.model('pais', {
            'id' : fields.Integer,
            'nome': fields.String
    })
