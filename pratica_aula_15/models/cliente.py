# models/cliente.py

class Cliente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
        
    def __repr__(self):
        return f"Cliente({self.id}, '{self.nome}', '{self.email}')"