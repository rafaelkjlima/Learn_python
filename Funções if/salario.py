sal = float(input('qual seu salario? '))
    #pegar o valor de 1250,00
if sal >= 1250.00:
    alm1 = sal * 1.10
    print('seu salario ficou de {} teve um aumento para {}.'.format(sal, alm1))
else:
    alm2 = sal * 1.15
    print('Seu salario ficou de {} teve um aumento para {}.'.format(sal, alm2))
print('\033[7mobrigado por usar nosso app.\033[m')
