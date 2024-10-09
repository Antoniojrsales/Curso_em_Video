nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite a segunda nota: '))
media = (nota_um + nota_dois) / 2
print(f'A media entre {nota_um} e {nota_dois} e igual a {media:.1f}')

'''
# Criando uma funcao para o exer. com tratamento de erro

# funcao que calcula a média entre as duas notas
def media(pri_nota, seg_nota):
        media = (pri_nota + seg_nota) / 2
        print(f'A media da nota_1: {pri_nota} e a nota_2: {seg_nota} e igual a {media:.1f}')

while True:
    inicio = input('Digite [s/S] para finalizar o programa ou qualquer tecla para continuar: ').upper() # Pergunta ao usuário se deseja continuar ou finalizar o programa
    if inicio == 'S': # Verifica se o retorno é [s/S], indicando que o programa deve ser encerrado
         print('Programa finalizado')
         break

    # Solicita as notas ao usuário
    nota_um = input('Digite a primeira nota: ')
    nota_dois = input('Digite a segunda nota: ')
    if nota_um.isdigit() and nota_dois.isdigit(): # Verifica se as notas foram digitadas com valores validos
        nota_um_float = float(nota_um) # Tenta converter as entradas para float
        nota_dois_float = float(nota_dois) # Tenta converter as entradas para float
        media(nota_um_float, nota_dois_float) # Chama a função media() para calcular e imprimir a média das notas    
    else:
        print('Vc digitou algo errado ou nao digitou nada')
        print('Favor digitar um valor valido') # Se ocorrer um erro de conversão, informa o usuário e repete o loop '''


'''
# Obtendo um script mais estruturado

# funcao que calcula a média entre as duas notas
def media(pri_nota, seg_nota):
        media = (pri_nota + seg_nota) / 2
        print(f'A media da nota_1: {pri_nota:.1f} e a nota_2: {seg_nota:.1f} e igual a {media:.1f}')

# Função para obter as notas do usuário
def obter_numero():
    while True:
        inicio = input('Digite [s/S] para finalizar o programa ou qualquer tecla para continuar: ').upper() # Pergunta ao usuário se deseja continuar ou finalizar o programa
        if inicio == 'S':
            print('Programa finalizado')
            return None, None  # Retorna None para indicar que o programa deve ser encerrado

        # Solicita as notas ao usuário
        nota_um = input('Digite a primeira nota: ')
        nota_dois = input('Digite a segunda nota: ')
        try:
            nota_um_float = float(nota_um) # Tenta converter as entradas para float
            nota_dois_float = float(nota_dois) # Tenta converter as entradas para float
            return nota_um_float, nota_dois_float # Retorna as notas convertidas para float
        except ValueError:
            print('Erro: você não digitou um valor válido. Tente novamente.') # Se ocorrer um erro de conversão, informa o usuário e repete o loop

# Função principal que controla o fluxo do programa
def main():
     while True:
        nota_um, nota_dois = obter_numero() # Chama a função obter_numero() e recebe as notas
        if nota_um is None and  nota_dois is None: # Verifica se o retorno é None, indicando que o programa deve ser encerrado
            break
        media(nota_um, nota_dois) # Chama a função media() para calcular e imprimir a média das notas

# Inicia o programa
if __name__ == "__main__":
    main()'''
