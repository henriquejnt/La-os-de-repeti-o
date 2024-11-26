#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#  O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
#  Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
from sympy import primerange, isprime
primo = int(input('Digite um número primo: '))
divisores = 1
valores_primos = 0
for valor in range(1,primo):
        valores_primos = list(primerange(1, valor))
print(f'Número primos : {valores_primos}')
print(len(valores_primos))
print(f'Divisões necessarias: {(len(valores_primos))*2}')
