'''A Confererancao Nacional de Natacao precisa de um programa que leia o ano de nascimento 
de um atleta e mostre sua categoria
-Ate 9 anos: MIRIM
-Ate 14 anos: INFANTIL
-Ate 19 anos: JUNIOR
-Ate 25 anos: SENIOR
-Acima: MASTER'''

from datetime import date

while True:
    print('Favor digitar o ano do atleta ou [F] ou [f] para finalizar o programa')
    ano_nasc = input('Ano de Nascimento: ').lower()
    ano_atual = date.today().year
    
    if ano_nasc == 'f':
        print('Fim do programam')
        break

    if ano_nasc.isdigit():
        ano_nasc = int(ano_nasc)
        idade_atual = ano_atual - ano_nasc
        if ano_nasc >= ano_atual:
            print('Vc digitou algo errado favor digitar um ano valido')
            continue
        print(f'O atleta tem {idade_atual} anos.')
        if idade_atual <= 9:
            print('Classificacao: MIRIM')
        elif idade_atual <= 14:
            print('Classificacao: INFANTIL')
        elif idade_atual <= 19:
            print('Classificacao: JUNIOR')
        elif idade_atual <= 25:
            print('Classificacao: SENIOR')
        elif idade_atual > 25:
            print('Classificacao: MASTER')
        else:
            print('valor invalido favor digitar um valor valido')

    else:
        print('ERRO!!!!!')



