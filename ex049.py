t = int(input('digite um número:'))
print('\033[32;40mx'*20)
for c in range(1, 11):
    print(f'{t:2} x {c:2} = {t*c}')
print('\033[32mx'*20)