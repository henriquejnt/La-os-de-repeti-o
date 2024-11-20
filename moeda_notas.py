#Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. 
# A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
# A seguir mostre a relação de notas necessárias.
valor = 3456.64
valor_inteiro = int(valor)
nota_100 = int(valor //100)
nota_50 = int(valor - nota_100*100) // 50
nota_20 = int((valor - nota_100*100) - nota_50*50) // 20
nota_10 = int(((valor - nota_100*100) - nota_50*50) - nota_20*20) // 10
nota_5 = int((((valor - nota_100*100) - nota_50*50) - nota_20*20) - nota_10 *10) // 5
nota_2 = int(((((valor - nota_100*100) - nota_50*50) - nota_20*20) - nota_10 *10) - nota_5*5) // 2
moeda_1 = int((((((valor - nota_100*100) - nota_50*50) - nota_20*20) - nota_10 *10) - nota_5*5) - nota_2*2) // 1
moeda_meia= (valor - valor_inteiro) // 0.50
moeda_vinte_cinco = ((valor - valor_inteiro) - moeda_meia*0.50) // 0.25
moeda_10 = (((valor - valor_inteiro) - moeda_meia*0.50) - moeda_vinte_cinco*0.25) // 0.10
moeda_005 = ((((valor - valor_inteiro) - moeda_meia*0.50) - moeda_vinte_cinco*0.25) - moeda_10 *0.10)// 0.05
moeda_001 = (((((valor - valor_inteiro) - moeda_meia*0.50) - moeda_vinte_cinco*0.25) - moeda_10 *0.10)- moeda_005*0.05) //0.01
print(moeda_1)
print(f"{moeda_meia} 0.50 centavos")
print(f"{moeda_vinte_cinco} 0.25 centavos")
print(f'{moeda_10} 0.10 centavos')
print(f'{moeda_005} 0.05 centavos ')
print(f'{moeda_001} 0.01 centavos')
print("NOTAS:")
if nota_100 > 0:
    print(f"{nota_100} notas de R$100")
if nota_50 > 0:
    print(f"{nota_50} notas de R$50")
if nota_20 > 0:
    print(f"{nota_20} notas de R$20")
if nota_10 >0:
    print(f"{nota_10} notas de R$ 10")
if nota_5 > 0:
    print(f"{nota_5} notas de R$5")
if nota_2 > 0:
    print(f'{nota_2} notas de R$2')
if moeda_1 > 0:
    print(f'{moeda_1} moedas de R$1')
if moeda_meia > 0.00:
    print(f"{moeda_meia} moedas de R$0.50")
if moeda_vinte_cinco > 0.00:
    print(f"{moeda_vinte_cinco} moedas de R$0.25")
if moeda_10 >0.00:
    print(f"{moeda_10} moedas de R$0.10 ")
if moeda_005 > 0.00:
    print(f"{moeda_005} moedas de R$0.05")
if moeda_001 > 0.00:
    print(f"{moeda_001} moedas de R$0.01")