import random
import time
lista, matriz = [], []
print("=+=" * 20)
print(" " * 15, "JOGO DA LOTERIA")
print("=+=" * 20)
aux = int(input("Quantos jogos vc quer que eu sorteie? "))
# repetição e criação dos números aleatórios
print("=+=" * 5, f" SORTEANDO {aux} JOGOS ", "=+=" * 5)
for i in range(0, aux):
    while len(lista) != 6:
        aux1 = random.randint(1, 60)
        if aux1 not in lista:
            lista.append(aux1)
    lista.sort()
    matriz.append(lista[:])
    lista.clear()
for i in range(0, aux):
    time.sleep(1)
    print(f"Jogo {i+1}:{matriz[i]}")
print("=+=" * 5, "BOA SORTE", "=+=" * 5)
