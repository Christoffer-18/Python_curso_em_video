def leiaDinheiro(x):
    while True:
        num = str(input(x)).replace(',','.').strip()
        if num.isalpha():
            print(f'\033[0;31mERRO "{num}" é um preço inválido!\033[m')
        else:
            num = float(num)
            return num
