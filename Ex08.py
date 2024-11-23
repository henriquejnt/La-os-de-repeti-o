#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e 
# limitando o fatorial a números inteiros positivos e menores que 16.Altere o programa de cálculo do fatorial, 
# permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e
#  menores que 16.
#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

while True:
    fatorial = int(input('Digite um valor para calcular seu fatorial: '))
    calculo = 1
    print(f'{fatorial}! = ', end=' ')
    for valor in range(1, fatorial+1):
        calculo *= valor
        print(f"{valor}", end=". ")
    print("=",calculo)
    s_n = input("Quer continuar? [Sim/Não]").upper()
    while s_n != 'SIM' and  s_n != 'NÃO':
        s_n = input("Quer continuar? [Sim/Não]").upper()
    if s_n == 'NÃO':
        break
print('Programa encerrado !')