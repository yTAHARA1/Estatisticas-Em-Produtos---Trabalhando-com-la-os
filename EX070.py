acm = 0
prodc = 0
total = 0

produto = []
preco = []
while True:
    while True:
        prec = input('Digite o valor do produto: R$')
        try:
            prec1 = float(prec)
            total += prec1
            preco.append(prec1)
            break
        except ValueError:
            print('Somente Números')
    acm += 1
    while True:
        prod = input(f'Digite o nome do produto {acm}: ')
        if prod.replace(' ', '').isalpha():
         break
        else:
            print('Somente palavras')
    if prec1 > 1000:
        prodc += 1
    produto.append(prod)
    while True:
        dnv = input('Voce deseja mais algum produto?: ').lower()
        if dnv in['s', 'sim','n', 'nao']:
            break
        else: 
           print('Resposta Invalida')
    if dnv == 's' or dnv == 'sim':
                print('-'*30)
                print('Próximo Produto')
                print('-'*30)
    else:
        print('Operacao Finalizada')
        break

menorpreco = min(preco)
posicao = preco.index(menorpreco)
produto_mais_barato = produto[posicao]
print('-'*30)
print(f'O produto com menor preço é {produto_mais_barato}')
print('-'*30)
print(f'O valor total da compra é R${total}')
print('-'*30)
print(f'{prodc} produtos custam mais de 1000R$')
print('-'*30)