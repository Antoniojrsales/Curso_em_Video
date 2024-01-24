'''Crie um programa que leia o comprimento de tres retas e 
diga ao usuario se elas formam ou nao um triangulo'''

print('-='*12)
print('Analisador de Triangulo')
print('-='*12)
reta_um = float(input('Primeiro seguimento: '))
reta_dois = float(input('Segundo seguimento: '))
reta_tres = float(input('Terceiro seguimento: '))

if reta_um < reta_dois + reta_tres and reta_dois < reta_um + reta_tres and reta_tres < reta_um + reta_dois:
     print('Os segmentos acima PODEM FORMAR um Triangulo')
else:
    print('Os segmentos acima NAO PODEM FORMAR um Triangulo')

#Forma Melhorada#
'''
print('-='*12)
print('Analisador de Triangulo')
print('-='*12)
try:
    valores = list(map(str, input('Digite os valores das 3 retas com espaco entre eles: ').split()))
    A = float(valores[0])
    B = float(valores[1])
    C = float(valores[2])

    if A < B + C and B < A + C and C < A + B:
     print('Os segmentos acima PODEM FORMAR um Triangulo')
    else:
        print('Os segmentos acima NAO PODEM FORMAR um Triangulo')
except ValueError:
   print('Digite um valor valido')
except IndexError:
   print('Vc digitou uma letra ou esta faltando valores favor digitar um valor valido')'''