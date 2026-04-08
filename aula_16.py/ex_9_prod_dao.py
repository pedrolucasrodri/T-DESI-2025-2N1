import sqlite3

class ProdutoDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, produto):
        if produto.preco < 0:
            raise ValueError("O preço do produto não pode ser negativo!")

        cursor = self.conexao.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, preco) VALUES (?, ?)", 
            (produto.nome, produto.preco)
        )
        self.conexao.commit()
        produto.id = cursor.lastrowid
        return produto