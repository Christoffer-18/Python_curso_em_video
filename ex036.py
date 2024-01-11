#

v = float(input('Qual é o valor do imóvel?R$'))  #valor
s = float(input('Qual é a sua renda?R$'))  #salario
a = float(input('Em quantos anos você deseja pagar?'))  #vezes dividido
c = v /(a * 12) #conta
m = a * 12
p = (s * 30)/ 100 #porcentagem
if c > p:
    print(f'\033[31;1mDesculpa, seu empréstimo foi negado!!\n'
          f'O seu pedido ultrapassa os 30% do seu salário.')
else:
    print(f'\033[32;1mParabéns, seu empréstimo foi aceito!!\n'
          f'Vão ser {m:.0f} parceals de R${c:.2f}!! ')