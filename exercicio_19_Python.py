import random
lista_alunos = ['Paulo', 'Ana', 'Pedro', 'Maria']
for valor, lista in enumerate(lista_alunos):
    print(f'Aluno {valor}: {lista}')

print()

print(f'Primeiro aluno: {lista_alunos[0]}')
print(f'Segundo aluno: {lista_alunos[1]}')
print(f'Terceiro aluno: {lista_alunos[2]}')
print(f'Quarto aluno: {lista_alunos[3]}')

print()

sorteado = random.choice(lista_alunos)
print(f'O aluno escolhido foi: {sorteado}')