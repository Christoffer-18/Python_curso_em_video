# SIMPLIFICANDO A FORMA DE CHAMAR PACOTES
# 1ª FORMA UMA FORMA BEM SIMPLES, PORÉM SE TIVER MUITAS FUNÇÕES PODE SE TORNAR DÍFICIL DE MEXER 

'''from pacotes.moedas4 import moeda, metade, dobro, aumentar,diminuir

num = float(input("Digite o preço: R$"))
print(f"A metade de {moeda(num)} é {moeda(metade(num))}")
print(f"O dobro de {moeda(num)} é {moeda(dobro(num))}")
print(f"Aumentando 10%, temos {moeda(aumentar(num,10))}")
print(f"Reduzindo 13%, temos {moeda(diminuir(num,13))}")'''

# 2ª FORMA ELE RETORNA COM UMA CONDIÇÃO, O QUE TORNA MAIS FÁCIL É VISIVEL DO QUE NO EX 108

from pacotes import moedas4

num = float(input("Digite o preço: R$"))
print(f"A metade de {moedas4.moeda(num)} é {moedas4.metade(num, True)}")
print(f"O dobro de {moedas4.moeda(num)} é {moedas4.dobro(num,True)}")
print(f"Aumentando 10%, temos {moedas4.aumentar(num,10,True)}")
print(f"Reduzindo 13%, temos {moedas4.diminuir(num,13,True)}")
