#Cria a variável para guardar a soma, começando com 0
soma = 0

#Usa o laço (loop) for para percorrer os números de 1 a 100
for valores in range(1,101):
     #Adiciona o valor de 'valores' à variável 'soma'
    soma = soma + valores


print(f"a soma de 1 a 100 é: {soma}")


#O que significa soma = soma + valores?
#À primeira vista, pode parecer um erro matemático, já que soma não pode ser igual a soma + valores na álgebra tradicional.
# No entanto, em programação, o sinal de = não significa "igual a", mas sim "recebe o valor de" ou "atribui o valor de".

#A Analogia do Cofrinho
#Imagine que a variável soma é um cofrinho e a expressão soma = soma + valores é o ato de colocar moedas nele.
#Você começa com um cofrinho vazio: soma = 0.
#Você coloca a primeira moeda, de 1 real: soma = 0 + 1. Agora, seu cofrinho tem 1 real.
#Você coloca a segunda moeda, de 2 reais: soma = 1 + 2. Agora, seu cofrinho tem 3 reais.
#Você coloca a terceira moeda, de 3 reais: soma = 3 + 3. Agora, seu cofrinho tem 6 reais.
