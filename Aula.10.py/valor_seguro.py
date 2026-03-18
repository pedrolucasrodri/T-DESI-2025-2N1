
# Solicitando um valor financeiro ao usuário de forma segura
while True:
    try:
        # Tenta converter a entrada diretamente para float
        valor = float(input("Digite o valor do depósito: R$ "))
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        break # Sai do loop se der tudo certo
    except ValueError:
        # Se o usuário digitar "cem", o float() levanta um ValueError
        # O programa cai aqui em vez de crashar
        print("ERRO: Por favor, digite apenas valores numéricos válidos (ex: 150.50).")