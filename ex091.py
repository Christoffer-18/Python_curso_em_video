from random import randint
from time import sleep 
from operator import itemgetter

# minha primeira solução:
'''jogador, gambiarra = {}, []
#criando os números 
for i in range(0,4):
    x = random.randint(1,6)
    gambiarra.append(x)
#colocando em um dicionário
for i in range(0,4):
    jogador[f"jogador {i+1}"] = gambiarra[i]
#mostrando os resultados
for k, v in jogador.items():
    print(f"O {k} tirou {v} no dado.")
    sleep(1)
print("+=+"*30)
print("     O RANKING DOS JOGADORES")
x = 1
for t in sorted(jogador, key = jogador.get, reverse=True):
    print(f"O {x}º lugar: {t} com {jogador[t]}")
    x+=1'''
#solução do professor:'
jogo = {'jogador1' : randint(1,6),
        'jogador2' : randint(1,6),
        'jogador3' : randint(1,6),
        'jogador4' : randint(1,6)}
ranking = dict()
print("Valores sorteados:")
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("+++"*20)
for i, v in enumerate(ranking):
    print(f" {i+1} lugar: {v[0]} com {v[1]}")