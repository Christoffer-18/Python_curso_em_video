dic, lista, dados = {}, [], []
cont = 1
#coletar informações
while True:
    dic.clear()
    dic["nome"] = str(input("Nome do jogador: "))
    aux = int(input(f"Quantas partidas {dic['nome']} jogou? "))
    lista = [int(input(f"Quantos gols na {i+1}º partida? "))for i in range(0,aux)]
    dic['gols'] = lista[:]
    dic['total'] = sum(lista)
    dados.append(dic.copy())
    resp = str(input("Quer continuar? [S/N]")).upper()[0].strip()
    while resp != "N" and resp != "S":
        resp = str(input("Erro! Digite [S/N]!!")).upper()[0].strip()
    if resp == "N":
        break
#mostrando os resultados 
print("=+="*30)
print("Cod ", end=" ")
for i in dic.keys():
    print(f"{i:<15}", end=" ")
print()
print("---"*30)
for k, v in enumerate(dados):
    print(f"{k:>3} ", end=' ')
    for d in v.values():
        print(f"{str(d):<15}", end=" ")
    print()
print("---"*30)
while True:
    cod = int(input("Mostrar dados de qual jogador (999 para parar) "))
    if cod == 999:
        break
    while cod >= len(dados):
        cod =int(input(f"Erro! Não existe jogador com o código {cod}, por favor digite outro código! "))
    print(f"-- LEVANTAMENTO DO JOGADOR {dados[cod]['nome']}:")
    for i , g in enumerate(dados[cod]['gols']):
        print(f"    No jogo {i+1} fez {g} gols.")
    print('---'*30)
print("Volte sempre")