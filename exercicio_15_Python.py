dias = input('Quantos dias alugados? ')
km = input('Quantos Km rodados? ')

try:
    resultado = (int(dias) * 60) +(int(km) * 0.15)
    print(f'O total a pagar e de R$ {resultado}')
except ValueError:
    print('Favor digitar um valor inteiro')
