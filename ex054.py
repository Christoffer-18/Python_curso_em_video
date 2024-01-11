from datetime import date as d
m = 0  #maior
n = 0  #menor
for c in range(1,8):
    a = int(input(f'em que ano a {c}ª pessoa nasceu:'))
    s1 = d.today().year - a
    if s1 >= 21:
        m += 1
    else:
        n += 1
print(f'Tem {m} pessoas com mais de 21 anos \n'
      f'E {n} com menos de 21.')
