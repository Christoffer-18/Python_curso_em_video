from random import randint as al
from time import sleep as s
cor = {'f': '\033[m', 'v': '\033[31m', 'verde':'\033[32m', 'b': '\033[4;37m'}
a = al(0, 10)
c = 0
print(f'{cor["verde"]}-=-{cor["f"]}' * 30)
n = int(input('Estou pensando em um número entre 0 e 10, tente adivinhar...'))
print(f'{cor["verde"]}-=-{cor["f"]}' * 30)
print(f'{cor["b"]}PROCESSANDO...{cor["f"]}')
s(1)
if n == a:
    print(f'{cor["verde"]}PARABÉNS!! você venceu.{cor["f"]}')
else:
    while a != n:
        if a != n:
            c += 1
            if a > n:
                n = int(input(f'{cor["v"]}mais..., tente novamente:'))
            else:
                n = int(input(f'{cor["v"]}menos..., tente novamente:'))
    if a == n:
        print(f'{cor["verde"]}PARABÉNS!! você conseguiu acertar o número após {c + 1} tentativas.{cor["f"]}')