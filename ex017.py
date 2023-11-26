# Catetos e Hipotenusa

from math import hypot as h
c1 = float(input('Digite o comprimento do primeiro cateto:'))
c2 = float(input('Digite o comprimento do segundo cateto:'))
print(f'A hipotenusa desse triângulo retângulo é {h(c1,c2):.2f} ')