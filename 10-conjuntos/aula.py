#conjuntos
usuarios = {"alice", "bob"}

#conjuntos tmb pode ser representados por listas
#usando o comando set vc tranforma a lista em um conjunto
usuarios_2 = set(["alice", "bob"]) 

#conjuntos não podem ter elementos repetidos
#numero = { 2, 2, 4}

# para adionar um elemento no conjunto usamos add()
usuarios.add("anderson")

#conjuntos não garatem ordenação de elementos
#pode-se agrupar conjuntos com o comando union()
# ou o pipe
usuarios.union(usuarios_2)
usuarios | usuarios_2

#interceção mostrando os mesmos elementos em dois
#conjuntos, comando intersection() ou &
usuarios.intersection(usuarios_2)
usuarios & usuarios_2

#diferenças entre os conjuntos com o comando 
#difference ou sinal de -
usuarios.difference(usuarios_2)
usuarios - usuarios_2