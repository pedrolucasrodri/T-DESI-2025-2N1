class paciente:
    def __init__(self, nome, diagnostico, cor_pulseira, contato):
        self.nome = nome
        self.diagnostico = diagnostico
        self.cor_pulseira = cor_pulseira
        self.contato = contato

paciente_01 = paciente("Pedro", "Febre", "Amarelo", "47 1234-5678")
print(paciente_01.nome)
print(paciente_01.diagnostico)
print(paciente_01.cor_pulseira)
print(paciente_01.contato)
