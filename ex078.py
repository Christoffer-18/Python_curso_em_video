lista = [int(input(print(f"Digite o {i+1}º número da lista:"))) for i in range(5)]
print(lista)
print(f"O maior número da lista é {max(lista)} e está localizado na posição ", end=" ")
for p, v in enumerate(lista):
    if v == max(lista):
        posicao = p + 1
        print(f"{posicao}... ", end=" ")
print(f"\nO menor número da lista é {min(lista)} e está localizado na posição ", end=" ")
for p, v in enumerate(lista):
    if v == min(lista):
        posicaomin = p + 1
        print(f"{posicaomin}... ", end=" ")