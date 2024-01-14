frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A aparece {frase.count("a")} vezes na frase')
print(f'A primeira letra A aparece na posicao {frase.find("a")+1}')
print(f'A ultima letra A aparece na posicao {frase.rfind("a")+1}')
