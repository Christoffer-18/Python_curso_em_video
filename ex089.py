dados, x = [], []
while True:
    suporte = str(input("Nome: "))
    x.append(suporte)
    suporte1 = float(input("Nota 1 : "))
    x.append(suporte1)
    suporte2= float(input("Nota 2 : "))
    x.append(suporte2)
    dados.append(x[:])
    x.clear()
    resp = str(input("Quer continuar? [S/N]")).upper().strip()
    while resp != "S" and resp != "N":
        resp = str(input("Erro!! Digite [S/N]")).upper().strip()
    if resp == "N":
        break
# Tabelinha mostrando a media     
print("=+="*20)
print("COD.   NOME"," "*10,"MÉDIA")
print("---"*20)
for i in range(len(dados)):
    media = (dados[i][1] + dados[i][2])/2
    print(f"{i:<4}   {dados[i][0]:<15} {media:>8.2f}")
print("---"*20)
# mostrando nota de alunos expecificos
while True:
    cod = int(input("Mostar a nota de qual aluno? (DIGITE 999 PARA ENCERRAR O PROGRAMA)"))
    if cod == 999:
        break
    # se o cod não tiver registrado o programa não deixa proseguir 
    while cod < 0 or cod > (len(dados)):
        cod = int(input("Código inválido, por favor digitar um válido "))
        if cod == 999:
            break
    if cod != 999:
        print(f"As notas de {dados[cod][0]} foram [{dados[cod][1]}, {dados[cod][2]}]")
print("FIM!")