print('''Qual sua idade ?
[1] Até 9 anos.
[2] De 10 a 14.
[3] De 15 a 19.
[4] 20 a 25.
[5] mais de 25.''')
r = int(input('digite o número:'))
if r == 1:
    print('\033[1;33mSua categoia é MIRIM!!')
elif r == 2:
    print('\033[1;33mSua categoria é INFANTIL!!')
elif r ==3:
    print('\033[1;33mSua categoria é JUNIOR!!')
elif r == 4:
    print('\033[1;33mSua categoria é SÊNIOR!!')
elif r == 5:
    print('\033[1;33mSua categoria é MASTER!!')
