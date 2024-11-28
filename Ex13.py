#O cardápio de uma lanchonete é o seguinte:
#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a 
# ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando
#  o pedido deve ser encerrado. EXERCICIO 43
valor_pago100 = valor_pago101 = valor_pago102 = valor_pago103 = valor_pago104 = valor_pago105 = 0
quant100 = quant101 = quant102 = quant103 = quant104 = quant105 = 0
valor_total = 0
while True:
    print('''O cardápio de uma lanchonete é o seguinte:
        Especificação   Código  Preço
        Cachorro Quente 100     R$ 1,20
        Bauru Simples   101     R$ 1,30
        Bauru com ovo   102     R$ 1,50
        Hambúrguer      103     R$ 1,20
        Cheeseburguer   104     R$ 1,30
        Refrigerante    105     R$ 1,00''')
    codigo = int(input('Código do item: '))
    #se cod > 1005
    if codigo > 105 or codigo < 100:
        while codigo > 105 or codigo < 100:
            print('Tente novamente:')
            codigo = int(input('Código do item: '))
    quantidades = int(input("Quantidade desejada do produto: ")) 
    if codigo == 100:
        valor_pago100 = 1.20
        quant100 += quantidades
        valor_total += valor_pago100 * quantidades
    elif codigo == 101:
        valor_pago101 = 1.30
        quant101 += quantidades
        valor_total += valor_pago101 * quantidades
    elif codigo == 102:
        valor_pago102 = 1.50
        quant102 += quantidades
        valor_total += valor_pago102 * quantidades
    elif codigo == 103:
        valor_pago103 = 1.20
        quant103 += quantidades
        valor_total += valor_pago103 * quantidades
    elif codigo == 104:
        valor_pago104 = 1.30
        quant104 += quantidades
        valor_total += valor_pago104 * quantidades
    elif codigo == 105:
        valor_pago105 = 1.00
        quant105 += quantidades
        valor_total += valor_pago105 * quantidades
    #verificação sim ou não
    print('=-'*20)
    s_n = input('Quer continuar? [S/N]: ').upper()
    while s_n != 'S' and s_n != 'N':
        print("Tente novamente !")
        s_n = input('Quer continuar? [S/N]: ').upper()
    if s_n == 'N':
        break
print('='*35)
print("PEDIDOS:")
if valor_pago100 == 1.20:
    print(f'-Cachorro Quente, valor:R$ 1.20 , quantidades:{quant100} -> VALOR A PAGAR R${quant100*valor_pago100}')
if valor_pago101 == 1.30:
    print(f'-Bauru Simples, valor:R$ 1.30 , quantidades:{quant101} -> VALOR A PAGAR R${quant101*valor_pago101}')
if valor_pago102 == 1.50:
    print(f'-Bauru com ovo, valor:R$ 1.50 , quantidades:{quant102} -> VALOR A PAGAR R${quant102*valor_pago102}')
if valor_pago103 == 1.20:
    print(f'-Hambúrguer , valor:R$ 1.20 , quantidades:{quant103} -> VALOR A PAGAR R${quant103*valor_pago103}')
if valor_pago104 == 1.30:
    print(f'-Cheeseburguer , valor:R$ 1.30 , quantidades:{quant104} -> VALOR A PAGAR R${quant104*valor_pago104}')
if valor_pago105 == 1.00:
    print(f'-Refrigerante , valor:R$ 1.00 , quantidades:{quant105} -> VALOR A PAGAR R${quant105*valor_pago105}')
print(f"VALOR TOTAL A PAGAR: R${valor_total}")





