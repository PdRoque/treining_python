print("*******")
print("PAR OU ÍMPAR")
print("*******")

num = int(input("Digite um número: "))

if num % 2 == 0: # número par divido por 2 possui resto = 0, número ímpar divido por 2 possui resto = 1
    print("O número é par. ")
else:
    print("O número é ímpar. ")

#utilizando % para pegar o resto da divisão simples. 
#Ex: 2/2 tem resto 0 (número par). 3/2 tem resto 1 em divisão simples (número ímpar).

