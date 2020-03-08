from flask_restplus import Resource
from rotas.pais.dto import PaisDto, PaisInputDto, PaisOutputDto
from rotas.pais.service import save, list_all

api = PaisDto.api

@api.route('/')
class PaisResources(Resource):

    @api.marshal_with(PaisOutputDto.pais_criado)
    @api.expect(PaisInputDto.novo_pais, validate=True)
    def post(self):
        return save(PaisInputDto.to_model()), 201