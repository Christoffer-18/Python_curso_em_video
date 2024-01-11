lista, dic = [], {}
#cadastrando pessoas 
soma = 0
while True:
    dic.clear()
    dic['nome'] = str(input("Nome: ")).strip()
    dic['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while dic['sexo'] != "M" and dic['sexo'] != "F":
        dic['sexo'] = str(input("Erro!! Por favor digitar [M/F]")).strip().upper()[0]
    dic['idade'] = int(input("Idade: "))
    soma += dic['idade']
    lista.append(dic.copy())
    resp = str(input("Deseja continuar? [S/N]")).upper()[0].strip()
    while resp != "N" and resp != "S":
        resp = str(input("Erro !! Por favor digitar [S/N]!")).upper()[0].strip()
    if resp == "N":
        break
    print("=+="*20)
#analisando os dados 
media = soma/len(lista)
print(f"A) Foram cadastradas {len(lista)} pessoas.")
print(f"B) A média de idade é de {media:.2f} anos.")
print(f"C) As mulheres cadastradas foram", end=' ')
for i in lista:
    if i['sexo'] == 'F':
            print(f'{i["nome"]}', end=' ')
print(f"D) Lista de pessoas que estão acima da média: ", end=" ")
print(" ")
for i in lista:
    if i['idade'] >= media:
        print(f"    ", end="")
        for k, v in i.items():
            print(f"{k} = {v}", end=" ")
        print()
print("<< ENCERRANDO >>")