n1 = float(input('Digite um valor:'))
n2 = float(input('Digite outro valor:'))
print('''O que você deseja fazer com esses valores:
 [1] Somar.
 [2] Multiplicar.
 [3] Maior.
 [4] Novos números.
 [5] finalizar.''')
o = int(input('Qual opção:'))
while o != 5:
    if o == 1:
        print(f'A soma de {n1:.0f} e {n2:.0f} é {n1 + n2:.0f}')
    elif o == 2:
        print(f'A multiplicação de {n1:.0f} e {n2:.0f} é igual a {n1 * n2:.0f}')
    elif o == 3:
        if n1 > n2:
            print(f'{n1:.0f} é maior que {n2:.0f}')
        else:
            print(f'{n2:.0f} é maior que {n1:.0f}')
    elif o == 4:
        n1 = int(input('Digite um novo número:'))
        n2 = int(input('Digite outro número:'))
    else:
        print('Opção inválida, tente novamente!')
    print('=-=' * 20)
    o = int(input('qual a proxima opção:'))
print('finalizando...\n'
      'fim do programa, volte sempre.')