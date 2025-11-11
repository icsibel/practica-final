from ejecutable import SistemasPrestamos, ComputadorPortatil, validar_texto
sistemasPrestamos = SistemasPrestamos()
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Equipos")
    print("2. Estudiantes")
    print("3. imprimir inventario total")
    print("4. Ver equipos devueltos")
    print("5. salir del programa")
    op=input("\n seleccione una opcion: ")

    match op:
        case "1":
            print("1. Registrar equipo")
            print("2. Buscar equipo")
            opcion=input("\nseleccione una opcion: ")
            match opcion:
                case "1":
                    sistemasPrestamos.registar_equipo()
                case "2":
                    serial= validar_texto("Ingrese el serial que deseas buscar: ")
                    equipo = sistemasPrestamos.buscar_equipo(serial)
                    if isinstance(equipo, ComputadorPortatil):
                        print(f"Computador portatil: {equipo.serial} | {equipo.marca} | {equipo.tamano} | {equipo.precio} | {equipo.sistema_operativo} | {equipo.procesador}")
                    else:
                        print(f"Tableta grafica: {equipo.serial} | {equipo.marca} | {equipo.tamano} | {equipo.precio} | {equipo.almacenamiento} | {equipo.peso}")
                    

        case "2":
            print("1. Registrar estudiante")
            print("2. Registrar préstamo")
            print("3. Devolver equipo")
            print("4. Modificar préstamo")
            print("5. buscar estudiante")
            print("6. volver al menu principal")
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
                    sistemasPrestamos.buscar_estudiante()
                case "6":
                    print("Volviendo al menú principal...")
                    break
                case _:
                    print("Opción inválida")
        
        case "3":
            sistemasPrestamos.imprimir_inventario()
        
        case "4":
            sistemasPrestamos.mostrar_devueltos()
        
        case "5":
            print("saliendo del sistema... byeee")
            break
