#Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
media = 0
for valor in range(1, 6):
    n1 = float(input(f'Digite o {valor} valor: '))
    soma += n1
media = soma / 5
print(f'A média é {media} e a soma é {soma}')
