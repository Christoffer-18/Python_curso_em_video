print(f'{" lojas colombo ":=^40}')
v = float(input('Qual o valor do pruduto?R$'))
print('''Qual a forma d epagamento?
[1] À vista dinheiro ou cheque.
[2] À vista no cartão.
[3] Em até 2 vezes no cartão
[4] em 3 vezes ou mais no cartão.''')
f = int(input('Escolha a forma de pagamento:'))
if f == 1:
    print(f'O seu produto vale R${v:.2f}, pagando com o dinheiro/cheque o valor final será de R${v - (v*10/100):.2f}')
elif f == 2:
    print(f'O seu produto vale R${v:.2f}, pagando com o cartão o valor final será de R$ {v - (v*5/100):.2f}')
elif f == 3:
    print(f'O seu produto vale R${v:.2f}, pagando em até 2x no cartão o valor final será {v:.2f}')
elif f == 4:
    p = int(input('quantas parcelas ?'))
    print(f'O seu produto vale R${v:.2f}, com um juros de 20%, será {p}x de R${(v*20/100+v)/p:.2f}'
          f'\no valor final será R${(v*20/100) + v:.2f}')
else:
    print('\033[31mOPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE ')
