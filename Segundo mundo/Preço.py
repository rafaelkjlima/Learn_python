pag = int(input(
    'Qual é o tipo de pagamento?\n 1 - avista dinheiro\n 2 - avista cheque \n 3 - avista cartão \n 4 - parcelado'))
if pag == 4:
    vezes = int(input('Em quantas parcelas deseja fazer?'))
preço = 300

if pag == 1:
    print('Você tem direito a 10% de desconto e o valor cai de {} para {:.2f} .'.format(preço, preço - preço * 0.1))
elif pag == 2:
    print('Você tem direito a 10% de desconto e o valor cai de {} para {:.2f} .'.format(preço, preço - preço * 0.1))
elif pag == 3:
    print('Você tem direito a 5% de desconto e o valor cai de {} para {:.2f} .'.format(preço, preço - preço * 0.05))
elif pag == 4 and vezes < 2:
    print('Você parcelou em {} x de R${}.'.format(vezes, preço/vezes))
elif pag == 4 and vezes >= 3:
    print('Você parcelou em {} x de R${}. com o valor total de {}'.format(vezes, (preço + preço*0.2)/vezes, preço + preço*0.2))
