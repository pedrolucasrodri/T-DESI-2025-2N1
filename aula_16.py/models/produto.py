class Produto:
    def __init__(self, id, nome, qtd_est):
        self.id = id
        self.nome = nome
        self.qtd_est = qtd_est
    
    def __repr__(self):
        return f"Produto({self.id}, {self.nome},{self.qtd_est})"