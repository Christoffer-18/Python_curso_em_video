def notas(*valor, sit = False):
    """
    -> Função para analisar notas e situaqções de vários alunos
    valor = Uma ou mais notas dos alunos(aceigta várias)
    sit: Valor opcional, indicamos se deve ou não adicionar a sitiação
    return = Dicionário com várias informações sobre a situação da turma.
    """
    print("---"*10)
    dic = dict()
    dic["Total:"] = len(valor)
    #Forma mais longa
    '''maxi = valor[0]
    mini = valor[0]
    for c in range(len(valor)):
        print(f"{valor[c]}")
        if valor[c] > maxi:
            maxi = valor[c]
        if valor[c] < mini:
            mini = valor[c]
    dic["Maior:"] = maxi
    dic["Menor:"] = mini'''
    dic["Maior:"] = max(valor)
    dic["Menor:"] = min(valor)
    #Forma mais longa
    '''soma = 0
    for c in valor:
        soma += c
    media = soma/len(valor)
    dic["Média:"] = media'''
    dic["Média:"] = sum(valor)/len(valor)
    if sit:
        if dic["Média:"] >= 7:
            dic["Situação:"] = "BOA"
        elif dic["Média:"] >=5:
            dic["Situação:"] = "RAZOÁVEL"
        else:
            dic["Situação:"] = "RUIM"
    return dic


resp = notas(5.5, 2.5, 8.5)
print(resp)
help(notas)