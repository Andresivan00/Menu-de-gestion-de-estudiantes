# =====================================
# CÓDIGO COMPLETO EN PYTHON: GESTIÓN DE ESTUDIANTES CON MENÚ
# =====================================
# Este script crea un programa interactivo con un menú para gestionar estudiantes.
# Los datos se almacenan en un archivo de texto "estudiantes.txt" con formato: "nombre, programa" por línea.
# Usa pistas de códigos anteriores: manejo de archivos con open (mejorado con 'with' para cierre automático),
# bucles for/range, listas para leer líneas, y condicionales para búsquedas/eliminaciones.
# El menú se ejecuta en un bucle while hasta que el usuario elija salir.
# No requiere librerías externas; todo es Python estándar.
# Nota: Asume que el archivo puede no existir al inicio (se crea automáticamente al registrar).
# En caso de errores (e.g., archivo no encontrado al leer), se manejan con try-except básicos.
# =====================================

# Función principal para mostrar el menú y manejar opciones
def menu_principal():
    while True:  # Bucle infinito hasta que se elija salir
        print("\n=== MENÚ DE GESTIÓN DE ESTUDIANTES ===")
        print("1. Registrar estudiante")
        print("2. Mostrar lista de estudiantes")
        print("3. Buscar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        opcion = input("Elija una opción (1-5): ")  # Solicita entrada del usuario
        
        if opcion == '1':
            registrar_estudiante()  # Llama a la función de registro
        elif opcion == '2':
            mostrar_lista()  # Llama a la función de mostrar
        elif opcion == '3':
            buscar_estudiante()  # Llama a la función de búsqueda
        elif opcion == '4':
            eliminar_estudiante()  # Llama a la función de eliminación
        elif opcion == '5':
            print("Saliendo del programa...")  # Mensaje de salida
            break  # Sale del bucle while
        else:
            print("Opción inválida. Intente de nuevo.")  # Manejo de entrada incorrecta

# Función para registrar un nuevo estudiante
# Pide nombre y programa, los une con coma, y los agrega al final del archivo (modo 'a' para append).
def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")  # Solicita nombre
    programa = input("Ingrese el programa del estudiante: ")  # Solicita programa
    linea = f"{nombre}, {programa}\n"  # Formato: "nombre, programa" con salto de línea
    with open("estudiantes.txt", "a") as archivo:  # Abre en modo append (agrega si existe, crea si no)
        archivo.write(linea)  # Escribe la línea
    print("Estudiante registrado exitosamente.")  # Confirmación

# Función para mostrar la lista completa de estudiantes
# Lee el archivo en modo 'r', imprime cada línea (si existe el archivo).
def mostrar_lista():
    try:
        with open("estudiantes.txt", "r") as archivo:  # Abre en modo lectura
            lineas = archivo.readlines()  # Lee todas las líneas como lista
            if not lineas:  # Si la lista está vacía
                print("No hay estudiantes registrados.")
            else:
                print("\nLista de estudiantes:")
                for i, linea in enumerate(lineas, start=1):  # Enumera líneas empezando en 1
                    print(f"{i}. {linea.strip()}")  # Imprime numerado, quitando \n con strip()
    except FileNotFoundError:  # Manejo si el archivo no existe aún
        print("No hay estudiantes registrados (archivo no encontrado).")

# Función para buscar un estudiante por nombre
# Lee el archivo, busca coincidencia en el nombre (antes de la coma), imprime si encuentra.
def buscar_estudiante():
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")  # Solicita nombre
    encontrado = False  # Bandera para rastrear si se encuentra
    try:
        with open("estudiantes.txt", "r") as archivo:  # Abre en modo lectura
            for linea in archivo:  # Itera línea por línea (más eficiente que readlines para archivos grandes)
                nombre, programa = linea.strip().split(", ")  # Divide la línea en nombre y programa
                if nombre.lower() == nombre_buscar.lower():  # Compara ignorando mayúsculas
                    print(f"Estudiante encontrado: {nombre}, {programa}")
                    encontrado = True
                    break  # Sale del bucle una vez encontrado
        if not encontrado:
            print("Estudiante no encontrado.")
    except FileNotFoundError:
        print("No hay estudiantes registrados (archivo no encontrado).")

# Función para eliminar un estudiante por nombre
# Lee todas las líneas, crea una nueva lista sin la línea coincidente, y sobrescribe el archivo.
def eliminar_estudiante():
    nombre_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")  # Solicita nombre
    eliminado = False  # Bandera para rastrear eliminación
    try:
        with open("estudiantes.txt", "r") as archivo:  # Lee el archivo original
            lineas = archivo.readlines()  # Obtiene todas las líneas
        with open("estudiantes.txt", "w") as archivo:  # Sobrescribe el archivo
            for linea in lineas:  # Itera sobre las líneas leídas
                nombre, _ = linea.strip().split(", ")  # Extrae nombre (ignora programa)
                if nombre.lower() != nombre_eliminar.lower():  # Si no coincide, escribe de nuevo
                    archivo.write(linea)
                else:
                    eliminado = True  # Marca como eliminado
        if eliminado:
            print("Estudiante eliminado exitosamente.")
        else:
            print("Estudiante no encontrado.")
    except FileNotFoundError:
        print("No hay estudiantes registrados (archivo no encontrado).")

# Ejecución del programa: Llama al menú principal al iniciar
if __name__ == "__main__":
    menu_principal()  # Inicia el bucle del menú

# =====================================
# FIN DEL CÓDIGO
# =====================================
# Al ejecutar este script:
# - Se muestra el menú en consola.
# - El usuario interactúa ingresando números y datos.
# - Los cambios se guardan persistentemente en "estudiantes.txt".
# - Ejemplo de contenido en archivo: "Juan Perez, Ingeniería\nMaria Lopez, Medicina\n"
# Este código es modular (funciones separadas), robusto (manejo de errores) y simple.