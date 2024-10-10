numero = int(input('Digite um numero: '))
print('-'*11)
print(f'{numero} x  1 = {numero * 1}')
print(f'{numero} x  2 = {numero * 2}')
print(f'{numero} x  3 = {numero * 3}')
print(f'{numero} x  4 = {numero * 4}')
print(f'{numero} x  5 = {numero * 5}')
print(f'{numero} x  6 = {numero * 6}')
print(f'{numero} x  7 = {numero * 7}')
print(f'{numero} x  8 = {numero * 8}')
print(f'{numero} x  9 = {numero * 9}')
print(f'{numero} x 10 = {numero * 10}')
print('-'*11)


'''
# Obtendo um script mais estruturado

"""Função que exibe a tabuada de um número."""
def tabuada(num):
    for i in range(1, 11): # Laço de repetição que vai de 1 a 10
        print(f'{num} x  {i} = {num * i}') #Msg do resultado da tabuada

"""Funcao que obtém e valida a entrada do usuário."""
def obter_dados():
    while True:
        numero = input('Digite [s/S] para finalizar o programa ou um valor valido para tabuada: ').strip().upper() # Entrada do usuario

        if numero == 'S': # Finaliza o programa se o usuário digitar 'S'
            print('Muito obrigado por usar nosso programa.')
            print('Programa finalizado com sucesso.')
            return None
        
        try:
            numero_int = int(numero) # Tenta converter a entrada para um inteiro
            return numero_int
        except ValueError:
            print('Erro: você não digitou um valor válido. Tente novamente.') # Msg de erro caso algo de errado

"""Função principal que executa o programa de Tabuada."""
def main():
     while True:
        numero = obter_dados() # Obtém o número do usuário

        if numero is None:
             break # Sai do loop se o usuário escolher finalizar
        
        tabuada(numero) # Exibe a tabuada do número 

# Inicia o programa
if __name__ == "__main__":
    main()'''
