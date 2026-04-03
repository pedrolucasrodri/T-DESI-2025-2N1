import sqlite3
from models.cliente import Cliente

class ClienteDAO:
    def __init__(self, db_path: str = 'meu_banco.db'):
        self.db_path = db_path
        self.criar_tabela()

    def criar_tabela(self):

        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()
        
        sql = """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT
        )
        """
        cursor.execute(sql)
        conexao.commit()
        cursor.close()
        conexao.close()

    def salvar(self, cliente: Cliente):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
            
            sql  = "INSERT INTO clientes (id, nome, email) VALUES (?,?,?)"
            valores = (cliente.id, cliente.nome, cliente.email)
            
            cursor.execute(sql, valores)
            conexao.commit()
            print("LOG: Cliente salvo com sucesso no banco de dados.")
            
        except sqlite3.Error as e:
            print(f"ERRO DAO: Falha ao inserir cliente. Detalhe: {e}")
            
        finally:
            cursor.close()
            conexao.close()
        
    def listar_todos(self):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()
        
        cursor.execute("SELECT id, nome, email FROM clientes") 
        resultado_bruto = cursor.fetchall()

        lista_dados = []
        for linha in resultado_bruto:
            cliente_dicionario = {
                "id": linha[0],
                "nome": linha[1],
                "email": linha[2]
            }
            lista_dados.append(cliente_dicionario)

        conexao.close()
        
        print("--- RELATÓRIO DO SISTEMA ---")
        
        if len(lista_dados) == 0:
            print("Nenhum cliente cadastrado no momento.")
        else:
            for cliente in lista_dados:
                print(f"[{cliente['id']}] Nome: {cliente['nome']}, Email: {cliente['email']}")