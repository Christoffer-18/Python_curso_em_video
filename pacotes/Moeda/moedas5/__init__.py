# EX 110

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

def resumo(n = 0, aum = 0, dim = 0):
    print(f"-"*30)
    print(f"RESUMO DO VALOR".center(30))
    print(f"-"*30)
    print(f"Preço analisado: \t{moeda(n)}")
    print(f"Dobro do preço: \t{moeda(dobro(n))}")
    print(f"Metade do preço: \t{moeda(metade(n))}")
    print(f"{aum}% de aumento: \t{moeda(aumentar(n, aum))}")
    print(f"{dim}% de redução: \t{moeda(diminuir(n, dim))}")
    print(f"-"*30)