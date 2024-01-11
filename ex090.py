dic = {}
# pegando as informações 
dic["Nome"] = str(input("Nome: "))
dic["Média"] = float(input(f"Média de {dic['Nome']}: "))
# verificando se está aprovado, média tem que ser mais de 7
if dic["Média"] >= 7:
    dic["Situação"] = "Aprovado"
elif 5<= dic["Média"] < 7:
    dic["Situação"] = "Recuperação" 
else:
    dic["Situação"] = "Reprovado"
print("+++"*20)
for k, v in dic.items():
    print(f"{k} é igual a {v}")