print('\033[33;1;4mDIGITE UM NÚMERO NEGATIVO QUANDO QUISER PARAR!!\033[m')
while True:
    print('\033[32;40mXXX\033[m' * 20)
    t = int(input('Quer ver a tabuada de qual valor ?'))
    if t < 0:
        break
    for c in range(1, 11):
        print(f'{t} * {c:2} = {t*c:2}')
print('Programa tabuada encerrado, volte sempre!') 