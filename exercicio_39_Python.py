'''Crie um programa que leia o ano de nascimento de um jovem e informe de acordo 
com sua idade se ele ainda vai se alistar ao servico militar se e hora de se alistar 
ou seja ja passou do alistamento o seu programa tambem deverar mostrar o tempoque falta 
ou que passou do prazo'''

from datetime import date

ano_atual = date.today().year
alistamento = 18

while True:
    ano_nasc = input('Ano de nascimento: ')
    if ano_nasc.isdigit():
        ano_nasc = int(ano_nasc)
        if ano_nasc < 1900 or ano_nasc >= ano_atual:
            print('Favor digitar um Ano valido')
            continue
    else:
        print('Vc digitou uma letra ou nao digitou nada.\n'
              'Seu programa sera Finalizado')
        break

    resultado = ano_atual - ano_nasc
    print(f'Quem nasceu em {ano_nasc} tem {resultado} anos em {ano_atual}')

    if resultado == 18:
        print(f'Vc tem que se alistar IMEDIATAMENTE')
    elif resultado < 18:
        print(f'Ainda faltam {alistamento - resultado} anos para o seu alistamento')
        print(f'Seu alistamento sera em {ano_atual + (alistamento - resultado)}')
    elif resultado > 18:
        print(f'Vc ja deveria ter se alistado ha {resultado - alistamento} anos')
        print(f'Seu alistamento foi em {ano_atual - (resultado - alistamento)}')
    