custo = float(input('Qual e a distancia da sua viagem: '))
print(f'Voce esta prestes a comecar uma viagem de {custo:.1f}Km')
if custo <= 200:
    print(f'E o preco da sua viagem sera de R${custo * 0.5:.2f}')
else:
    print(f'E o preco da sua viagem sera de R${custo * 0.45:.2f}') 