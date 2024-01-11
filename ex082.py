lista = []
par = []
impar = []
while True:
    num = int(input(print("Digite um valor:")))
    lista.append(num)
    resp = input(print("Deseja continuar ? [S/N]")).upper().strip()
    while resp != "S" and resp != "N":
        resp = input(print("Erro!! Por favor digite [S/N]")).upper().strip()
    #1º forma q eu consegui
    teste = num % 2
    if teste == 0:
        par.append(num)
    else:
        impar.append(num)
    if resp == "N":
        break
print(f"A lista completa é essa: {lista}")
if len(par) > 0: 
    print(f"Os números pares da lista sãe esses: {par}")
if len(impar) > 0:
    print(f"Os números impares da lista são esses: {impar}")