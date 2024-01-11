matriz = []
soma = soma1 = maxi = 0
for i in range(0, 3):
    linhas = [int(input(f"Digite um valor para [{i}, {l}]: ")) for l in range(3)]
    matriz.append(linhas[:])
    linhas.clear()
print("=-="*20)
for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:0>3}]", end=" ")
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
        if j == 2:
            soma1 += matriz[i][j]
    print()
print("")
print("=-="*20)
print(f"A soma dos valores pares é {soma}")
print(f"A soma dos valores da terceira coluna é {soma1}")
#print(f"O maior valor da segunda linha é {max(matriz[1])}") o jeito mais fácil
for c in range(0,3):
    if c == 0:
        maxi = matriz[1][c]
    elif matriz[1][c] > maxi:
        maxi= matriz[1][c]
print(f"O maior valor da segunda linha é {maxi}.")
