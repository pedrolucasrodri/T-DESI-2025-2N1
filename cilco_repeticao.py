saldo = 1000.0
opcao = input("Digite um dos números abaixo: \n")

while opcao != "4":
    opcao = input("Digite a opção desejada:\n [1] Ver saldo\n [2] Depositar\n [3] Sacar\n [4] Sair\n")
    
    if opcao == "1":
        print(f"Seu saldo é de R$ {saldo:.2f}")

    elif opcao == "2":
       deposito =  float(input("Digite o valor para deposito: "))
       
    if deposito > 0:
        saldo = saldo + deposito
        print(f"Seu saldo é de R$ {saldo}")
    else:
        print("Erro: favor informar um valor maior que 0")

    elif opcao == "3":
        saque = float(input("Informe o valor a ser sacado: "))
        saque = saldo - saque
        print(f"Saldo R$ {saque}")
