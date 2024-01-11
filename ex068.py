from random import randint as al
print('=-='*20)
print('Vamos jogar \033[31mPAR\033[m ou \033[32mÍMPAR\033[m ')
print('=-='*20)
cont = 0
while True:
    a = al(1, 10)
    n = int(input('Digite um número:'))
    n1 = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0:1]
    print('---'*20)
    if n1 != 'P' and n1 != 'I':
        print('\033[31mERRO!! TENTE NOVAMENTE!\033[m')
    soma = n + a
    d = soma % 2 #divisão
    print(f'Você jogou {n} e eu {a}, o total foi {soma} que é ', end='')
    print('\033[31mPAR\033[m' if d == 0 else '\033[32mÍMPAR\033[m')
    if n1 == 'P':
        if d == 0:
            print('Você VENCEU!!')
        else:
            print('você PERDEU!!')
            break
    if n1 == 'I':
        if d != 0:
            print('Você VENCEU!!')
        else:
            print('Você PERDEU!!')
            break
    cont += 1
print('---'*20)
print(f'GAME OVER! você venceu {cont} vezes.')