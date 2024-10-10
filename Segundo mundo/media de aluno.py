n1 = float(input('Primeiro trimestre: '))
n2 = float(input('Segundo trimestre: '))
n3 = float(input('terceiro trimestre: '))
media = (n1 + n2 + n3) / 3
if media < 5:
    print('reprovado com uma media abaixo de {:.2f}'
          .format(media))
elif media >= 5 and media < 6.9:
    print('recuperação com media de {:.2f}'
          .format(media))
else:
    print('aprovado com a media de {:.2f}'
          .format(media))
print('\033[32mObrigado por usar nosso app')
