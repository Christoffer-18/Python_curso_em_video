lista = []
cinco = "não contém"
while True:
    lista.append(int(input("Digite um valor: ")))
    '''num = int(input(print("Digite um valor:")))
    lista.append(num)'''
    #Ao invés de usar 2 linhas simplicica e usa apenas uma 
    resp = str(input(print("Deseja continuar ? [S/N] "))).upper().strip()
    while resp != "S" and resp != "N":
        resp = input(print("Erro!! Por favor digite [S/N]")).upper().strip()
    if 5 in lista:
        cinco = "contém"
    if resp == "N":
        break
lista.sort(reverse=True)
print(f"A quantidade de números digitados foram {len(lista)}")
print(lista)
print(f"Na lista {cinco} o número 5.")