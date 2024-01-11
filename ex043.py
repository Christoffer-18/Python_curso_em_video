p = float(input('Digite seu peso:(Kg)'))
a = float(input('Digite o sua atura (em metros):'))
imc = p / a ** 2
print(f'O seu IMC é de {imc:.1f}')
if imc < 18.5:
    print(f'\033[31mIsso significa que você esta ABAIXO DO PESO!, procure um médico!!')
elif 18.5 > imc < 25:
    print('\033[32mIsso significa que você esta no PESO IDEAL!, Parabéns!!')
elif imc > 25 and imc < 30:
    print("\033[33mIsso significa que você esta com SOBREPESO!, prucure um médico!!")
elif imc > 30 and imc < 40:
    print('\033[31mIsso significa que você esta com OBESIDADE!!, procure um médico!!')
else:
    print('\033[1;31mISSO SIGNIFICA QUE VOCÊ ESTA COM OBESIDADE MÓRBIDA, PROCURE UM MÉDICO IMEDIATAMENTE!!')