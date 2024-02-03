'''Crie um programa que leia dois numeros inteiros e compare-os
mostrando na tela uma mensagem
-O primeiro valor e maior
-O segundo valor e maior
-nao existe valor maior os dois sao iguais
-F ou f = Fim do Programa'''

while True:
    try:
        primeiro_num = input('Primeiro Numero: ').lower()
        if primeiro_num.isdigit():
            primeiro_num = int(primeiro_num) 
        if primeiro_num == 'f' :
            print('FIM')
            break
        
        segundo_num = int(input('Segundo Numero: '))
        
        if primeiro_num > segundo_num:
            print('O PRIMEIRO valor e maior')
        elif segundo_num > primeiro_num:
            print('O SEGUNDO valor e maior')
        elif primeiro_num == segundo_num:
            print('Os dois valores sao IGUAIS')
    except ValueError:
        print('Vc digitou uma letra ou nao digitou nada, Favor digitar um valor valido'
              ' ou [f] para FIM do programa')
        continue