print('='* 30)
print('{:^30}'.format('Banco Py'))
print('='* 30)
valor = int(input("informe o valor a ser sacado R$ : "))

while (valor % 2 != 0) and (valor % 5 != 0) or (valor <= 0):
    print(f"\033[;;31mEsse valor é impsossível de ser sacado, por favor escolha um número terminado em 0,2 ou 5!\033[;;m")
    valor = int(input("Qual o valor que você deseja sacar R$?"))

""""nota200 = valor // 200
valor %= 100
nota100 = valor // 100
valor %= 100
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota5 = valor // 5
valor %= 5
nota2 = valor // 2''
if nota200 > 0:
    print(f"{nota200} nota(s) de R$200")
if nota100 > 0:
    print(f"{nota100} nota(s) de R$100")
if nota50 > 0:
    print(f"{nota50} nota(s) de R$50")
if nota20 > 0:
    print(f"{nota20} nota(s) de R$20")
if nota10 > 0:
    print(f"{nota10} nota(s) de R$10")
if nota5 > 0:
    print(f"{nota5} nota(s) de R$5")
if nota2 > 0:
    print(f"{nota2} nota(s) de R$2")""""" #jeito que eu fiz

# jeito do professor

total = valor
ced = 200
tot_ced = 0
while True:
    if total >= ced:
        total -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f"Total de {tot_ced} cédula(s) de R${ced}")
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        tot_ced = 0
        if total == 0:
            break
print('='* 30)
print(f"Volte sempre!")