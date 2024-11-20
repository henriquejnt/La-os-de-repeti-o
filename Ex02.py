#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome = input('Digite seu nome: ')
    senha = input("Sua senha: ")
    if nome == senha:
        print('=-'*25)
        print('ERROR !')
        print("Não pode as duas serem iguais !")
    else:
        print('=-'*25)
        print("Nome e senha cadastrados !")
        break
