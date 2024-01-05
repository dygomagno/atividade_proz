#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:

def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Verifica se o divisor não é zero
            return num1 / num2
        else:
            print("Erro: Divisão por zero.")
            return 0
    else:
        print("Operação não reconhecida.")
        return 0

# Exemplo de uso:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação (1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão): "))

resultado = calculadora(num1, num2, operacao)
print("Resultado:", resultado)

