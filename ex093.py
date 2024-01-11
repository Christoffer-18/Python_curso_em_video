x = 0
dic = {}
#coletar informações
dic["Nome"] = str(input("Nome do jogador: "))
aux = int(input(f"Quantas partidas {dic['Nome']} jogou? "))
lista = [int(input(f"Quantos gols na {i+1}º partida? "))for i in range(0,aux)]
#uma forma de achar o total
'''for i in lista:
    x += i
dic['total'] = x'''
#outra forma de achar o total
dic['total'] = sum(lista)
dic['gols'] = lista
print("=+="*30)
print(dic)
print("=+="*30)
#mostrando os resultados 
for k, v in dic.items():
    print(f"O campo {k} tem o valor {v}.")
print("=+="*30)
print(f"O jogador {dic['Nome']} jogou {aux} partidas.")
for i in range(len(lista)):
    print(f"  => Na partida {i+1}, ele fez {dic['gols'][i]}.")
print(f"Foi um total de {dic['total']} gols.")