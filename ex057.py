lst = ['M' , 'F']
while lst != 'M' and lst != 'F':
    lst = str(input('Digite seu sexo[M/F]:')).strip().upper()[0]
    if lst == 'F' or lst == 'M':
        if lst == 'M':
            print('O sexo escolhido foi o masculino.')
        elif lst == 'F':
            print('O sexo escolhido foi feminino.')
    else:
        print(f'Desculpe a palavra digitada não esta disponivel, tente novamente!')