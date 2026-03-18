saldo = 1000.0
opcao = ""

while opcao != "4":
    print(f"\nSaldo atual: R$ {saldo:.2f}") # Exibe o saldo para te ajudar a testar
    opcao = input("Escolha: [1] Saldo [2] Depósito [3] Saque [4] Sair: ")

    if opcao == "1":
        print(f"Seu saldo é R$ {saldo:.2f}")
    
    elif opcao == "2":
        # Tente escrever a lógica do depósito aqui!
        # Dica: peça o valor, verifique se é > 0 e some ao saldo.
        pass # O 'pass' é só um espaço reservado, substitua-o pelo seu código

    elif opcao == "3":
        # Aqui você fará o saque (subtrair), mas precisa checar se o saldo é suficiente.
        pass

    elif opcao == "4":
        print("Saindo... Até logo!")
    
    else:
        print("Opção inválida!")

        