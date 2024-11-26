#Faça um programa que calcule o mostre a média aritmética de N notas.
quantidade_num = 0
soma_n1 = 0
while True:
    n1 = float(input(f'Digite o {quantidade_num+1} valor: '))
    soma_n1 += n1
    quantidade_num +=1
    s_n = input('Quer continuar? [S/N] ').upper()
    while s_n != 'S' and s_n != 'N':
        print('Tente novamente !')
        s_n = input('Quer continuar? [S/N] ').upper()
    if s_n == 'N':
        break
print(f'A média aritmetica dos valores é de {soma_n1 / quantidade_num}')