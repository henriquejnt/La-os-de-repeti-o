while True:
    acumulador = 0
    maior_menor = []
    print('=-'*20)
    nome_atleta = input('Nome do atleta: ')
    if nome_atleta == "":
        break
    else:
        for salto in range(5):
            acumulador += 1
            saltos = float(input(f"{acumulador} salto: "))
            maior_menor.append(saltos)
    maior_menor.remove(max(maior_menor))
    maior_menor.remove(min(maior_menor))
    maior = max(maior_menor)
    menor = min(maior_menor)
    media = sum(maior_menor)/3
    print(f"Melhor salto: {maior}")
    print(f"Pior salto: {menor}")
    print(f"Média dos demais saltos: {media:.2f}")
    print('=-'*15)
    print('Resultado final:')
    print(f"{nome_atleta}: {media:.2f}m")