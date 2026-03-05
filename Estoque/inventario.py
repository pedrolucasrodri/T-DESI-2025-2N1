estoque = {
    "Cilindro":       [35, 75.99],
    "Valvula escape": [10, 15.65],
    "Filtro de ar":   [20, 35.50]
}

historico_compras = []

print("Informe nome do produto, quantidade e valor")

# cadastro de produtos e verificação se item já foi cadastrado #

continuar = "sim"

while continuar == "sim":
    produtos    = (input("Produto: "))

    if produtos in estoque:
        print("Error, produto já cadastrado!")
        continuar = input("Continuar cadastrando? (sim/não)").lower()
    else:
        quantidades = int(input("Unidades: "))
        precos      = float(input("Valores: "))
        estoque[produtos] = [quantidades, precos]
        print("Produto cadastrado!")    
        continuar = input("Continuar cadastrando? (sim/não) ").lower()

print("\n --- ESTOQUE ATUALIZADO ---")
print(estoque)

# comprando o produto, verifica se o item existe na lista do estoque.

cancelar = "sim"

while cancelar == "sim":
    pedidos = (input("Qual o produto desejado?: "))
    
 
    if pedidos not in estoque:
        print("Erro, produto não existe!")
        cancelar = input("Cancelar compra? (sim/não): ").lower()
        if cancelar == "sim":
           break
        else:
            cancelar = "sim"
            continue
    else:
        while True:
            unidades = int(input("E quantas unidades?: "))
            
            # Verificação de saldo do estoque, se tem material suficiente para o pedido.
            if unidades <= estoque[pedidos][0]:
                estoque[pedidos][0] -= unidades
                print(f"Venda realizada! saldo restante {estoque[pedidos][0]} unidades.")
                (input("Concluir compra? (sim/não): ")).lower()

            else:
                print(f"Estoque insuficiente! temos apenas {estoque[pedidos][0]}.")
                tentar_novamente = (input("Por favor diminua a quantidade! (sim/não): ")).lower()

                if tentar_novamente != "sim":
                    break    

                
                