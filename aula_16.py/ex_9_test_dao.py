import unittest
import sqlite3

class Produto:
    def __init__(self, nome, preco):
        self.id = None
        self.nome = nome
        self.preco = preco

class ProdutoDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, produto):
        if produto.preco < 0:
            raise ValueError("O preço do produto não pode ser negativo!")
        
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", (produto.nome, produto.preco))
        self.conexao.commit()
        produto.id = cursor.lastrowid
        return produto

class TestProdutoConfiabilidade(unittest.TestCase):
    
    def setUp(self):
        self.conexao = sqlite3.connect(':memory:')
        self.conexao.execute("CREATE TABLE produtos (id INTEGER PRIMARY KEY, nome TEXT, preco REAL)")
        self.dao = ProdutoDAO(self.conexao)

    def test_bloqueio_preco_negativo(self):
        p_invalido = Produto("Produto Errado", -10.50)
        with self.assertRaises(ValueError):
            self.dao.salvar(p_invalido)

    def test_salvamento_preco_valido(self):
        p_valido = Produto("Produto Bom", 100.00)
        resultado = self.dao.salvar(p_valido)
        self.assertIsNotNone(resultado.id)

    def tearDown(self):
        self.conexao.close()

if __name__ == '__main__':
    unittest.main()