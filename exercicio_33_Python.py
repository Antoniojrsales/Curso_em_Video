valor_um = int(input('Digite o primeiro Valor: '))
valor_dois = int(input('Digite o segundo Valor: '))
valor_tres = int(input('Digite o terceiro Valor: '))

menor = valor_um
if valor_dois < valor_um and valor_dois < valor_tres:
    menor = valor_dois
if valor_tres < valor_um and valor_tres < valor_dois:
    menor = valor_tres
print(f'O menor valor digitado foi {menor}')

maior = valor_um
if valor_dois > valor_um and valor_dois > valor_tres:
    maior = valor_dois
if valor_tres > valor_um and valor_tres > valor_dois:
    maior = valor_tres
print(f'O maior valor digitado foi {maior}')

#Forma Melhorada#

'''valores = list(map(int, input('Digite os valores separados por um espaco: ').split()))
sorteio = sorted(valores)
print(f'O menor valor digitado foi {min(sorteio)}')
print(f'O maior valor digitado foi {max(sorteio)}')'''
