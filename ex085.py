lista = [[],[]]
for i in range(0,7):
    num = int(input(f"Digite o {i+1}º valor:"))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print("=+="*30)
print(f"Os valores pares são: {sorted(lista[0])}")
print(f"OS valores impares são: {sorted(lista[1])}")