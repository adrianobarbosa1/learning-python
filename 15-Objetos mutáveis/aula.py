# objetos mutáveis

# Em Python, um objeto mutável é um objeto cujo estado pode ser alterado após sua criação. Isso significa que você pode modificar diretamente os valores dos atributos de um objeto mutável sem criar um novo objeto.

# Aqui estão alguns exemplos de objetos mutáveis em Python:

# Listas Mutáveis: As listas são uma das estruturas de dados mais comumente usadas em Python e são objetos mutáveis. Você pode adicionar, remover, modificar ou reordenar elementos em uma lista. Por exemplo:
# python
# Copy code
# lista = [1, 2, 3]
# lista.append(4)  # Adiciona o número 4 à lista existente
# lista[0] = 10  # Modifica o primeiro elemento da lista para 10
# Dicionários Mutáveis: Os dicionários em Python são estruturas de dados que armazenam pares chave-valor e são objetos mutáveis. Você pode adicionar, remover ou modificar pares chave-valor em um dicionário. Por exemplo:
# python
# Copy code
# dicionario = {'a': 1, 'b': 2, 'c': 3}
# dicionario['d'] = 4  # Adiciona um novo par chave-valor ao dicionário
# dicionario['a'] = 10  # Modifica o valor associado à chave 'a'
# Conjuntos Mutáveis: Os conjuntos em Python são coleções não ordenadas de elementos únicos e são objetos mutáveis. Você pode adicionar, remover ou modificar elementos em um conjunto. Por exemplo:
# python
# Copy code
# conjunto = {1, 2, 3}
# conjunto.add(4)  # Adiciona o número 4 ao conjunto existente
# conjunto.remove(2)  # Remove o número 2 do conjunto
# Arrays Mutáveis: O módulo array em Python fornece um tipo de objeto de array mutável que permite armazenar elementos do mesmo tipo. Você pode modificar diretamente os valores dos elementos em um array. Por exemplo:
# python
# Copy code
# import array

# arr = array.array('i', [1, 2, 3, 4])
# arr[0] = 10  # Modifica o primeiro elemento do array para 10
# É importante ter em mente que, ao trabalhar com objetos mutáveis, as alterações feitas em uma variável que faz referência ao objeto afetam o objeto em si, não criam um novo objeto. Portanto, é necessário tomar cuidado ao lidar com objetos mutáveis para garantir que as modificações ocorram conforme o desejado.