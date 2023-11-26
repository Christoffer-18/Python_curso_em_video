#Sorteando uma ordem na lista

from random import shuffle
a1 = str(input('Qual o nome do primeiro aluno: ')).strip()
a2 = str(input('O nome do segundo: ')).strip()
a3 = str(input('O nome do terceiro: ')).strip()
a4 = str(input('O nome do quarto: ')).strip()
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentação será: \n'
      f'{lista}')