n = int(input('Digte um número:'))
print('\033[32;1;4mDIGITE 0 QUANDO QUISER PARAR!\033[m')
cont = media = 0
soma = ma = me = n
while n != 0:
    print('~~' * 20)
    n = int(input('digite outro número:'))
    cont += 1
    soma += n
    if n > ma:         #a melhor forma que eu consegui para ver o maior e menor núm.
        ma = n
    if n > 0:
        if n < me:
            me = n
media = soma /cont
print(f'Você colocou {cont} números.\n'
      f'A média dos números digitados é de {media:.2f}\n'
      f'O maior valor digitado foi {ma} e o menor foi {me}')