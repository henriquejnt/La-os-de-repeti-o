#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

fatorial = int(input('Digite um valor para calcular seu fatorial: '))
calculo = 1
print(f'{fatorial}! = ', end=' ')
for valor in range(1, fatorial+1):
    calculo *= valor
    print(f"{valor}", end=". ")
print("=",calculo)