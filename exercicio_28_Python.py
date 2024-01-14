import random
from colorama import init
from colorama import Fore
from time import sleep
init(autoreset=True)
computador = random.randint(0, 5)
print('-#'*27)
print(Fore.BLUE + 'Vou pensar em um numero entre 0 a 5, Tente Adivinhar... ')
print('-#'*27)
jogador = int(input('Digite o numero escolhido: '))
print('PROCESSANDO...')
sleep(2)
print()
if jogador == computador:
    print(Fore.YELLOW + 'Parabens vc conseguiu me vencer')
else:
    print(Fore.RED + f'GANHEI! Eu pensei no numero {computador} e nao no numero {jogador}')

