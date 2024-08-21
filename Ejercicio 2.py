diccionario_a = {
    'a': 10,
    'b': 2,
    'c': 5
}

diccionario_b = {
    'a': 10,
    'b': 2,
    'c': 5,
    'd': 8
}
def verificar_claves_valores(diccionario_a, diccionario_b):
    for clave, valor in diccionario_a.items():
        if diccionario_b.get(clave) != valor:
            return False
    return True
resultado = verificar_claves_valores(diccionario_a, diccionario_b)
print("Todos los pares clave-valor están en el segundo diccionario:", resultado,)
