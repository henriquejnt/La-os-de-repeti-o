#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos 
# seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido
#  um número negativo.
primeiro_intervalo = 0
segun_intervalo = 0
terce_intervalo = 0
quart_intervalo = 0
while True:
    try:
        num = int(input('Digite um valor positivo (número negativo p/ sair): '))
    except ValueError:
        print("Deve ser número inteiro !")
    else:
        if num < 0:
            break
        else:
            if num >= 0 and num <=25:#[0-25]
                primeiro_intervalo += 1
            elif num >= 26 and num <= 50: #[26-50]
                segun_intervalo +=1
            elif num >= 51 and num <= 75:#[51-75]
                terce_intervalo += 1
            elif num >= 76 and num <= 100:#[76-100]
                quart_intervalo += 1
print(f"Estão apenas {primeiro_intervalo} valores entre [0-25].")
print(f"Estão apenas {segun_intervalo} valores entre [26-50].")
print(f"Estão apenas {terce_intervalo} valores entre [51-75].")
print(f"Estão apenas {quart_intervalo} valores entre [76-100].")
