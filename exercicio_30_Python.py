from colorama import init
from colorama import Fore
init(autoreset=True)

numero = input('Me diga um numero qualquer: ')

try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O numero {numero} e', Fore.BLUE + 'PAR')
    else:
        print(f'O numero {numero} e', Fore.RED + 'IMPAR')
except ValueError:
    print('Digite um valor valido')