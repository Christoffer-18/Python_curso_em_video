# Aluguel de Carros

d = float(input('O automóvel foi alugado por quantos dias?'))
km = float(input('Ele percorreu quantos km?'))
print(f'O total a pagar é de {(d * 60) + (km * 0.15):.2f}')