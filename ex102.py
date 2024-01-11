def fatorial(f=1, show = False):
    '''
    -> calculo fatorial de um número.
    f = O número a ser calculado
    booleana = para mostrar ou não a conta
    return = trás de volta o valor fatorial de f
    '''
    
    aux = 1
    print("---"*10)
    if show == False:
        for c in range(f, 0, -1):
            aux *=c
        return aux
    else:
        for c in range(f, 0, -1):
            if c == 1:
                print(f"{c}", end=" ")
            else:
                print(f"{c} x", end=" ")
            aux *= c 
        return (f" = {aux}")

#show = True
print(fatorial(5, False))
#help(fatorial)