# Aumentos múltiplos

s = float(input('Qual é o seu salário?R$'))
if s > 1250:
    print(f'O seu salário de R${s} com um aumento de 10%, ficaria em R${(s*10/100)+s:.2f}')
else:
    print(f'O seu saário de R${s} com um aumento de 15%, ficaria em R${(s*15/100)+s:.2f}')