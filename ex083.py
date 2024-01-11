x = input(print("Digite a expressão:"))
y = 0 
cont = 0
cont2 = 0
while y < len(x):
    if x[y] == "(":
        cont += 1
    if x[y] == ")":
        cont2 += 1
    y += 1
if cont == cont2:
    print("Correto")
else:
    print("Errado")