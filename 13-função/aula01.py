# função retornando valor

def calcular_conta(consumo, taxa, desconto_fidelidade):
    servico = consumo * taxa
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto
    return valor

valor = calcular_conta(consumo=200, taxa=0.1, desconto_fidelidade=0.5)
print(valor)

# valores padrões
#valores padrão são passados nos parametros
def calcular_comanda(consumo, taxa=0.1, desconto_fidelidade=0):
    servico = consumo * taxa
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto
    return valor

#caso não seja especificado o valor do segundo e terceiro
#parametro, a função assumi o valor padrão
valor2 = calcular_comanda(consumo=20)