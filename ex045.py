from random import randint as al
from time import sleep as d
itens = ('Pedra', 'Papel', "Tesoura")
print('''\033[36mEscolha uma opção:
{1} Pedra.
{2} Papel.
{3} Tesoura.''' )
e = int(input('Qual é a sua escolha:'))
print('JO')
d(1)
print('KEN')
d(1)
print('PO!!')
a = al(1 ,3)
if e == a:
    print(f'Deu empate eu pensei em {itens[a]} e você também.')
elif a == 1 and e == 2:
    print(f'\033[32mVOCÊ VENCEU!! PAPEL embrulha PEDRA.')
elif a == 1 and e == 3:
    print('\033[31mVOCÊ PERDEU!! PEDRA quebra TESOURA.')
elif a == 2 and e == 1:
    print('\033[31mVOCÊ PERDEU!! PAPEL embrulha PEDRA.')
elif a == 2 and e == 3:
    print('\033[32mVOCÊ VENCEU!! TESOURA corta PAPEL.')
elif a == 3 and e == 1:
    print('\033[32mVOCÊ VENCEU!! PEDRA quebra TESOURA.')
elif a == 3 and e == 2:
    print('\033[31mVOCÊ PEDEU!! TESOURA corta PAPEL.')
else:
    print('\033[31mJOGADA INVÁLIDA. TENTE NOVAMENTE!')