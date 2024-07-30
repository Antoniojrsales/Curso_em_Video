'''mat = [[0 for j in range(3)] for i in range(3)]

for l in range(3):
    for c in range(3):
        mat[l][c] = int(input(f'Digite um valor para a posicao [{l+1}, {c+1}]: '))

for l in range(3):
    for c in range(2):
        print(f'{mat[l][c]:5}', end=' ')
    print()'''

'''from string import ascii_uppercase
a=list(ascii_uppercase)
mc=input('Digite a mensagem criptografada: ')
mc=mc.upper()
m=""
for l in mc:
    i=ord(l)-65
    if l in a:
        m+=a[(i-4)%26]
    else:
        l
print(f'Mensagem original: {m}')'''

import math
a = 3.445161e+03
b = 1.151436e+03
c = a / b
print('%.10e'%c)