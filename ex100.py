from time import sleep
from random import randint

def aleatorio(num):
    print("Os 5 números sorteados foram: ", end="")
    for i in range(5):
        x = int(randint(0,9))
        print(f"{x}", end=" ", flush=True)
        sleep(0.5)
        lista.append(x)
        if x % 2 == 0:
            par.append(x)
    print("PRONTO!")

def soma(teste):
    somap = 0
    for p in par:
        somap += p
    print(f"Somando os valores pares da lista {lista}, temos o resultado: {somap}.")

lista, par = [], []
aleatorio(lista)
soma(par)
