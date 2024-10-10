casa = int(input('Qual o valor da casa ?'))
sal = int(input('Qual o valor do seu salario ?'))
anos = int(input('Quantos anos você pretende pagar a casa ?'))
ent = int(input('possui entrada?'))
meses = anos * 12
parcela = (casa-ent) / meses
porc = sal * 0.3

if parcela > porc:
    print('valor negado pois a parcela fica em R${:.2f} em {}x 30% do seu salario não é {:.2f} compativel.'
          .format(parcela, meses, porc))
else:
    print('valor aprovado pois a parcela fica em R${:.2f} em {}x 30% do seu salario é {:.2f} compativel.'
          .format(parcela, meses, porc))
print('obrigado por usar nosso app')
