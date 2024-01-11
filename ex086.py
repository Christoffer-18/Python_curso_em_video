matriz = []
soma = soma1 = 0
for i in range(0, 3):
    linhas = [int(input(f"Digite um valor para [{i}, {l}]: ")) for l in range(3)]
    matriz.append(linhas[:])
    linhas.clear()
print("=-="*20)
for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}]", end=" ")
        #if j == 2:
        #    print(" ") ou vc faz assim, que gasta apenas uma linha 
    print()    
print("=-="*20)
