n = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze','Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesis', 'Dezesete', 'dezoito', 'dezenove','Vinte'
while True :
    x = int(input(print("Digite um númedo de 0 até 20: ")))
    while x > 20 or x < 0:
        if x > 20:
            x = int(input(print("Digite um número que seja menor que 20 e maior que 0, por favor!")))
        if x < 0:
            x = int(input(print("Digite um número que seja maior que 0 e menor que 20, por favor!")))
        if x <= 20 and x >= 0:
            break
    print(n[x])
    # r de resposta, é strip para ignorar os espaços e upper para deixar tudo maiusculo 
    r = input(print("Deseja continar ? [sim ou não] ")).strip().upper()
    # usar o upper para deixar maiusculo é o '[]' para pegar apenas a primera letra 
    r2 = r[0]
    if r2 == "N":
        break
    while r2 !="N" and r2 !="S":
    #if r2 != "N" and r2 != "S":
        r = input(print("Por favor digite sim ou não.")).strip().upper
        r2 = r[0]
print("Fim do programa") 