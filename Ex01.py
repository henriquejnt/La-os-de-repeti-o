#Faça um programa que peça uma nota, entre zero e dez.
#  Mostre uma mensagem caso o valor seja inválido e continue pedindo até 
# que o usuário informe um valor válido.

while True:
    try:
        nota = int(input("Digite uma nota de 0 ate 10: "))
    except ValueError:
        print('Deve ser número inteiro !')
    else:
        if nota > 0 and nota <= 10:
            print(f'Número informado: {nota}')
            break
        else:
            print('O número deve ser entre 0 e 10 !')
