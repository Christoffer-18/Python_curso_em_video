lista = []
while True:
    num = int(input(print("Digite um número: ")))
    if num not in lista:
        lista.append(num)
        print("Número adicionado.")
    else:
        print("Valor repetido! NÃO irei adicionar!!!")
    # minha primeira solução
    """if num in lista:
        print("Número já adicionado, NÃO irei adicionar.")
        lista.remove(num)"""
    r = input(print("Quer continuar? [S/N]")).upper().strip()
    rcurta = r[0]
    while rcurta != "N" and rcurta != "S":
        r = input(print("Por favor digite SIM ou NÃO!")).strip().upper()
        rcurta = r[0]
    if rcurta == "N":
        break
lista.sort()
print(lista)
