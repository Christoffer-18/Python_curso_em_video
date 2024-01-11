ma = 0
me = 0
for c in range(1 , 6):
    p = float(input(f'Qual é o peso da {c}ª pessoa?'))
    if c == 1:
        ma = p
        me = p
    else:
        if p > ma:
           ma = p
        if p < me:
           me = p
print(f'O maior peso lido foi de {ma}Kg\n'
    f'O menor peso lido foi de {me}Kg')

                                  #Outra forma de fazer
#lst=[]  #lista vazia
#for c in range(1, 6):
#    peso=float(input('Peso da {}ª pessoa: '.format(c)))
#    lst+=[peso]   #adc os valores de peso na lista
#print('')
#print('O Maior peso foi:', max(lst))  #maximo valor da lista
#print('O Menor peso foi:', min(lst))  #minimo valor da lista
