#fazer a tupla ler 4 número do teclado
tupla = ()
#nove = 0
pares =()
contpar = 0
print("Vamos completar uma tupla com 4 números:\n")
for i in range(4):
    valor = int(input(print(f"Digite o {i+1}º número :")))
    #que o valor digitado é colocado entre parênteses para criar uma tupla com apenas um elemento
    tupla += (valor,)
print(tupla)
# para ver se tem o número nove na tupla
"""for x in range(4):
    if tupla[x] == 9:
        nove += 1
if nove == 0:
    print("Não foi possível encontrao o número 9 na tupla.")
if nove == 1:
     print(f"O número nove foi digitado {nove} vez.")
if nove != 0 and nove != 1:
    print(f"O número nove foi digitado {nove} vezes.")"""
# OU VC FAZ ISSO SEU ANIMAL BURRO 
contnove = tupla.count(9)
if contnove == 0:
    print(f"Não foi possivel encontar o número 9 na tupla.")
elif contnove == 1:
    print(f"O número nove foi digitado {contnove} vez")
else:
    print(f"O número nove foi digitado {contnove} vezes ")
# para ver se o número 3 está na tupla
try:
    #.index(x) mostra em qual posição o x apareceu pela primeira vez 
    tres = tupla.index(3)
    print(f"O número 3 está na posição: {tres+1}")
except ValueError:
    print("O número 3 não foi encontrado na tupla.")
#OUTRA FORMA É ASSIM:
"""if 3 in tupla:
    print(f"O valor 3 apareceu {tupla.index(3)+1} vezes")
else
    print("O valor 3 não foi digitado em nenhuma posição")"""
#Quais foram os números pares 
for x in range(4):
    if tupla[x]%2 == 0:
        par = tupla[x]
        pares += (par,)
        contpar += 1
if contpar == 1:
    print(f"Foi digitado {contpar} número par")
    print(f"Os números pares da tupla são {pares}")
elif contpar > 1:
    print(f"Foram digitados {contpar} números pares")
    print(f"Os números pares da tupla são: {pares}")
else:
    print("Não tem número par na tupla")