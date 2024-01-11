dados = []
usuarios = []
pesos = []
while True:
    # adicinar usúarios
    usuarios.append(str(input("Digite o nome: ")))
    usuarios.append(float(input("Digite o peso: ")))
    pesos.append(usuarios[1])
    dados.append(usuarios[:])
    usuarios.clear()
    #para verificar a resposta
    resp = str(input("Deseja continuar? [S/N]")).upper().strip()
    print("---"*25)
    while resp != "S" and resp != "N":
        resp = str(input("Opção inválida, por favor digite [S/N]!")).upper().strip()
    if resp == "N":
        break
# verificando, mais pesados e mais leves 
print(dados)
print(f"Ao todo, foram cadastradas {len(dados)} pessoas no sistema.")
print(f"O maior peso foi de {max(pesos):.2f}Kg. Peso de", end=" ")
for i in dados:
    if i[1] == max(pesos):
        print(f"[{i[0]}]", end=" ")
print(f"\nO menor peso foi de {min(pesos):.2f}Kg. Peso de", end=" ")
for i in dados: 
    if i[1] == min(pesos):
        print(f"[{i[0]}]", end=" ")
