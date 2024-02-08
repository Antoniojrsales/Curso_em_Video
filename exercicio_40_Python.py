'''Crie um programa que leia duas notas de um aluno e calcule 
sua media mostrando uma msg no final de acordo com a media atingida
-Media abaixo de 5: REPROVADO
-Media entre 5.0 e 6.9: RECUPERACAO
-Media acima de 7.0: APROVADO '''

try:
    notas = []
    for nota in range(2):
        nota = float(input('Digite a nota do aluno: '))
        notas.append(nota)

    media = round((notas[0] + notas[1]) / len(notas), 1)

    print(f'Tirando {notas[0]} e {notas[1]}, a media do aluno e {media}')

    if media < 5:
        print(f'O aluno esta REPROVADO')
    elif media < 6.9:
        print(f'O aluno esta em RECUPERACAO')
    else:
        print('O aluno esta APROVADO')
except ValueError:
    print('ERRO, Vc digitou uma letra ou nao digitou nada')
    print('Programa Finalizado')
    
    

