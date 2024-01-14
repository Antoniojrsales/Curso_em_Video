from random import shuffle
lista_alunos = []
contador = 0

while contador < 4:
    lista = input('Digite o nome do aluno: ')
    contador += 1
    lista_alunos.append(lista)
    shuffle(lista_alunos)
print('A ordem de apresentacao sera: ')
print(lista_alunos)
