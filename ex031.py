#Custo da Viagem

p = float(input('Digite a distância da sua viagem em km:'))
print(f'Você está prestes a começar uma viagem de {p}km. ')
if p < 200:
    print(f'O preço da passagem é de {p * 0.5:.2f}')
else:
    print(f'O preço da passagem é de {p * 0.45:.2f}')
