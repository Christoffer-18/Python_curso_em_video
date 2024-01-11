# EX 108

def metade(n=0):
    res = n / 2
    return res

def dobro(n=0):
    res = n * 2
    return res

def aumentar(n=0, por=0):
    res = (n * por) / 100 + n
    return res

def diminuir(n=0, por=0):
    res = ((n*por)/100 -n)*-1
    return res

def moeda(preço = 0, moeda='R$'):
    return f"{moeda}{preço:.2f}".replace('.',',')