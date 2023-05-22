# objetos imutaveis

# Em Python, um objeto imutável é um objeto cujo estado não pode ser alterado após sua criação. Isso significa que, uma vez que um objeto imutável é criado, seus valores não podem ser modificados. Em vez disso, qualquer operação que pareça modificar o objeto cria um novo objeto com o valor modificado.

# Aqui estão alguns exemplos de objetos imutáveis em Python:

# Números Imutáveis: Os números inteiros (int), números de ponto flutuante (float) e números complexos (complex) são imutáveis em Python. Por exemplo:
# python
# Copy code
# x = 10
# x += 5  # Isso cria um novo objeto com o valor 15
# Strings Imutáveis: As strings em Python são objetos imutáveis. Depois de criar uma string, você não pode modificar seu conteúdo. Em vez disso, você precisa criar uma nova string com as modificações desejadas. Por exemplo:
# python
# Copy code
# s = "Olá"
# s += " mundo"  # Isso cria uma nova string "Olá mundo"
# Tuplas Imutáveis: As tuplas são sequências imutáveis de objetos em Python. Uma vez que uma tupla é criada, seus elementos não podem ser alterados. No entanto, é possível criar uma nova tupla combinando ou fatiando tuplas existentes. Por exemplo:
# python
# Copy code
# t = (1, 2, 3)
# t += (4, 5)  # Isso cria uma nova tupla (1, 2, 3, 4, 5)
# Frozensets Imutáveis: O tipo frozenset em Python é uma versão imutável do tipo set. Um frozenset pode ser usado como chave em um dicionário porque é imutável. No entanto, assim como os sets, você não pode modificar diretamente um frozenset após a criação.
# python
# Copy code
# fs = frozenset([1, 2, 3])
# fs.add(4)  # Isso resultará em um erro, já que um frozenset é imutável
# É importante observar que objetos imutáveis podem ser usados de maneira eficiente em Python, pois a criação de um novo objeto, em vez de modificação direta, é geralmente otimizada para minimizar o uso de memória.