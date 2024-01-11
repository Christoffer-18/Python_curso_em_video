m20 = h = ma18 = 0
while True:
    i = int(input('Idade:'))
    s = ' '
    while s != 'M' and s != 'F':
        s = str(input('Sexo [M/F]:')).strip().upper()[0]
    print('--' * 20)
    o = ' '
    while o != 'S' and o != 'N':
        o = str(input('Quer continuar? [S/N]')).strip().upper()[0] #opção
    print('--' * 20)
    if s == 'F' and i < 20:
        m20 += 1
    if s == 'M':
        h += 1
    if i > 18:
        ma18 += 1
    if o == 'N':
        break
print('FIM DO PROGRAMA')
print(f'Total de pessoa(s) com mais de 18 anos é {ma18}\n'
      f'Ao todo tem {h} homen(s) cadastrados.\n'
      f'E temos {m20} mulhere(s) com menos de 20.')