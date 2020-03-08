import unittest
from tests.base import BaseTestCase
import json
from rotas.pais import service
from rotas.pais.model import Pais

url = '/rotas-api/paises/'

class TestPaisResource(BaseTestCase):

    def test_deve_cadastrar_pais_com_sucesso(self):
        with self.client:
            novo_pais_json = json.dumps(dict(nome="Argentina"))
            response = self.client.post(url, data=novo_pais_json, content_type="application/json")
            data = json.loads(response.data.decode())

            self.assertTrue(data['nome'] == 'Argentina')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_nao_deve_cadastrar_pais_com_nome_nulo(self):
        with self.client:
            novo_pais_json = json.dumps(dict(nome=""))
            response = self.client.post(url, data=novo_pais_json, content_type="application/json")
            data = json.loads(response.data.decode())

            self.assertTrue(data['errors']['nome'] == 'não pode ser nulo.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_nao_deve_cadastrar_pais_existente(self):
        service.save(Pais('Argentina'))

        novo_pais_json = json.dumps(dict(nome="Argentina"))
        response = self.client.post(url, data=novo_pais_json, content_type="application/json")
        data = json.loads(response.data.decode())

        self.assertTrue(data['errors']['nome'] == 'pais com mesmo nome já existe no sistema.')
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()