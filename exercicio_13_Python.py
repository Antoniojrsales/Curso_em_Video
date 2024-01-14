salario = float(input('Qual e o salario do funcionario R$: '))
aumento = salario + (salario * 15/100)
print(f'Um funcionario que ganhava R${salario} com 15% de aumento passa a receber R${aumento:.2f}')