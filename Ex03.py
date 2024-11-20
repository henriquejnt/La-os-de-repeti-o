#Supondo que a população de um país A seja da ordem de 80000 habitantes 
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
#  com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número
#  de anos necessários para que a população do país A ultrapasse ou iguale a população do 
# país B, mantidas as taxas de crescimento.
pais_A = 80000
pais_B = 200000
contador_anos = 0
crescimento_A = (3/100)+1
crescimento_B = (1.5/100)+1
while pais_A < pais_B:
    pais_A *= crescimento_A 
    pais_B *= crescimento_B
    contador_anos += 1
    print('=-'*15)
    print(f'############ Em {contador_anos} anos país A e B ficará:')
    print(f'População de A: {int(pais_A)}')
    print(f'Aumento de {crescimento_A}% no crescimento de A.')
    print('-'*15)
    print(f'População de B: {int(pais_B)}')
    print(f'Aumento de {crescimento_B}% no crescimento de B.')

