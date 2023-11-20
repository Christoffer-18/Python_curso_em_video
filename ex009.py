#Tabuada

t = int(input('digite um número:'))
c = {'f': '\033[32;40m'}
print('\033[32;40mx'*20)
print(f'{t} x 01 = {c["f"]}{t*1}\033[m')
print(f'{t} x 02 = \033[32;40m{t*2}\033[m')
print(f'{t} x 03 = \033[32;40m{t*3}\033[m')
print(f'{t} x 04 = \033[32;40m{t*4}\033[m')
print(f'{t} x 05 = \033[32;40m{t*5}\033[m')
print(f'{t} x 06 = \033[32;40m{t*6}\033[m')
print(f'{t} x 07 = \033[32;40m{t*7}\033[m')
print(f'{t} x 08 = \033[32;40m{t*8}\033[m')
print(f'{t} x 09 = \033[32;40m{t*9}\033[m')
print(f'{t} x 10 = \033[32;40m{t*10}\033[m')
print('\033[32;40mx\033[m'*20)