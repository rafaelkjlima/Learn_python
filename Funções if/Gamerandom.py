import random
    #Está com falha do codigo random, instalar na pasta.
nome = input('qual seu nome?')
if nome == 'rafael':
    print('Legal seu nome')
print('seja bem vindo {}'.format(nome))

n1 = random.randrange(0,10)
n2 = int(input('Pensei em um numero, adivinhe o numero?'))
if n1 == n2:
    print('Parabens, {} venceu!!'.format(nome))
else:
    print('Errou, pensei em {}. bom jogo {}'.format(n1, nome))
print('fim de game')
