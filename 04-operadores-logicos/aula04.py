# not inverte o valor
idade = 16
maior_de_idade = idade >= 18 #retorno false
maior_de_idade = not maior_de_idade #retorno true

# and os valores tem q ser verdadeiro
usuario = True
senha = True
sucesso = usuario and senha #retorno verdadeiro

# or um dos valores tem que ser verdadeiro
idade = 16
idade_minima = 16
acompanhada_pelos_pais = True

#retorno true
pode_assistir = idade >= idade_minima or acompanhada_pelos_pais 