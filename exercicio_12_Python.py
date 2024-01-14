preco = float(input('Digite o valor do produto R$: '))
desconto = preco - (preco * 5/100)
print(f'O produto que custava R${preco} na promocao com desconto de 5% saira R${desconto:.2f}')