#Analisando Triângulo v1.0

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
a = float(input('digite o comprimento da primeira reta:'))
b = float(input('digite o comprimento da segunda reta:'))
c = float(input('digite o comprimento da terceira reta:'))
if b + c > a and a + c > b and a + b > c:
    print('Os números digitados PODEM FORMAR um triângulo!')
else:
    print('Os números digitados NÃO PODEM FORMAR um triangulo!')