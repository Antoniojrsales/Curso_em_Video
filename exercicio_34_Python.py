'''Crie um programa que pergunte o salario de um funcionario
e calcule o valor do seu aumento.
Para salarios acima de R$ 1250,00 calcule o aumento de 10%
Para salarios -= a R$ 1250,00 calcule o aumento de 15%'''

salario = float(input('Qual o salario do funcionario? R$'))

if salario > 1250:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario + (salario * 10/100):.2f} agora')
else:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario + (salario * 15/100):.2f} agora')