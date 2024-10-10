n1 = int(input('Digite um numero para PA: '))
razão = int(input( 'digite a razão: '))

for c in range(0, n1+1, razão):
    print(c, end=' - ')
print('acabou')
