# def e_primo(numero):
#     if numero < 2:
#         print("False")
#         return False

#     for i in range(2, int(numero**0.5) + 1):
#         if numero % i == 0:
#             print("False")
#             return False
#     print('True')
#     return True

# e_primo(3)

def maior_numero__da_lista(lista):
    if not lista:
        return None
    
    maior = lista[0]

    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            posicao = i

    return (posicao, maior)


valor = maior_numero__da_lista([1, 10, 5, 8])
print(valor)