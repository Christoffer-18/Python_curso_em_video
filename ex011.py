#  Pintando Parede

a = float(input('Qual é a altura da parede?'))
l = float(input('Qual é a largura da parede?'))
t = float(input('Quantos metros a lata de tinta pinta?'))
p = int(input('quantas paredes tem no cômodo?'))
t1 = (a*l)/2
print(f"Sua  parede tem a dimensão de {l}x{a} e sua área e de {a*l:.2f}m²"
    f"\nPara pintar essa parede,você vai precisar de {t1:.2f}l de tinta"
    f"\nNas paredes do cômodo vão ser {t1*p:.2f}l de tinta" )