import unittest
import sqlite3

class Usuario:
    def __init__(self, nome, email):
        self.id = None
        self.nome = nome
        self.email = email

class UsuarioDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, usuario):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (usuario.nome, usuario.email))
        self.conexao.commit()
        usuario.id = cursor.lastrowid
        return usuario

    def buscar_por_id(self, id_usuario):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios WHERE id = ?", (id_usuario,))
        linha = cursor.fetchone()
        if linha:
            user = Usuario(linha[1], linha[2])
            user.id = linha[0]
            return user
        return None

    def deletar(self, id_usuario):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
        self.conexao.commit()


    def atualizar(self, id_usuario, novo_nome):
        cursor = self.conexao.cursor()

        cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (novo_nome, id_usuario))
        #self.conexao.commit()


class TestUsuarioDAO(unittest.TestCase):
    def setUp(self):
        self.conexao = sqlite3.connect(':memory:')
        self.conexao.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)")
        self.dao = UsuarioDAO(self.conexao)

    def test_salvar_e_buscar_objeto(self):
        usuario_original = Usuario("Ana Silva", "ana@email.com")
        usuario_salvo = self.dao.salvar(usuario_original)
        
        usuario_recuperado = self.dao.buscar_por_id(usuario_salvo.id)
        
        self.assertIsNotNone(usuario_recuperado)
        self.assertEqual(usuario_original.nome, usuario_recuperado.nome)
        self.assertEqual(usuario_original.email, usuario_recuperado.email)

    def test_deletar_objeto(self):
        usuario = Usuario("Carlos Deletado", "carlos@email.com")3
        usuario_salvo = self.dao.salvar(usuario)
        id_para_deletar = usuario_salvo.id 

        self.dao.deletar(id_para_deletar)
        usuario_recuperado = self.dao.buscar_por_id(id_para_deletar)
        self.assertIsNone(usuario_recuperado)

    def test_atualizar_objeto(self):

        usuario = Usuario("João Antigo", "joao@email.com")
        usuario_salvo = self.dao.salvar(usuario)
        id_alvo = usuario_salvo.id

        nome_esperado = "João Moderno"
        self.dao.atualizar(id_alvo, nome_esperado)

        usuario_atualizado = self.dao.buscar_por_id(id_alvo)

        self.assertEqual(usuario_atualizado.nome, nome_esperado)

        self.assertEqual(usuario_atualizado.email, "joao@email.com")

    def tearDown(self):
        self.conexao.close()

if __name__ == '__main__':
    unittest.main()