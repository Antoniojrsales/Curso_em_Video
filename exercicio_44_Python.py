'''Crie um programa que calcule o valor a ser pago por um produto
-A vista: dinheiro/pix 10% de desconto
-A vista no cartao: 5% de desconto
-2x no cartao: preco normal
-3x ou mais no cartao : 20% de juros
'''

print('='*7,'LOJAS GUANABARA','='*7)
preco = float(input('Preco da(s) Compra(s): '))
print('Formas de Pagamento\n'
      '[1] a vista dinheiro ou pix\n'
      '[2] a vista no cartao\n'
      '[3] 2x no cartao\n'
      '[4] 3x ou mais no cartao')
pagamento = int(input('Qual e a opcao? '))

if pagamento == 1:
    print(f'Sua compra de R${preco:.2f} vai custar R${preco - (preco * 10 / 100):.2f} no final ')
elif pagamento == 2:
    print(f'Sua compra de R${preco:.2f} vai custar R${preco - (preco * 5 / 100):.2f} no final ')
elif pagamento == 3:
    print(f'sua compra sera parcelada em 2x de R${preco/2:.2f} SEM JUROS')
    print(f'Sua compra vai custar R${preco:.2f} final ')
else:
    quant_parcelas = int(input('Quantas parcelas? '))
    print(f'sua compra sera parcelada em {quant_parcelas}x de '
          f'R${(preco + (preco * 20 / 100)) / quant_parcelas:.2f} COM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${preco + (preco * 20 / 100):.2f} no final ')