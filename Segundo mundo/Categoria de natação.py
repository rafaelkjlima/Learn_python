import datetime
nome = str(input('Qual seu nome ?'))
ano = int(input('Qual ano você nasceu ?'))
idade = datetime.datetime.now().year - ano

if nome ==  'rafael':
    print('Uauu, que legal seu nome')

if idade < 9:
    print('Sua categoria é mirim')
elif idade > 9 and idade < 14:
    print('Sua categoria é infantil')
elif idade > 14 and idade < 19:
    print('Sua categoria é Junior')
elif idade > 19 and idade < 20:
    print('Sua categoria é sênior')
else:
    print('Sua categoria é Master')
print('Obrigado por usar nosso app')