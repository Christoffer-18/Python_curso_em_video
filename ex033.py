#Maior e menor valores

a = float(input('digite o primeiro número:'))
b = float(input('Digite o segundo número:'))
c = float(input('Digite o ultimo número:'))
m = a # verificando qual é o menor.
if b < a and b < c:
    m = b
if c < a and c < b:
    m = c
m2 = b #verificando qual e o maior
if a > b and a > b:
    m2 = a
if c > b and c > b:
    m2 = c
print(f'O maior valor digitado foi {m2:.0f}')
print(f'O menor valor digitado foi {m:.0f}')

