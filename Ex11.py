#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
#  mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser 
# informados também pelo usuário.

num = int(input('Número de sua tabuada: '))
inicia = int(input('Inicia: '))
termina = int(input('Termina: '))
while termina < inicia:
    termina = int(input('Termina: '))
    if termina > inicia:
        break
for tabuada in range(inicia,termina+1):
    print(f'{num} x {tabuada} = {num*tabuada}')