import random
n1 = int(input('Pedra (1), Papel(2) ou Tesoura (3)?'))
n2 = random.randrange(0,4)


if n1 == 1 and n2 == 2 or n1 == 2 and n2 == 1 or n1 == 3 and n2 == 2:
    print('player 1 ganhou.', n2)
elif n1 == 1 and n2 == 3 or n1 == 2 and n2 == 3 or n1 == 3 and n2 == 1:
    print('player 1 perdeu.', n2)
else:
    print('empate')
print('bom jogo')
