numero = int(input('Digite um valor: '))
antecessor = numero - 1
sucessor = numero + 1
print(f'Analisando o valor {numero} seu antecessor e {antecessor} e seu sucessor e {sucessor}')

    
'''
Criando uma funcao para o exer. com tratamento de erro

def antes_depois(num):
    print(f'Analisando o valor {num}, seu antecessor é {num - 1} e seu sucessor é {num + 1}')

# Input do usuário
numero = input('Digite um valor: ') 

if numero.isdigit():
    numero_int = int(numero)
    antes_depois(numero_int)
else:
    print('Você não digitou um valor válido')
'''

'''Obtendo um script mais estruturado

def antes_depois(num):
    """Mostra o antecessor e o sucessor de um número."""
    print(f'Analisando o valor {num}, seu antecessor é {num - 1} e seu sucessor é {num + 1}')

def obter_numero():
    """Obtém um número válido do usuário com tratamento de erro."""
    while True:
        numero = input('Digite um valor numérico: ').strip()

        # Verificação de finalização
        if numero.lower() == 's':
            print('Programa finalizado.')
            return None
        
        # Tenta converter o input para inteiro
        try:
            numero_int = int(numero)
            return numero_int
        except ValueError:
            print('Erro: você não digitou um valor válido. Tente novamente ou digite [s] para sair.')

# Função principal que coordena a execução
def main():
    while True:
        numero = obter_numero()
        if numero is None:
            break
        antes_depois(numero)

# Inicia o programa
if __name__ == "__main__":
    main()'''