from random import randrange
from time import sleep

nome = input('qual seu nome?')
fichas = int(input('quantas fichas você quer ? '))

for c in range(0, fichas):

    if nome == 'rafael':
        print('Legal seu nome')
    print('seja bem vindo {}'.format(nome))

    n1 = randrange(0,10)
    n2 = int(input('Pensei em um numero, adivinhe o numero?'))
    if n1 == n2:
        print('Parabens, {} venceu!!'.format(nome))
    else:
        print('Errou, pensei em {}. bom jogo {}'.format(n1, nome))

    print('Verificando se ainda temos fichas {} ...'.format(nome))
    sleep(3)

print('acabou nossas fichas')
