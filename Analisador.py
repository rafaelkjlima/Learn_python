somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = 0
sub20mulher = 0
    #Apliquei todas as variaveis com '0', mas tanto faz.
    
for p in range(1, 5):
    print('------ {} pessoa -------- '.format(p))
    nome = str(input('nome: '))
    idade = int(input('Idade: '))
    sex = str(input('M/F: '))
        #Aqui capta todos os dados que foram pedidos no desafio

    somaidade += idade
    if p == 1 and sex in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sex in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
            #Aqui faz a seguinte analize: é o primeiro nome que está na lista ? não ?
            #então o segundo nome é maior que o primeiro ?

    if sex in 'Ff' and idade < 20:
        sub20mulher += 1
    
mediaidade = somaidade / 4
print('A media das pessoas é de {}.'.format(mediaidade))
print('O homem mais velho é chamado de {} e tem {} anos.'.format(nomemaisvelho, maioridadehomem))
print('Das pessoas {} são mulheres abaixo de 20 anos.'.format(sub20mulher))
