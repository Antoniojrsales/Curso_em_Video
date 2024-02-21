'''Refaca o Desafio 35 dos triangulos acrescentando o 
recurso que mostra o tipo de triangulo que sera formado:
Equilatero: Todos os lados iguais
Isoceles: Dois lados iguais
Escaleno: Todos os lados diferentas''' 
import os

while True:
    validador = input('Digite [F] para finalizar o programa ou digite algo para continuar: ').upper()
    if validador == 'F':
        print('Fim do Programa!!!!!!')
        break
    else:
        os.system('cls')
    print('-='*12)
    print('Analisador de Triangulo')
    print('-='*12)
    valores = []
    try:
        for valor in range(3):
            valor = float(input('Digite o segmento da reta: '))
            valores.append(valor)
            
        A = valores[0]
        B = valores[1]
        C = valores[2]
            
        if A < B + C and B < A + C and C < A + B:
            if A == B == C:
                segmento = 'EQUILATERO'
            elif A != B != C != A:
                segmento = 'ESCALENO'
            else:
                segmento = 'ISOCELES'
            print()
            print(f'Os segmentos acima PODEM FORMAR um Triangulo {segmento}!')
        else:
            print()
            print('Os segmentos acima NAO PODEM FORMAR um Triangulo')
    except ValueError:
        print('Vc digitou algo errado ou nao digitou nada')
        print('Favor digitar todos os segmentos com valores validos')
