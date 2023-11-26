#Sorteando um item na lista

from random import choice as um
a1 = str(input('Qual o nome do primeiro aluno:')).strip()
a2 = str(input('O nome do segundo:')).strip()
a3 = str(input('O nome do terceiro:')).strip()
a4 = str(input('O nome do quarto:')).strip()
l = [a1, a2, a3, a4]
b = um(l)
print(f'O aluno escolhido foi {b}')