'''Crie um programa para aprovar o emprestimo bancario da compra de uma casa 
Pergunte o valor da casa o salario do comprador e em quantos anos ele vai pagar.
A prestacao mensal nao podera exceder 30% do valor do salario ou entao o emprestimo sera negado'''

try:
    casa = float(input('Valor da casa: R$'))
    salario = float(input('Salario do comprador: '))
    anos = int(input('Quantos anos de financiamento: '))
    prestacao = casa / (anos * 12)
    minimo = salario * (30/100)
    print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestacao sera de R${prestacao:.2f} ')
    if prestacao > minimo:
        print('Emprestimo NEGADO!')
    else:
        print('Emprestimo CONCEDIDO!')
except ValueError:
    print('Favor digitar um valor valido')