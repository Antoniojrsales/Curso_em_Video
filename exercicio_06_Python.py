numero = int(input('Digite um numero: '))
print(f'O Dobro de {numero} Vale {numero * 2}')
print(f'O Triplo de {numero} Vale {numero * 3}')
print(f'O Raiz de {numero} Vale {numero ** (1/2):.2f}')

'''Criando uma funcao para verificar o exer. com tratamento de erro

def dobro(num):
    print(f'O Dobro de {num} é = {num * 2}')
    print(f'O Triplo de {num} é = {num * 3}')
    print(f'O Raiz de {num} é = {num ** (1/2):.2f}')

while True:
    print('Digite [s/S] para finalizar o programa')
    numero = input('Digite um numero: ')
    if numero == 'S' or numero == 's':
        print('Programa finalizado')
        break
    elif numero.isdigit():
        numero_int = int(numero)
        dobro(numero_int)
    else:
        print('Vc digitou um valor invalido ou nao digitou nada')
        print('Favor digitar um valor valido')
        continue'''

'''Obtendo um script mais estruturado

def dobro(num):
    print(f'O Dobro de {num} é = {num * 2}')
    print(f'O Triplo de {num} é = {num * 3}')
    print(f'A Raiz de {num} é = {num ** (1/2):.2f}')

while True:
    print('Digite [S] para finalizar o programa')
    numero = input('Digite um número: ').strip()
    
    # Verifica se o usuário quer sair
    if numero.upper() == 'S':
        print('Programa finalizado.')
        break

    # Verifica se o valor é um número
    try:
        numero_float = float(numero)
        dobro(numero_float)
    except ValueError:
        print('Valor inválido! Por favor, digite um número válido.')'''