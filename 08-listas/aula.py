notas = [10, 10, 10]
print("LISTA PRINCIPAL: \n",notas)

#adicionar na lista
notas.append(9)
print("ADIONCADO: \n",notas)

#ordenar a lista
notas.sort()
print("ORDERNADO: \n",notas)

#ordenar de forma decrescente
notas.sort(reverse=True)
print("ORDENAR DECRESCENTE: \n",notas)

#remover elemento da lista
notas.pop() #por padrão remove o ultimo elemento
notas.pop(0) #posição a ser removida

# inserir na lista
notas.insert(0,8) #primeiro parametro posição, segundo o valor a ser inserido

i = 0
total = 0
qtd = len(notas)

while i < qtd:
    total = total + notas[i]
    i = i + 1
    print(total)
