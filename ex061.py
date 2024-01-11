print('==' * 20)
print('10 termos de uma PA')
print('==' *20)
a = int(input('Primeiro termo:'))
b = int(input('Razão:'))
t = a
cont = 1
while cont <= 10:
    print(f'{t}', end= ' ')
    t += b
    cont +=1