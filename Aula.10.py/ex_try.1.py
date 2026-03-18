while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        result = num1 / num2
        print(f"Resultado {result}")
        break
    except ValueError:
        print("Insira valores númericos")
    except ZeroDivisionError:
        print("Não é possivel dividir por 0, insira um número diferente")
        