# Crie uma lista apenas com elementos numéricos

numeros = [1, 2, 3, 4, 5, 6]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora

impares = [1, 3, 5, 7]
lista = ['Jean', [2010, 2014, 2018], numeros, True, impares]

# Imprima na tela apenas os 5 primeiros elementos da lista

print(lista[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par

elementos_indice_par = (lista[::2])
print(elementos_indice_par)

# Remova da lista o último item

lista.pop()
print(lista)

# Insira na lista um novo item

lista.append('papagaio')
print(lista)

# Remova da lista um item específico

lista.remove(True)
print(lista)