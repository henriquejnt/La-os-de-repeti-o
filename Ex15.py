#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido
valor = int(input("Digite um valor inteiro positivo: "))
while valor <= 0:
    print("ERROR, tente novamente !")
    valor = int(input("Digite um valor inteiro positivo: "))
for valor in range(valor, 0, -1):
    print(valor, end=",")