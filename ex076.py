tupla = "Lápis", 1.75, "borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livros", 34.90
print("-----"*10)
print(" "*13,"LISTAGEM DE PREÇO")
print("-----"*10)
x = 0
while x < len(tupla):
    if x % 2 == 0:
        print(f"{tupla[x]:.<38}  R${tupla[x+1]:>8.2f}")
    x += 1
print("-----"*10)