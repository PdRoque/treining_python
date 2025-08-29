print("********")
print("TABUADA")
print("********")

#Pede o número ao usuário
num = int(input("Digite o número para ver a tabuada: "))
print("********")

#
for num_tabuada in range(1,11): #range(1,11) = Inicia o laço de repetição de 1 a 10 
    #Fazendo o cálculo
    resultado = num * num_tabuada
    #Mostrando o resultado de forma clara
    print(f"{num} x {num_tabuada} = {resultado}")


#O for e o in são usados para repetir algo em Python.
#Eles formam um laço (ou loop), que percorre uma coleção de itens, como uma lista, um texto ou uma sequência de números.


#O for começa. Ele pega o primeiro item da lista guarda na variável num_tabuada.
#O print é executado com o primeiro valor da variável num_tabuada: 1 * num
#O for volta para o início e pega o segundo item de range: 2, e guarda na variável num_tabuada.
#O print é executado novamente: 2 * num
#O for pega o terceiro item: 3, e guarda na variável num_tabuada e repete o mesmo processo ate o ultimo valor: 10
