from datetime import date
dados ={}
dia = date.today().year
#pegar os dados
while True:
    dados['nome'] = str(input("Nome: ")).strip()
    dados['idade'] = dia - int(input("Ano de nascimento: "))
    dados['ctps'] = int(input("Carteira de trabalho (digite 0 se não tiver): "))
    if dados['ctps'] == 0:
        break
    dados['ano'] = int(input("Ano de contratação: "))
    dados['salário'] = float(input("Salário: "))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano'] + 35) - dia)
    break
print("=+="*30)
for k,v in dados.items():
    print(f"- {k} tem o valor {v}")