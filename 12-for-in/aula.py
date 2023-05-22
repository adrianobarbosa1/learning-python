# for in
# pode usar o FOR IN em dicionarios, conjuntos, listas e tuplas

notas = [8, 9, 10]

for nota in notas:
    print(nota)

# iterando pelo conjunto
notas_conjunto = {7, 8, 9} 

# apesar de o conjunto não funcionar com while, 
# ele funriona com o FOR IN
for nota in notas_conjunto:
    print(nota)

#dicionario
# dict.keys() especifica apenas as chaves
# dict.value() especifica apenas valores
# dict.items() especifica os dois
notas_dicionario = {
    "alice" : 10,
    "adriano": 11,
    "jhon do": 9
}

for nota in notas_dicionario.items():
    print(nota)

for k, v in notas_dicionario.items():
    print(k, v)