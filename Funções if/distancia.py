d = int(input('qual a distancia da sua viagem ?'))
if d <=200:
    soma = d * 0.5
    print('o valor da sua viagem fica em R$ {:.2f} baseado em {} km.'.format(soma, d))
else:
    soma2 = d * 0.45
    print('O valor da sua viagem fica em R$ {:.2f} baseado em {} km.'.format(soma2, d))
print('obrigado por usar nosso app.')
