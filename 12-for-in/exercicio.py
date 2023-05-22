# 1. Escreva um programa que lê números inteiros positivos do usuário, um após o
# outro, e monta uma lista a partir desses números e depois imprime a lista montada.
# O programa deve continuar solicitando por números até que o elemento digitado
# seja um número negativo (que não deve ser inserido na lista).


# numeros = []


# while True:
#     numero = int(input("Digite um numero inteiro para continuar e negativo para acabar: \n"))

#     if numero < 0:
#         break

#     numeros.append(numero)
    
# print("lista de numeros: \n",numeros)


# 2. Dada uma lista de números inteiros, escreva um programa que calcula a soma de
# todos os números na lista.
# Se preferir, pode utilizar a lista abaixo como exemplo:
# lista = [1, 10, 20, 35, 22, 12]
# Resultado deve ser = 100

# lista = [1, 10, 20, 35, 22, 12]
# soma = 0
# for numero in lista:
#     soma = numero + soma

# print(soma)

# 3. Data uma lista de números inteiros, escreva um programa que calcula a média dos
# números na lista. O resultado não deve incluir números decimais. Exemplo: 12.3
# deve imprimir apenas 12 .
# Se preferir, pode utilizar a lista abaixo como exemplo:
# lista = [1, 10, 20, 35, 22, 12]
# # Resultado deve ser 16
# P.S.: Pode utilizar o operador // (divisão inteira)

# lista = [1, 10, 20, 35, 22, 12]
# soma = 0
# for numero in lista:
#     soma = numero + soma

# media = soma // len(lista)

# print(media)

# 4. Suponha o seguinte programa:
# # Alunos e suas respectivas notas
# alunos = [
# ("Alice", 8),
# ("Bob", 7),
# ("Carlos", 9),
# ]
# Escreva uma programa que calcula a média das notas de todos os alunos.

# alunos = [
# ("Alice", 8),
# ("Bob", 7),
# ("Carlos", 9),
# ]

# soma = 0
# for aluno in alunos:
#     nome, nota = aluno
#     soma = nota + soma

# media = soma // len(alunos)

# print(media)

# 5. Suponha o seguinte programa:
# Exercícios – Estruturas de dados 2
# # Alunos e suas notas representados através de dicionários
# alunos = [
# {
# "nome": "Alice",
# "nota": 8,
# },
# {
# "nome": "Bob",
# "nota": 7,
# },
# {
# "nome": "Carlos",
# "nota": 9,
# }
# ]
# Escreva uma programa que calcula a média das notas de todos os alunos.

# alunos = [
# {
# "nome": "Alice",
# "nota": 8,
# },
# {
# "nome": "Bob",
# "nota": 7,
# },
# {
# "nome": "Carlos",
# "nota": 9,
# }
# ]
# soma = 0
# for aluno in alunos:
#     soma = aluno["nota"] + soma
    
# media = soma // len(alunos)

# print(media)

# 6. DESAFIO. Escreva um programa que dado uma lista de números inteiros, imprime
# o maior número dessa lista.
# lista = [1, 3, 2, 5]

# Deve imprimir 5

# lista = [1, 3, 2, 5]

# print(max(lista, key=int))

# Escreva um programa que solicite uma string para o usuário e imprima quantas
# vezes cada letra aparece na palavra. Por exemplo:
# "banana"
# # O resultado deve ser
# {
# 'a': 3,
# 'b': 1,
# Exercícios – Estruturas de dados 3
# 'n': 2
# }

# palavra = input("digite a palavra: \n")

# contagem = {}
# for letra in palavra:
#     if letra in contagem:
#         print(contagem)
#         contagem[letra] += 1
#     else:
#         contagem[letra] = 1
     
# print(contagem)

# 8. DESAFIO. Escreva um programa que declara uma lista com elementos de
# diferentes tipos e imprime na tela essa lista invertida. Não é permitido utilizar
# métodos como reverse ou sort .
# def inverte_lista(lista):
# ...
# lista = ["a", 5, {1}]
# lista_invertida = inverte_lista(lista)
# print(lista_invertida)
# [{1}, 5, "a"]

# lista = ["a", 5, {1}]

# lista_invertida = []
# for i in range(len(lista) - 1, -1, -1):
#     lista_invertida.append(lista[i])

# print("Lista invertida:")
# print(lista_invertida)