dados = input('Digite Algo: ')
print(f'O tipo primitivo desse valor e: {type(dados)}')
print(f'So tem espacos: {dados.isspace()}')
print(f'E um numero: {dados.isnumeric()}')
print(f'E um alfabeto: {dados.isalpha()}')
print(f'E um alfanumerico: {dados.isalnum()}')
print(f'Esta em maiusculo: {dados.isupper()}')
print(f'Esta em minusculo: {dados.islower()}')
print(f'Esta capitalizado: {dados.istitle()}')
