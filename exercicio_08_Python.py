metro = float(input('Digite um valor em metros: '))
print(f'A medida de {metro}m corresponde a ')
print(f'{metro / 1000}km\n{metro / 100}hm\n{metro / 10}dam\n{metro * 10}dm\
      \n{metro * 100}cm\n{metro * 100}mm')

'''
# Obtendo um script mais estruturado

"""Funcao que converte metros para outras unidades e exibe os resultados."""
def conversao(metro):
      print(f'A medida de {metro}m corresponde a ')
      print(f'{metro / 1000}km\n{metro / 100}hm\n{metro / 10}dam\n{metro * 10}dm\
      \n{metro * 100}cm\n{metro * 100}mm') 

"""Funcao que obtém e valida a entrada do usuário."""
def obter_dados():
      while True:
            valor = input('Digite [s/S] para finalizar o programa ou um valor valido para fazer a conversao: ').upper()
            
            if valor == 'S':
                  print('Programa finalizado com sucesso.')
                  return None
            
            try:
                  valor_float = float(valor)
                  return valor_float
            except ValueError:
                  print('Erro: você não digitou um valor válido. Tente novamente.')

"""Função principal que executa o programa de conversão."""
def main():
      while True:
            valor = obter_dados()
            if valor is None:
                  break
            conversao(valor)

# Inicia o programa
if __name__ == "__main__":
    main()'''

'''
# Obtendo um script mais estruturado outra forma

def conversao(metro):
    """Converte metros para outras unidades e exibe os resultados."""
    print(f'A medida de {metro} m corresponde a:')
    print(f'{metro / 1000:.3f} km')  # Convertendo metros para quilômetros
    print(f'{metro / 100:.3f} hm')   # Convertendo metros para hectômetros
    print(f'{metro / 10:.3f} dam')   # Convertendo metros para decâmetros
    print(f'{metro * 10:.3f} dm')    # Convertendo metros para decímetros
    print(f'{metro * 100:.3f} cm')   # Convertendo metros para centímetros
    print(f'{metro * 1000:.3f} mm')  # Convertendo metros para milímetros
    print()  # Adiciona uma linha em branco para melhor legibilidade


def obter_dados():
    """Obtém e valida a entrada do usuário."""
    while True:
        valor = input('Digite [s/S] para finalizar o programa ou um valor válido para fazer a conversão: ').upper()
        
        if valor == 'S':
            print('Programa finalizado com sucesso.')  # Mensagem de finalização
            return None
        
        try:
            valor_float = float(valor)  # Tenta converter a entrada para float
            return valor_float
        except ValueError:
            print('Erro: você não digitou um valor válido. Tente novamente.')  # Mensagem de erro


def main():
    """Função principal que executa o programa de conversão."""
    while True:
        valor = obter_dados()  # Obtém o valor do usuário
        if valor is None:
            break  # Finaliza o loop se o valor for None
        conversao(valor)  # Chama a função de conversão


# Inicia o programa
if __name__ == "__main__":
    main()'''
