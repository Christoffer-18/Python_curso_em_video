#Seno, Cosseno e Tangente

from math import radians as r, sin as s, cos as c, tan as t
a = int(input('Digite um ângulo:'))
print(f'O ângulo de {a}º tem o SENO de {s(r(a)):.2f}\n'
      f'O COSENO de {c(r(a)):.2f}\n'
      f'E a TANGENTE será de {t(r(a)):.2f}')