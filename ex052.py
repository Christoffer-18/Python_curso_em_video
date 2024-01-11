a = int(input('Digite um número:'))
t =0
for c in range(1, a + 1):
    if a % c ==0:
        print('\033[32m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {a} é divisível por {t} números.')
if t == 2:
    print('E por isso que ele é PRIMO!')
else:
    print('E por isso que ele nãe é PRIMO')