from time import sleep
n = int(input('Digite um numero: '))
for c in range(n, 0, -1):
    print(c)
    sleep(1)
print('fim de contagem')
