#Jogo da Adivinhação v.1.0

from random import randint as al
from time import sleep as d
cor = {'f': '\033[m', 'v': '\033[31m', 'verde':'\033[32m', 'b': '\033[4;37m'}
a = al(0, 5)
print(f'{cor["verde"]}-=-{cor["f"]}' * 30)
n = int(input('Estou pensando em um número entre 0 e 5, tente adivinhar...'))
print(f'{cor["verde"]}-=-{cor["f"]}' * 30)
print(f'{cor["b"]}PROCESSANDO...{cor["f"]}')
d(2)
if n == a:
    print(f'{cor["verde"]}PARABÉNS!! você venceu.{cor["f"]}')
else:
    print(f'{cor["v"]}Ganhei!! Eu pensei no número {a} e não no {n}.{cor["f"]}')
