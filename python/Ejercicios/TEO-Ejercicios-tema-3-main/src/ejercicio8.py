nombres = ["Juan", "Ana", "Manuel", "Irene", "Jaime", "María"]
apellidos = ["Ruiz", "López", "Martínez", "Fernández", "Jiménez", "Castro"]
# La salida debe ser ['Juan Ruiz', 'Ana López', 'Manuel Martínez', 'Irene Fernández', 'Jaime Jiménez', 'María Castro']

nombres_completos = list(zip(nombres,apellidos))
nombres_completos2 = []
# TODO
for nombreCompleto in nombres_completos:
    nombres_completos2.append(nombreCompleto[0] + " " + nombreCompleto[1])
print(nombres_completos2)