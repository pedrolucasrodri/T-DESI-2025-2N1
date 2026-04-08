import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.produto import Produto
from dao.produto_dao import ProdutoDAO

class TestProdDAO(unittest.TestCase):
    
    def setUp(self):
        # 1. Definimos um nome para um banco de teste temporário
        self.nome_banco_teste = 'banco_teste.db'
        
        # 2. Passamos esse arquivo para o DAO (ele vai criar o arquivo e a tabela)
        self.dao = ProdutoDAO(self.nome_banco_teste)

    def tearDown(self):
        # 3. O tearDown agora deleta o arquivo de teste após rodar para não deixar lixo!
        if os.path.exists(self.nome_banco_teste):
            os.remove(self.nome_banco_teste)

    def test_salvar_prod(self):
        prod_novo = Produto(None, "Teclado Mecanico", 15)

        prod_salvo = self.dao.salvar(prod_novo)

        self.assertIsNotNone(prod_salvo.id)
        self.assertEqual(prod_salvo.nome, "Teclado Mecanico")
        
        # Corrigido para bater com o nome exato do atributo no model Produto
        self.assertEqual(prod_salvo.qtd_est, 15) 

if __name__ == '__main__':
    unittest.main()