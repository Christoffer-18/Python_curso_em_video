lista = []
# primeira solução, grande de mais.... 
"""num = int(input(print("Digite um número:")))
lista.append(num)
print("Adicionado ao final da lista...")"""
for i in range(5):
    num = int(input(print("Digite um número:")))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print("Adicionado ao final da lista...")
    else:
        x = 0
        while x < len(lista):
            if num <= lista[x]:
                lista.insert(x, num)
                print(f"Adicionado na posição {i}")
                break
            x +=1 
print(lista)