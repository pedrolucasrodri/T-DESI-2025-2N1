import sqlite3
from models.produto import Produto

class ProdutoDAO:
    def __init__(self, db_path='banco_loja.db'):
        self.db_path = db_path
        self.criar_tabela()

    def criar_tabela(self):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        sql = """
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT,
                qtd_est INTEGER
            )
            """
        cursor.execute(sql)
        conexao.commit()
        conexao.close()

    def salvar(self, produto: Produto):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        sql = "INSERT INTO produtos (nome, qtd_est) VALUES (?,?)"
        valores = (produto.nome, produto.qtd_est)

        cursor.execute(sql, valores)
        conexao.commit()

        produto.id = cursor.lastrowid
        conexao.close()
        return produto