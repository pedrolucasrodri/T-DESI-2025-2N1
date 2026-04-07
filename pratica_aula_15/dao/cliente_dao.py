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
            raise e 
        finally:
            cursor.close()
            conexao.close()
        
    def listar_todos(self):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()
        
        cursor.execute("SELECT id, nome, email FROM clientes") 
        resultado_bruto = cursor.fetchall()

        lista_clientes = []
        for linha in resultado_bruto:
            cliente_obj = Cliente(linha[0], linha[1], linha[2])
            lista_clientes.append(cliente_obj)

        conexao.close()
        return lista_clientes

    def buscar_por_id(self, id_busca: int):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()
        sql = "SELECT id, nome, email FROM clientes WHERE id = ?"
        cursor.execute(sql, (id_busca,))
        linha = cursor.fetchone() 
        conexao.close()
        if linha:
            return Cliente(linha[0], linha[1], linha[2])
        return None

    def atualizar(self, cliente: Cliente):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
            sql = "UPDATE clientes SET nome = ?, email = ? WHERE id = ?"
            valores = (cliente.nome, cliente.email, cliente.id)
            cursor.execute(sql, valores)
            conexao.commit()
            print(f"LOG: Cliente ID {cliente.id} atualizado com sucesso no banco.")
        except sqlite3.Error as e:
            raise e 
        finally:
            cursor.close()
            conexao.close()

    def deletar(self, id_deletar: int):
        cliente_existe = self.buscar_por_id(id_deletar)

        if cliente_existe:
            try:
                conexao = sqlite3.connect(self.db_path)
                cursor = conexao.cursor()
                sql = "DELETE FROM clientes WHERE id = ?"
                cursor.execute(sql, (id_deletar,))
                conexao.commit()
                print("Cliente deletado")
            except sqlite3.Error as e:
            # Em vez de print, nós lançamos o erro para a View capturar!
                raise e 
            finally:
                cursor.close()
                conexao.close()
                print("Aviso: Cliente inexistente")