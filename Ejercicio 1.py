mi_diccionario = {
    'a': 10.5,
    'b': 2.3,
    'c': 5.1,
    'd': 8.8
}
if all(isinstance(valor, float) for valor in mi_diccionario.values()):
    valores = list(mi_diccionario.values())
    valores_ordenados = sorted(valores)
    for valor in valores_ordenados:
        print(valor)
else:
    print("Todos los valores deben ser flotantes.")
