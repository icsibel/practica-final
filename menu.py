from ejecutable import SistemasPrestamos
sistemasPrestamos = SistemasPrestamos()
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Agregar equipo al inventario")
    print("2. Estudiante de ingenieria")
    print("3. Estudiante de diseño")
    print("4. imprimir inventario total")
    print("5. Ver equipos devueltos")
    print("6. salir del programa")
    op=input("seleccione una opcion: ")

    match op:
        case "1":
            sistemasPrestamos.registar_equipo()

        case "2":
            print("1. Registrar estudiante")
            print("2. Registrar préstamo")
            print("3. Devolver equipo")
            print("4. Modificar préstamo")
            print("5. Buscar equipo")
            print("6. buscar estudiante")
            print("7. volver al menu principal")
            opcion=input("seleccione una opcion: ")

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
                    sistemasPrestamos.buscar_equipo()
                case "6":
                    sistemasPrestamos.buscar_estudiante()
                case "7":
                    print("Volviendo al menú principal...")
                    break
                case _:
                    print("Opción inválida")

        case "3":
            print("1. Registrar estudiante")
            print("2. Registrar préstamo")
            print("3. Devolver equipo")
            print("4. Modificar préstamo")
            print("5. Buscar equipo")
            print("6. buscar estudiante")
            print("7. volver al menu principal")
            opcion=input("seleccione una opcion: ")

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
                    sistemasPrestamos.buscar_equipo()
                case "6":
                    sistemasPrestamos.buscar_estudiante()
                case "7":
                    print("Volviendo al menú principal...")
                    break
                case _:
                    print("Opción inválida")
        
        case "4":
            sistemasPrestamos.imprimir_inventario()
        
        case "5":
            sistemasPrestamos.mostrar_devueltos()
        
        case "6":
            print("saliendo del sistema... byeee")
            break
