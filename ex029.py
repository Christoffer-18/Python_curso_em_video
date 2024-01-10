# Radar eletrônico

v = int(input('Digite a velocidade em que você estava:'))
if v > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h\n'
          f'Você deve pagar uma multa de R${(v-80)*7:.2f}!')
print('Tenha um Bom Dia, dirija com segurança!')
