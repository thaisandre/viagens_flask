from flask import Blueprint
from flask_restplus import Api

rotas_api = Blueprint('rotas', __name__, url_prefix='/rotas-api')

api = Api(version='1.0', title='Rotas API', description='Api de Rotas', validate=True)
api.init_app(rotas_api)

from rotas.pais.resource import api as pais_resource
api.add_namespace(pais_resource, path='/paises')