# EX 109

def metade(n=0 , formato = False):
    res = n / 2
    return res if formato is False else moeda(res)

def dobro(n=0, formato = False):
    res = n * 2
    return res if formato is False else moeda(res)

def aumentar(n=0, por=0, formato = False):
    res = (n * por) / 100 + n
    return res if formato is False else moeda(res)

def diminuir(n=0, por=0, formato = False):
    res = ((n*por)/100 -n)*-1
    return res if formato is False else moeda(res)

def moeda(preço = 0, moeda='R$'):
    return f"{moeda}{preço:.2f}".replace('.',',')