# 1. Crear un diccionario
informacion_personal ={
    "nombre": "Bryan",
    "edad": 27,
    "ciudad": "Quito",
    "profesion": "Policia"
}

# 2. Acceder y modificar valores
informacion_personal["ciudad"] = "Quito"  # Modificar valor de la clave "ciudad"
informacion_personal["profesion"] = "Policia"  # Agregar nueva clave "profesion"

# 3. Verificar existencia de claves y agregar si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0981234567"  # Agregar clave "telefono" con un número ficticio

# 4. Eliminar una clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminar clave "edad"

# 5. Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)