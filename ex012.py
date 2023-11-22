# Calculando Descontos
p = float(input('digite o preço do produto: R$'))
d = float(input('digite o desconto:'))
r = (p*d)/100
print(f'o valor com do desconto de {d}% é de {r:.2f}'
    f'\nO preço final é de {p-r:.2f}')