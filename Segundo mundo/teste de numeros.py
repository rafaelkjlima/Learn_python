n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))

if n1 > n2:
    print('O primeiro valor {} é maior que o segundo valor {}.'
          .format(n1, n2))
elif n1 < n2:
    print('O segundo valor {} é maior que o primeiro valor {}.'
          .format(n2, n1))
else:
    print('Os valores digitados são iguais.')
print('Obrigado por usar nosso app.')
