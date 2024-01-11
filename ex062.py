print('==' * 20)
print('10 termos de uma PA')
print('==' *20)
a = int(input('Primeiro termo:'))
b = int(input('Razão:'))
t = a
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{t}', end=' ')
        t += b
        cont += 1
    print('pausa' , end='')
    mais = int(input('\nMais quantos termos você deseja mostrar?'))
print(f'Progressão finalizada com {total} termos.')
