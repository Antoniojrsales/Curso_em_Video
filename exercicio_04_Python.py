dados = input('Digite Algo: ')
print(f'O tipo primitivo desse valor e: {type(dados)}')
print(f'So tem espacos: {dados.isspace()}')
print(f'E um numero: {dados.isnumeric()}')
print(f'E um alfabeto: {dados.isalpha()}')
print(f'E um alfanumerico: {dados.isalnum()}')
print(f'Esta em maiusculo: {dados.isupper()}')
print(f'Esta em minusculo: {dados.islower()}')
print(f'Esta capitalizado: {dados.istitle()}')

'''
# Função para verificar as propriedades da string inserida

def verificar_propriedades(valor):
    print(f"O tipo primitivo desse valor é {type(valor)}")
    print(f"Só tem espaços? {valor.isspace()}")
    print(f"É um número? {valor.isnumeric()}")
    print(f"É alfabético? {valor.isalpha()}")
    print(f"É alfanumérico? {valor.isalnum()}")
    print(f"Está em maiúsculo? {valor.isupper()}")
    print(f"Está em minúsculo? {valor.islower()}")
    print(f"Está capitalizado? {valor.istitle()}")

# Captura a entrada do usuário
nome = input('Digite algo: ')

# Chama a função de verificação
verificar_propriedades(nome)'''