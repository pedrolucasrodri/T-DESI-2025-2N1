from dao.cliente_dao import ClienteDAO
from models.cliente import Cliente

cliente_ana = Cliente(1, "Ana", "ana@senai.br")

dao = ClienteDAO()
dao.salvar(cliente_ana)
dao.listar_todos()