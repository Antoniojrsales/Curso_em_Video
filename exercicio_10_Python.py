dinheiro = input('Quanto de dinheiro vc tem na carteira? R$ ')
try:
    dinheiro = float(dinheiro)
    conversao = dinheiro / 5.15
    print(f'Com R${dinheiro} vc pode comprar U$${conversao:.2f} ')
except ValueError:
    print('Vc nao digitou um valor valido favor digitar um valor valido')