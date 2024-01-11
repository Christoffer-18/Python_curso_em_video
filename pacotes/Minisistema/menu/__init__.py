import time

def leiaint(mens):
    while True:
        try:
            resposta = int(input(mens))
        except(ValueError, TypeError):
            print("\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[m")
        except KeyboardInterrupt:
            print('\n\033[0;31musuário preferiu não informar esse número.\033[m')
            break
        else:
            return resposta

def escrita(x = str):
    print("-"*40)
    print(f"{x}".center(40))
    print("-"*40)

def menu(lista):
    escrita('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c+=1
    print("-"*40)
    opc = leiaint('Sua Opção: ')
    return opc