nome = str(input('Digite o seu nome completo: ')).strip()
nome_spl = nome.split()
print('Analisando o seu nome... ')
print('O seu nome em maiusculo e ', nome.upper())
print('O seu nome em maiusculo e ', nome.lower())
print(f'Seu nome tem no total {len(nome) - nome.count(" ")} letras')
print('Seu primeiro nome tem no total ', len(nome_spl[0]))