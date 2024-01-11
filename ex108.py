from pacotes import moedas2

num = float(input("Digite o preço: R$"))
print(f"A metade de {moedas2.moeda(num)} é {moedas2.moeda(moedas2.metade(num))}")
print(f"O dobro de {moedas2.moeda(num)} é {moedas2.moeda(moedas2.dobro(num))}")
print(f"Aumentando 10%, temos {moedas2.moeda(moedas2.aumentar(num,10))}")
print(f"Reduzindo 13%, temos {moedas2.moeda(moedas2.diminuindo(num,13))}")
