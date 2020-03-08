import unittest
from tests.base import BaseTestCase
from rotas.pais.model import Pais
from rotas.pais.validator import validate
from rotas.pais import service

class TestPaisValidator(BaseTestCase):

    def test_deve_detectar_erro_validacao_de_pais_com_nome_nulo(self):
        with self.assertRaises(ValueError) as context:
            value = validate("")

        with self.assertRaises(ValueError) as context:
            value = validate(None)

    def test_deve_detectar_erro_validacao_de_pais_existente(self):
        service.save(Pais('Argentina'))
        with self.assertRaises(ValueError) as context:
            value = validate("Argentina")

if __name__ == "__main__":
    unittest.main()