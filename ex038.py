from time import sleep
a = float(input('digite um núemro:'))
b = float(input('digite outro número:'))
print('\033[4mANALISANDO...')
sleep(1.5)
if a > b:
    print(f'\033[4;34m{a:.0f} é o maior número.')
elif b > a:
    print(f'\033[4;34m{b:.0f} é o maior número.' )
elif a == b:
    print(f'\033[4;34m{a:.0f} e {b:.0f} tem o mesmo valor.')