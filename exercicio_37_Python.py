'''Crie um programa que leia um numero inteiro e peca para o usuario escolher qual sera a 
sua base de conversao:
1-Binario
2-Octal
3-Hexadecimal
f-Fim do programa'''

while True:
    try:
        print('-#' * 12)
        numero = str(input('Digite um numero: '))
        
        if numero.isdigit():
            numero = int(numero)
        elif numero == 'f' or numero == 'F':
            print(f'FIM')
            break        
        else:
            print('Vc digitou uma letra ou nao digitou nada Favor escolher uma das Opcoes Abaixo')
            continue 

        print('Escolha uma das Opcoes para conversao:\n'
            '[1] Converter para Binario \n'
            '[2] Converter para Octal\n'
            '[3] Converter para Hexadecimal\n'
            '[f] Fim do programa')
                       
        opcao = str(input('Sua Opcao: '))
        
        if opcao == '1':
            print(f'{numero} convertido em Binario e igual a {bin(numero)[2:]}')
        elif opcao == '2':
            print(f'{numero} convertido em Octal e igual a {oct(numero)[2:]}')
        elif opcao == '3':
            print(f'{numero} convertido em Binario e igual a {hex(numero)[2:]}')
        elif opcao == 'f' or opcao == 'F':
            print(f'FIM')
            break
        else:
            print('Opcao invalida')
            print('Escolha uma das Opcoes para conversao:\n'
            '[1] Converter para Binario \n'
            '[2] Converter para Octal\n'
            '[3] Converter para Hexadecimal\n'
            '[f] Fim do programa')
        
    except ValueError:
        print('Vc digitou uma letra ou nao digitou nada Favor escolher uma das Opcoes Abaixo')
        print('Escolha uma das Opcoes para conversao:\n'
            '[1] Converter para Binario \n'
            '[2] Converter para Octal\n'
            '[3] Converter para Hexadecimal\n'
            '[f] Fim do programa')