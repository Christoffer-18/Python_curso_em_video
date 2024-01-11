cont = s = 0
print('\033[32;4;1mDIGITE 999 QUANDO QUISER PARAR!!\033[m')
while True:
    n = int(input('digite um número:'))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram digitados {cont} números.\n'
      f'A soma foi {s}.')