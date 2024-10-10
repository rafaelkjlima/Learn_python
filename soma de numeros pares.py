cont = 0
soma = 0
for c in range(1, 7):
    n = int(input('digite o {} numero: '.format(c)))
    if n % 2 == 0:
        #soma = soma + c
        soma += n
        cont += 1
print('A soma dos {} valores são {}.'.format(cont, soma))

