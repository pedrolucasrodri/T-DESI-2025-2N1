import sqlite3
from models.cliente import Cliente
from dao.cliente_dao import ClienteDAO

class ClienteView:
    def __init__(self):
        # A View instancia o DAO para poder se comunicar com o banco
        self.dao = ClienteDAO()

    def exibir_menu(self):
        while True:
            print("\n=== SISTEMA DE GERENCIAMENTO DE CLIENTES ===")
            print("1 - Cadastrar Cliente")
            print("2 - Listar Clientes")
            print("0 - Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.cadastrar()
            elif opcao == '2':
                self.listar()
            elif opcao == '0':
                print("Saindo do sistema... Até logo!")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def cadastrar(self):
        print("\n--- CADASTRO DE CLIENTE ---")
        try:
            # 1. Captura de inputs do usuário
            id_cliente = int(input("Digite o ID do cliente: "))
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            
            # 2. Instancia o Objeto
            novo_cliente = Cliente(id_cliente, nome, email)
            
            # 3. Chama o DAO para salvar
            self.dao.salvar(novo_cliente)
            print("Sucesso: Cliente cadastrado!")
            
        except ValueError:
            # Captura erro se o usuário digitar letra no lugar de número no ID
            print("ERRO DE DIGITAÇÃO: O ID deve ser um número inteiro!")
            
        except sqlite3.OperationalError as e:
            # Captura o erro repassado pelo DAO e mostra o aviso amigável
            print(f"AVISO AMIGÁVEL: Ocorreu um problema na estrutura do banco de dados (A tabela pode não existir). Detalhe técnico: {e}")
            
        except Exception as e:
            # Fallback para qualquer outro erro genérico
            print(f"ERRO INESPERADO: {e}")

    def listar(self):
        print("\n--- LISTA DE CLIENTES ---")
        try:
            # Chama o DAO para buscar a lista
            clientes = self.dao.listar_todos()
            
            if not clientes:
                print("Nenhum cliente cadastrado no momento.")
            else:
                for c in clientes:
                    # Imprime de forma limpa usando os atributos do objeto
                    print(f"[{c.id}] Nome: {c.nome} | E-mail: {c.email}")
                    
        except sqlite3.OperationalError as e:
            print(f"AVISO AMIGÁVEL: Não foi possível listar. A tabela de clientes não existe no banco de dados. Detalhe técnico: {e}")
            
        except Exception as e:
            print(f"ERRO INESPERADO: {e}")