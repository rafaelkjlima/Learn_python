from datetime import date
menor = 0
maior = 0

for people in range(1, 8):
    nasc = int(input('qual sua data de nascimento? '))
    idade = date.today().year - nasc
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('O total de maiores de idade são {} e de menores de idade são {}.'.format(maior, menor))

        