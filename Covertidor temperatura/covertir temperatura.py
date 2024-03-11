def convertir_temperatura(celsius):
    fahrenheit = celsius * 9/5 + 32
    kelvin = celsius + 273.15
    return (fahrenheit, kelvin)

grados_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit, kelvin = convertir_temperatura(grados_celsius)
print(f"{grados_celsius} grados Celsius son {fahrenheit} grados Fahrenheit y {kelvin} grados Kelvin.")