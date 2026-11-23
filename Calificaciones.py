def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("Escribe un número mayor que 0.")
        except ValueError:
            print("No es válido. Escribe un número entero.")


def pedir_calificacion(mensaje):
    while True:
        try:
            calificacion = float(input(mensaje))
            if 0 <= calificacion <= 100:
                return calificacion
            print("  La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("No es válido. Escribe un número.")


# 1. Datos del grupo
num_estudiantes = pedir_entero("¿Cuántos estudiantes hay en el grupo? ")
num_materias = pedir_entero("¿Cuántas materias tiene el grupo? ")

# 2. Captura de la matriz (filas = estudiantes, columnas = materias)
matriz = []
for i in range(num_estudiantes):
    print(f"\n--- Estudiante {i + 1} ---")
    fila = []
    for j in range(num_materias):
        nota = pedir_calificacion(f"  Calificación en la materia {j + 1}: ")
        fila.append(nota)
    matriz.append(fila)

# 3. Cálculos
promedios_estudiantes = []
for fila in matriz:
    promedios_estudiantes.append(sum(fila) / num_materias)


promedios_materias = []
for j in range(num_materias):
    suma = 0
    for i in range(num_estudiantes):
        suma += matriz[i][j]
    promedios_materias.append(suma / num_estudiantes)


mas_alta = matriz[0][0]
mas_baja = matriz[0][0]
for fila in matriz:
    for nota in fila:
        if nota > mas_alta:
            mas_alta = nota
        if nota < mas_baja:
            mas_baja = nota

# 4. Resultados
print("\n" + "=" * 30)
print("        MATRIZ DE CALIFICACIONES")
print("=" * 30)
encabezado = "Estudiante".ljust(12)
for j in range(num_materias):
    encabezado += f"Mat {j + 1}".rjust(8)
print(encabezado)
print("-" * len(encabezado))
for i, fila in enumerate(matriz):
    linea = f"Est {i + 1}".ljust(12)
    for nota in fila:
        linea += f"{nota:8.1f}"
    print(linea)

print("\n" + "=" * 30)
print("        PROMEDIO POR ESTUDIANTE")
print("=" * 30)
for i, promedio in enumerate(promedios_estudiantes):
    print(f"Estudiante {i + 1}: {promedio:.2f}")

print("\n" + "=" * 30)
print("         PROMEDIO POR MATERIA")
print("=" * 30)
for j, promedio in enumerate(promedios_materias):
    print(f"Materia {j + 1}: {promedio:.2f}")


print("\n" + "=" * 30)
print("          EXTREMOS DEL GRUPO")
print("=" * 30)
print(f"Calificación más alta: {mas_alta:.1f}")
print(f"Calificación más baja: {mas_baja:.1f}")
print("=" * 30)