Menu de gestion de estudiantes

Es un programa simple y educativo en **Python puro** (sin dependencias externas) que permite gestionar una lista de estudiantes mediante un menú interactivo en consola.

Gestión de Estudiantes con Menú Interactivo


Programa educativo en Python puro para gestionar estudiantes.
Guarda los datos en un archivo de texto plano: estudiantes.txt
Formato por línea: "Nombre Completo, Programa Académico"

Funcionalidades:
- Registrar estudiante
- Mostrar todos los estudiantes
- Buscar por nombre
- Eliminar estudiante
- Persistencia de datos entre ejecuciones

Ideal para aprender: manejo de archivos, funciones, bucles y control de errores.

       
        def menu_principal():
    while True:
        print("\n" + "="*40)
        print("   MENÚ DE GESTIÓN DE ESTUDIANTES")
        print("="*40)
        print("1. Registrar estudiante")
        print("2. Mostrar lista de estudiantes")
        print("3. Buscar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        print("-"*40)
        
        opcion = input("Elija una opción (1-5): ").strip()
        
        if opcion == '1':
            registrar_estudiante()
        elif opcion == '2':
            mostrar_lista()
        elif opcion == '3':
            buscar_estudiante()
        elif opcion == '4':
            eliminar_estudiante()
        elif opcion == '5':
            print("¡Hasta luego! Programa finalizado.")
            break
        else:
            print("Opción inválida. Por favor, elija entre 1 y 5.")


    def registrar_estudiante():
        nombre = input("\nIngrese el nombre completo del estudiante: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        programa = input("Ingrese el programa académico: ").strip()
        if not programa:
            print("El programa no puede estar vacío.")
            return
    
    with open("estudiantes.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre}, {programa}\n")
    print(f"Estudiante '{nombre}' registrado exitosamente.")
    
    def mostrar_lista():
    try:
        with open("estudiantes.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    
        if not lineas:
            print("\nNo hay estudiantes registrados aún.")
            return
            
        print("\n" + "="*50)
        print("        LISTA DE ESTUDIANTES REGISTRADOS")
        print("="*50)
        for i, linea in enumerate(lineas, start=1):
            nombre, programa = linea.strip().split(", ", 1)
            print(f"{i:2d}. {nombre:<25} → {programa}")
        print("="*50)
        
    except FileNotFoundError:
        print("\nNo hay estudiantes registrados (archivo no encontrado).")

    
    def buscar_estudiante():
    if not verificar_archivo():
        return
        
    nombre_buscar = input("\nIngrese el nombre del estudiante a buscar: ").strip().lower()
    
    with open("estudiantes.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip():
                nombre, programa = linea.strip().split(", ", 1)
                if nombre.lower() == nombre_buscar:
                    print(f"\nEstudiante encontrado:")
                    print(f"   Nombre:   {nombre}")
                    print(f"   Programa: {programa}")
                    return
    print("Estudiante no encontrado.")

    def eliminar_estudiante():
    if not verificar_archivo():
        return
        
    nombre_eliminar = input("\nIngrese el nombre exacto del estudiante a eliminar: ").strip().lower()
        
    with open("estudiantes.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    
    eliminados = 0
    with open("estudiantes.txt", "w", encoding="utf-8") as archivo:
        for linea in lineas:
            if linea.strip():
                nombre_guardado = linea.strip().split(", ", 1)[0].lower()
                if nombre_guardado != nombre_eliminar:
                    archivo.write(linea)
                else:
                    eliminados += 1
    
    if eliminados > 0:
        print(f"Estudiante(s) eliminado(s) correctamente.")
    else:
        print("No se encontró ningún estudiante con ese nombre.")

    def verificar_archivo():
        try:
            with open("estudiantes.txt", "r"):
                return True
        except FileNotFoundError:
            print("No hay estudiantes registrados aún.")
            return False

    if __name__ == "__main__":
        print("Bienvenido al Sistema de Gestión de Estudiantes")
        menu_principal()
