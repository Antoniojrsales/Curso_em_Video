from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (f'O ano de {ano} Ano Bissexto')
else:
    print(f'O ano de {ano} Nao e um ano Bissexto')

'''
Usando Funcao
def is_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True#Se os tres calculos forem verdadeiros
            else:
                return False#Se um dos tres calculos forem falso
        else:
            return True#Se falso a divisao por 100
    else:
        return False#Se falso a divisao por 4
year = int(input())
print(is_leap(year))'''