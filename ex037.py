n = int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão\n'
      '[1] para BINÁRIO\n'
      '[2] para OCTAL\n'
      '[3] para HEXADECIMA' )
o = int(input('Sua escolha:'))
if o == 1:
    print(f'\033[35m{n} convertido para binário é {bin(n)[2:]}')
elif o == 2:
    print(f'\033[35m{n} convertido para octal é {oct(n)[2:]}')
elif o == 3:
    print(f'\033[35m{n} convertido para hexadecimal é {hex(n)[2:]}')
else:
    print('\033[31mOpção inválida. Tente novamente!')