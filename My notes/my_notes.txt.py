# 1. Escritura de Archivo de Texto:
# Crear un nuevo archivo llamado my_notes.txt y escribir al menos tres líneas de notas personales en el archivo.

with open("my_notes.txt", "w") as file:
    file.write("1. El lunes empezamos examenes en la UEA toca estudiar.\n")
    file.write("2. Comprar un regalo a mi hermana por su cumpleaños.\n")
    file.write("3. Tener todo lista para semana santa, llegan familiares a casa.\n")

# 2. Lectura de Archivo de Texto:
# Abrir el archivo my_notes.txt, leer el contenido del archivo línea por línea y mostrar cada línea leída en la consola.

with open("my_notes.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() elimina el carácter de nueva línea al final de cada línea

# 3. Cierre de Archivos:
# Cerrar el archivo my_notes.txt después de realizar las operaciones necesarias.
# No es necesario cerrar explícitamente el archivo cuando se usa la estructura "with open()".

# El archivo se cierra automáticamente al salir del bloque "with".