def calculadora():
    while True:
        # Mostra as opções de operações
        print("\nOperações:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        # Solicita a escolha do usuário
        escolha = input("Digite o número para a operação desejada: ")

        # Verifica se a escolha é válida
        if escolha not in ['0', '1', '2', '3', '4']:
            print("Essa opção não existe. Por favor, escolha uma opção válida.")
            continue

        # Se escolha for '0', encerra o programa
        if escolha == '0':
            print("Encerrando a calculadora. Até mais!")
            break

        # Solicita os números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Realiza a operação selecionada
        if escolha == '1':
            resultado = num1 + num2
        elif escolha == '2':
            resultado = num1 - num2
        elif escolha == '3':
            resultado = num1 * num2
        elif escolha == '4':
            if num2 != 0:  # Verifica se o divisor não é zero
                resultado = num1 / num2
            else:
                print("Erro: Divisão por zero. Resultado indefinido.")
                continue

        # Mostra o resultado da operação
        print("Resultado:", resultado)

if __name__ == "__main__":
    calculadora()
