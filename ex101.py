def idade(a):
    from datetime import date 
    data = date.today().year
    idade_atual = data - a
    if 16 >= idade_atual < 18 or idade_atual >=65:
        return(f"Com {idade_atual} anos o voto é opicional.")
    elif idade_atual < 16:
        return(f"Com {idade_atual} anos você não pode votar.")
    else:
        return(f"Com {idade_atual} anos o voto é obrigatório.")
    
print("---"*10)
ano = int(input("Em que ano você nasceu? "))
print(idade(ano))
