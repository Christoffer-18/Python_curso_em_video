print('\033[1;36m+/*' * 20)
print('\033[1;36mANALISADOR DE TRIÂNGULO!!')
print('\033[1;36m+/*' * 20)
a = float(input('digite o comprimento da primeira reta:'))
b = float(input('Digite o comprimento da segunda reta:'))
c = float(input('Digite o comprimento da terceira reta:'))
if b + c > a and a + c > b and a + b > c:
    print('\033[32mOs números digitados PODEM FORMAR um triângulo', end='')
    if a == b == c:
        print(' EQUILÁTERO!')
    elif a != b != c != a:
        print(' ESCALENO!')
    else:
        print(' ISÓSCELES!')
else:
    print('\033[31mOs números digitados NÃO PODEM FORMAR um triangulo!')