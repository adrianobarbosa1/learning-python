i=1
while i<=100:
    print(i)
    i = i+1

total = 0
continuar = "s"

while continuar == "s":
    valor = float(input("Digite o valor da compra: \n"))
    total = total + valor

    continuar = input("Deseja continuar? (s/n)")

print("valor total da compra: ", total)