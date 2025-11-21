from ejecutable import SistemasPrestamos, ComputadorPortatil, TabletaGrafica, validar_texto, validar_cedula, EstudianteIngenieria, EstudianteDiseno
sistemasPrestamos = SistemasPrestamos()
sistemasPrestamos.cargar_todo() 
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Equipos")
    print("2. Estudiantes")
    print("3. imprimir inventario total de equipos")
    print("4. imprimir listado de estudiantes")
    print("5. Ver equipos devueltos")
    print("6. salir del programa")
    op=input("\n seleccione una opcion: ")

    match op:
        case "1":
            while True:
                print("1. Registrar equipo")
                print("2. Buscar equipo")
                print("3. Volver al menú principal")
                opcion=input("\nseleccione una opcion: ")
                match opcion:
                    case "1":
                        sistemasPrestamos.registar_equipo()
                    case "2":
                        serial= validar_texto("Ingrese el serial que deseas buscar: ")
                        equipo = sistemasPrestamos.buscar_equipo(serial)

                        if isinstance(equipo, ComputadorPortatil):
                            print(f"Computador portatil: {equipo.serial} | {equipo.marca} | {equipo.tamano} | {equipo.precio} | {equipo.sistema_operativo} | {equipo.procesador}")
                        if isinstance(equipo, TabletaGrafica):
                            print(f"Tableta grafica: {equipo.serial} | {equipo.marca} | {equipo.tamano} | {equipo.precio} | {equipo.almacenamiento} | {equipo.peso}")
                    case "3":
                        print("\nVolviendo al menú principal...")
                        break 
                    case _:
                        print("opcion invalida")

        case "2":
            while True:
                print("1. Registrar estudiante")
                print("2. Registrar préstamo")
                print("3. Devolver equipo")
                print("4. Modificar préstamo")
                print("5. buscar estudiante")
                print("6. mostrar prestamos")
                print("7. volver al menu principal")
                opcion=input("\nseleccione una opcion: ")

                match opcion:
                    case "1":
                        sistemasPrestamos.registrar_estudiante()
                    case "2":
                        sistemasPrestamos.agregar_prestamo()
                    case "3":
                        sistemasPrestamos.devolver_equipo()
                    case "4":
                        sistemasPrestamos.modificar_prestamo()
                    case "5":
                        cedula= validar_cedula("Ingrese la cedula del estudiante que deseas buscar: ")
                        cedula = sistemasPrestamos.buscar_estudiante(cedula)

                        if isinstance(cedula, EstudianteIngenieria):
                            print(f"Estudiant de Ingenieria: {cedula.nombre} | {cedula.apellido} | {cedula.telefono} | {cedula.numero_semestre} | {cedula.promedio_acumulado} | {cedula.serial_equipo}")
                        if isinstance(cedula, EstudianteDiseno):
                            print(f"Estudiante de diseño: {cedula.nombre} | {cedula.apellido} | {cedula.telefono} | {cedula.modalidad} | {cedula.cant_asignaturas} | {cedula.serial_equipoD}")
                        
                    case "6":
                        sistemasPrestamos.mostrar_prestamos()
                    case "7":
                        print("Volviendo al menú principal...")
                        break
                
                    case _:
                        print("Opción inválida")
        
        case "3":
            sistemasPrestamos.imprimir_inventario()

        case "4":
            sistemasPrestamos.imprimir_estudiantes()
        
        case "5":
            sistemasPrestamos.mostrar_devueltos()
        
        case "6":
            print("saliendo del sistema... byeee")
            break

        case _:
            print("\nOpción inválida, intenta de nuevo.")
