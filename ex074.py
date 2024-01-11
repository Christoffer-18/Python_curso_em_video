import random 
x = 0 
# o tuple transforma o alista em uma tupla 
#o randintvem da biblioteca aléatoria(random )
tupla = tuple(random.randint(1, 100) for _ in range(5))
print(tupla)
'''maior2 = tupla[0]
menor2 = tupla[0]
while x < 5:
    maior = tupla[x]
    if maior > maior2:
        maior2 = maior
   
    menor = tupla[x]
    if menor < menor2:
        menor2 = menor
    x += 1
print(f"O maior número da tupla é: {maior2}")
print(f"O menor número da tupla é: {menor2}")'''
# OU VC SIMPLESMENTE FAZ ISSO
print(f"O maior número da tupla é: {max(tupla)}")
print(f"O menor número da tupla é: {min(tupla)}")
