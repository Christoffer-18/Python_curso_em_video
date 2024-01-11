print('==' * 20)
print('10 termos de uma PA')
print('==' *20)
a = int(input('Primeiro termo:'))
b = int(input('Razão:'))
s = a + (10 - 1) * b
for c in range(a, s + b, b):
    print(c, end= ' ')
