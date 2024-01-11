from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print("+=+" * 20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    sleep(2.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont}", end=" ", flush=True)
            sleep(0.5)
            cont += passo
        print("FIM!")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont}", end=" ", flush=True)
            sleep(0.5)
            cont -= passo
        print("Fim!")
        
contador(1,10,1)
contador(0,10,2)
print("+=+" * 20)
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("inicio: "))
fim = int(input("Fim: "))
passo = int(input("De quntos em quantos: "))
contador(inicio,fim,passo)