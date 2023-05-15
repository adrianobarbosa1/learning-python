# 1. “FizzBuzz” é um problema clássico de programação. O programa recebe um
# número inteiro e imprime:
# a. “Fizz", caso o número seja múltiplo de 3.
# b. “Buzz", caso o número seja múltiplo de 5.
# c. “FizzBuzz", caso o número seja múltiplo de 3 e de 5.
# Por exemplo:
# 3 -> "Fizz" (múltiplo de 3)
# 8 -> ... (não imprime nada)
# 10 -> "Buzz" (múltiplo de 5)
# 15 -> "FizzBuzz" (múltiplo de 3 e 5)
# 21 -> "Fizz"
# Implemente o programa FizzBuzz.


# numero = float(input("digite o numero: \n"))

# if numero % 3 == 0 and numero % 5 == 0:
#     print("FizzBuzz")
# elif numero % 5 == 0:
#     print("Buzz")
# elif numero % 3 == 0:
#     print("Fizz")
# else:
#     print('não é multiplo de 3 ou 5')

# 2. Implemente uma calculadora que recebe 3 valores do usuário:
# a. Operando a (pode ser um inteiro ou float).
# b. Operando b (pode ser um inteiro ou float).
# c. Operador op .
# i. op pode ser uma string representando o operador, por exemplo, "+" ou "-
# ". Outra opção é utilizar números, por exemplo, 1 para soma , 2 para
# subtração , etc.
# O seu programa deve receber esses 3 valores e imprimir o resultado da operação.
# Caso o operador seja de divisão e o segundo operando seja o valor zero, o
# programa deve imprimir uma mensagem: “Não é possível realizar divisão por
# zero!”.

# a = float(input("Digite o primeiro numero: \n"))
# op = input("Digite o operador")
# b = float(input("Digite o segundo numero: \n"))
# total = 0

# if op == "-":
#     total = a - b
#     print("Resultado: ", total)
# elif op == "+":
#     total = a + b
#     print("Resultado: ", total)
# elif op == "*":
#     total = a * b
#     print("Resultado: ", total)
# elif op == "/" and b != 0:
#     total = a / b
#     print("Resultado: ", total)
# elif op == "/" and b == 0:
#     print("Não é possível realizar divisão por zero!")


# 3. Escreva um programa de autenticação que receba um nome de usuário e senha
# ( input ) informe se:
# Exercícios – Controle de Fluxo 2
# Autenticação foi bem-sucedida.
# Se o nome de usuário não existe.
# Se a senha está incorreta.
# Os valores corretos de nome de usuário e senha devem estar armazenados em
# constantes, como no exemplo abaixo:
# USUARIO = "admin"
# SENHA = "123123"
# nome_usuario = input("Digite o nome do usuário: "\n)

# USUARIO = "adriano"
# SENHA = "123456"

# usuario = input("Digite o usuario: \n")
# password = input("Digite a senha: \n")

# if usuario == USUARIO and password == SENHA:
#     print("authenticação bem sucedida")
# else:
#     print("usuario não existe ou senha incorreta")

numero = 4
tentativa = 0

while tentativa < 3:
    numero_tentado = int(input("Digite a tentativa: "))
    tentativa = tentativa + 1

    if numero_tentado < numero:
        print("você errou, dica o numero colocado foi menor que o segredo")
    elif numero_tentado == numero:
        print("você acertou")
    elif numero_tentado > numero:
        print("você errou, dica o numero colocado fou maior que o segredo")

print("acabou as tentativas")