from pacotes import moedas

num = int(input("Digite o preço: R$"))
print(f"A metade de {num} é {moedas.metade(num)}")
print(f"O dobro de {num} é {moedas.dobro(num):.1f}")
print(f"Aumentando 10%, temos {moedas.aumentar(num,10)}")
print(f"Reduzindo 13%, temos {moedas.diminuindo(num,13)}")