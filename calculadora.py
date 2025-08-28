print("**********")
print("CALCULADORA")
print("**********")


num1 = int(input("Selecione o primeiro número: "))
num2 = int(input("Selecione o segundo número: "))
sinal = input("Selecione a operação: Soma(+), Subtração(-), Multiplicação(*), Divisão(/): ")

if sinal == "+":
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif sinal == "-":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif sinal == "*":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif sinal == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha +, -, * ou /.")


