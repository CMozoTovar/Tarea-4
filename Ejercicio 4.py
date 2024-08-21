def personas_en_rango(personas, edad_minima, edad_maxima):
    for persona in personas:
        edad = persona.get("edad")
        if edad_minima <= edad <= edad_maxima:
            nombres = persona.get("nombres")
            apellidos = persona.get("apellidos")
            print(f"Nombres: {nombres}, Apellidos: {apellidos}")

personas = [
    {"nombres": "Santiago", "apellidos": "Coy Torres", "edad": 101},
    {"nombres": "Ana María", "apellidos": "Gómez Bolaños", "edad": 69},
    {"nombres": "Carlos Santiago", "apellidos": "Mozo Tovar", "edad": 25},
    {"nombres": "María Clara", "apellidos": "Martínez López", "edad": 45},
    {"nombres": "Lionel Andrés", "apellidos": "Messi Cuccittini", "edad": 37},
]
edad_minima = 20
edad_maxima = 50
personas_en_rango(personas, edad_minima, edad_maxima)
