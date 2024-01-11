n = int(input('Digite um Número:'))
print('\033[32;1;4mDIGITE 999 PARA TERMINAR\033[m')
cont = 0
soma = n
while n != 999:
    print('~~' * 20)
    cont += 1
    soma += n
    n = int(input('digite outro número:'))
print(f'Você digitou {cont} números e a soma deles é {soma} ')
