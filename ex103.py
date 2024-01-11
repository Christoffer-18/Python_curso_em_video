def ficha(jogador ="<desconhecido>", gols=0 ):
    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")
    

print("---"*10)
nome = str(input("Digite o nome do jogador: "))
num = str(input("Quantos gols ele fez? "))
if num.isnumeric():
    num = int(num)
else:
    num = 0
if nome.strip()=="":
    ficha(gols=num)
else:
    ficha(nome,num)