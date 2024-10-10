nome = str(input('Qual seu nome ?'))
peso = int(input('Qual seu peso atual ?'))
altura = float(input('Qual sua altura ?'))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso com imc de {:.2f}.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal com imc de {:.2f}.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Sobrepeso com imc de {:.2f}.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Obesidade 1 com imc de {:.2f}.'.format(imc))
else:
    print('Obesidade 2 com imc de {:.2f}.'.format(imc))
print('Obrigado por usar nosso app.')
