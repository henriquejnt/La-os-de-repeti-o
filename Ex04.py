#Faça um programa que leia 5 números e informe o maior número.
contador = 0
maior = 0
for valor in range(1, 6):
    while True:
        try:
            n1 = float(input(f'Digite o {valor}: '))
        except ValueError:
            print('Digite um valor inteiro !')
        else:
            break
    contador += 1
    if contador == 1:
        maior = n1
    elif contador ==2 or contador > 2:
        if n1 > maior: 
            maior = n1 # 100
print(f"O maior valor é {maior}")
    

        