frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for l in range(len(junto) -1, -1, -1):
    inverso += junto [l]

if inverso == junto:
    print('está frase é um palindromo.')
else:
    print('está frase não é um palindromo.')

