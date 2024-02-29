'''
Crie um programa que leia o peso e a altura de uma pessoa calcule seu imc 
e mostre seu status de acordo com a tabela abaixo
Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso Ideal
25 ate 30: Sobrepeso
30 ate 40: Obesidade
Acima de 40: Obesidade Morbida
'''

try:
    peso = float(input('Qual o seu peso? (KG) '))
    altura = float(input('Qual a sua altura? (M) '))
    resultado = peso / (altura ** 2)
    print()      
    if altura > 2.1:
        print('Altura indisponivel vc digitou uma altura fora do padrao')
    elif resultado < 18.5:
        print('O seu imc esta: Abaixo do Peso')
    elif resultado <= 24.9:
        print('O seu imc esta: Peso Ideal')
    elif resultado <= 29.9:
        print('O seu imc esta: Levemente acima do Peso')
    elif resultado <= 34.9:
        print('O seu imc esta: Obesidade Grau 1')
    elif resultado <= 39.9:
        print('O seu imc esta: Obesidade Grau 2')
    else:
        print('O seu imc esta: Obesidade Morbida')
except ValueError:
    print('ERRRRRO!')
    print('Vc digitou uma letra ou nao digitou nada')