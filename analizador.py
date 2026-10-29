
def analizar_token(cadena):
    cadena = cadena.strip()

    if not cadena:
        return "Cadena vacía"

    estado = 0
    i = 0

    operadores = {'+', '-', '*', '/', '=', '<', '>', '%'}
    palabras_r = {'COMIENZO', 'ENTERO', 'MOSTRAR', 'SI', 'SINO', 'Y'}

    while i < len(cadena):
        c = cadena[i]

        if estado == 0:
            if c.isalpha() or c == '_':
                if c.isupper():
                    estado = 5
                else:
                    estado = 1
            elif c.isdigit():
                estado = 2
            elif c in operadores:
                estado = 4
            else:
                return "No válido / Desconocido"

        elif estado == 1:  # Identificador
            if not (c.isalnum() or c == '_'):
                return "Identificador no válido"

        elif estado == 2:  # Número entero
            if c == '.':
                estado = 3
            elif not c.isdigit():
                return "Número no válido"

        elif estado == 3:  # Número decimal
            if not c.isdigit():
                return "Número decimal no válido"

        elif estado == 4:  # Operador
            return "Operador no válido (demasiados caracteres)"

        elif estado == 5:  # Palabra reservada
            if c.isupper():
                estado = 5
            elif c.isalnum() or c == '_':
                estado = 1
            else:
                return "Identificador no válido"        
       
        i += 1

    # Clasificación final
    if estado == 5:
        if cadena in palabras_r:
            return "Palabra reservada válida"
        return "Identificador válido"
    elif estado == 1:
        return "Identificador válido"
    elif estado == 2:
        return "Número entero válido"
    elif estado == 3:
        if cadena.endswith('.'):
            return "Número decimal no válido"
        return "Número decimal válido"
    elif estado == 4:
        return "Operador válido"

    return "Cadena no válida"


# Pruebas
entradas = [
    "variable1", "125", "45.a67", "+", "_contador",
    "99num", "+++", "COMIENZO", "Car8", "Y"
]

for e in entradas:
    print(f"'{e}' -> {analizar_token(e)}")
