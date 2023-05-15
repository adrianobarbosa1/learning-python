# 1. Escreva um programa que contenha 4 variáveis e que imprima na tela o tipo de
# cada uma delas. A saída do seu programa deve ser na seguinte ordem:
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>

palavras = "ola"
numero = 2
numeroqubrado = 2.5
boleano = True

print(type(palavras))
print(type(numero))
print(type(numeroqubrado))
print(type(boleano))


# 2. Escreva um programa com as seguintes especificações:
#   - Uma variável “valor_compras” que receba um valor do tipo float, representando
#   o valor total das compras.
#   - Uma variável “desconto” que receba um valor do tipo float, representando o
#   desconto a ser aplicado sobre o valor total das compras.
#   - Uma variável “quantidade_itens”, que represente a quantidade de itens que
#   foram comprados.
# Seu programa deve imprimir dois resultados:
# 1. O valor final das compras, considerando o desconto aplicado.
# 2. O custo médio de cada item (considerando o valor final das compras).

valor_compras = 5.5
desconto = valor_compras * 0.1
total = valor_compras - desconto
quantidade_itens = 2

print("Valor final das compras: " + str((total)))
print("Custo medio de cada item: " + str((quantidade_itens / total )))