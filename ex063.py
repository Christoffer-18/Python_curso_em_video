print('*' * 30)
print('Sequência de Fibonacci')
print('*' * 30)
n = int(input('Quantos termos você quer mostrar?'))
print('~' * 30)
t1 = 0
t2 = 1
cont = 3
print(f'{t1} - {t2}' , end=' - ')
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(f'{t3}', end=' - ')
print('FIM')
print('~' * 30)