# Função para Calcular desconto
def calcular_preco_final(valor, desconto_percent):
    valor_do_desconto = valor * (desconto_percent/100)
    preco_com_desconto = valor - valor_do_desconto
    return preco_com_desconto

total = calcular_preco_final(100, 15)
print(f"O preço do desconto é: R$ {total}")


# Função para saudação
def saudar_usuario():
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}! Bem-vindo!")

saudar_usuario()


# Função para 3 banners
def exibir_banner():
    empresa =[]
    
    for i in range(3):
        nome = input(f"Digite os nome da {i+1} empresa: ")
        empresa.append(nome)

    for empresa in empresa:
        print(f" { '*' * 10} {empresa} { '*' * 10}" )

exibir_banner()


# Função para 1 empresa
def exibir_banner():
    empresa = input("Digite o nome da empresa: ")
    print(f"{'*' * 10 } {empresa} {'*' * 10 } ")

exibir_banner()