from colorama import init
from colorama import Fore
init(autoreset=True)
radar = input('Qual a velocidade atual do Carro? ')
velocidade_max = 80
valor_multa = 7 

try:
    radar = int(radar)
    if radar > velocidade_max:
        print(Fore.RED + f'MULTADO! Vc execeu o limite permitido que e de 80Km/h. Vc deve pagar uma multa de', 
              Fore.YELLOW + f'R${(radar - velocidade_max) * valor_multa:.2f}!')
    print(Fore.YELLOW + 'Tenha um bom dia! Dirija com seguranca')
except ValueError:
    print('Favor digitar um valor valido')

