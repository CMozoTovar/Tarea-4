def mezclar_diccionarios(dic1, dic2):
    nuevo_diccionario = dic1.copy()
    for clave, valor in dic2.items():
        if clave not in nuevo_diccionario:
            nuevo_diccionario[clave] = valor
    
    return nuevo_diccionario

diccionario1 = {
    'a': 1,
    'b': 2,
    'c': 34,
    'd': 5,
    'e': 6
}

diccionario2 = {
    'a': 12,
    'b': 13,
    'c': 14,
    'd': 15,
    'e': 16
}

resultado = mezclar_diccionarios(diccionario1, diccionario2)
print(resultado)
