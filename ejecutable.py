import re
import pandas as panditas
import os

#empezar  validaciones
#valida letras y espacios - r es para que tome la cadena literal, espacios es el \s, + para que puedan haber muchas letras, 
# y $ para marcar el final del texto, ^ para empezar la cadena- r.match es para validar el texto, r valida si y match verifica que si este con las reglas de r, {3, 60} longitud min max
def validar_texto(mensaje):
    atributo = input(mensaje).strip()
    if re.match(r'^[A-Za-záéíóúÁÉÍÓÚñÑ0-9\s]{2,60}$' , atributo):
        return atributo
    print("Solo se permiten letras, numeros y espacios, porfavor asegurate de que los datos esten completos (minimo 2 caracteres)")
    return validar_texto(mensaje)

def validar_texto_sin_numeros(mensaje):
    atributo = input(mensaje).strip()
    if re.match(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s]{2,60}$', atributo):
        return atributo
    print("Solo se permiten letras y espacios, porfavor asegurate de que los datos esten completos (minimo 2 caracteres)")
    return validar_texto_sin_numeros(mensaje)

def validar_entero(mensaje):
    atributo = input(mensaje).strip()
    if atributo.isdigit():
        return int(atributo)
    print("Escribe solo números enteros, sin letras ni símbolos")
    return validar_entero(mensaje) 

def validar_flotante(mensaje):
    atributo = input(mensaje).strip()
    try:
        return float(atributo)
    except ValueError:
        print("Escribe un número válido (usa punto, no coma)")
        return validar_flotante(mensaje)


def validar_modalidad(mensaje):
    atributo = input(mensaje).strip().lower()
    if atributo in ["virtual", "presencial"]:
        return atributo
    print("La modalidad debe ser 'virtual' o 'presencial'")
    return validar_modalidad(mensaje)

def validar_cedula(mensaje):
    atributo = input(mensaje).strip()
    # Solo números pero se devuelve como texto
    if atributo.isdigit():
        return atributo
    print("La cédula solo debe contener numeros, sin letras ni simbolos.")
    return validar_cedula(mensaje)


#HU2
class Estudiante:
    def __init__(self,cedula,nombre,apellido,telefono):
       self.cedula= cedula
       self.nombre= nombre
       self.apellido= apellido
       self.telefono= telefono

class EstudianteIngenieria(Estudiante):
    def __init__(self,cedula,nombre,apellido,telefono,numero_semestre,promedio_acumulado,serial_equipo):
        super().__init__(cedula,nombre,apellido,telefono)
        self.numero_semestre= numero_semestre
        self.promedio_acumulado= promedio_acumulado
        self.serial_equipo=serial_equipo

class EstudianteDiseno(Estudiante):
    def __init__(self,cedula,nombre,apellido,telefono,modalidad,cant_asignaturas,serial_equipoD):
        super().__init__(cedula,nombre,apellido,telefono)
        self.modalidad= modalidad
        self.cant_asignaturas= cant_asignaturas
        self.serial_equipoD=serial_equipoD

#HU3 
class Electronicos:
    def __init__(self,serial,marca,tamano,precio):
        self.serial= serial
        self.marca= marca
        self.tamano= tamano
        self.precio=precio

class TabletaGrafica(Electronicos):
    def __init__(self, serial, marca, tamano, precio,peso):
        super().__init__(serial, marca, tamano, precio)
        self.almacenamiento= None
        self.peso= peso
    
    def elegir_almacenamiento(self):
        while True:
            print("\n--- Seleccionar almacenamiento ---")
            print("1. 256 GB")
            print("2. 512 GB")
            print("3. 1 TB")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.almacenamiento= "256 GB"
                break
            elif opcion == "2":
                self.almacenamiento = "512 GB"
                break
            elif opcion == "3":
                self.almacenamiento = "1 TB"
                break
            else:
                print("Opción inválida, selecciona solo 1, 2 o 3.")

        print(f"\nAlmacenamiento seleccionado: {self.almacenamiento}")

class ComputadorPortatil(Electronicos):
    def __init__(self, serial, marca, tamano, precio):
        super().__init__(serial, marca, tamano, precio)
        self.sistema_operativo=None
        self.procesador=None

    def elegir_sistema_operativo(self):
        while True:
            print("\n--- Seleccionar sitema operativo  ---")
            print("1. Windows 7")
            print("2. Windows 10")
            print("3. Windows 11")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.sistema_operativo= "Windows 7"
                break
            elif opcion == "2":
                self.sistema_operativo = "Windows 10"
                break
            elif opcion == "3":
                self.sistema_operativo = "Window 11"
                break
            else:
                print("Opción inválida, selecciona solo 1, 2 o 3.")

    def elegir_procesador(self):
        while True:
            print("\n--- Seleccionar procesador  ---")
            print("1. AMD Ryzen")
            print("2. Intel Core i5")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.procesador= "AMD Ryzen"
                break
            elif opcion == "2":
                self.procesador = "Intel Core i5"
                break
            else:
                print("Opción inválida, selecciona solo 1 o 2.")

# HU4
#clase prestamos
class Prestamo:
    def __init__(self,estudiante,equipo):
        self.estudiante=estudiante
        self.equipo=equipo
        self.devuelto=False

#clase principal
class SistemasPrestamos:
    def __init__(self):
        self.estudiantes_ingenieria= []
        self.estudiantes_diseno= []
        self.inventario_equipos= []
        self.prestamos= []
        self.equipos_devueltos= []

    #HU6 cargar y guardar pandita
    # os sirve para manejar las funciones del sistema operativo, sirve para crear nuevas carpetas dentro del proyecto
    # crear nuevos archivos, saber si una ruta existe, esto mira que hay dentro del proyecto
    # makedir es para crear carpetas
    # path es ruta
    # funcion para crear la carpeta datos si no existe
    def asegurar_carpeta(self):
        if not os.path.exists("datos"): 
            os.makedirs("datos")

    def guardar_todo(self):
        self.asegurar_carpeta()
        #panditas solo recibe listas de diccionarios
        datos_inge = []
        for est in self.estudiantes_ingenieria:
            datos_inge.append({ "cedula": est.cedula, 
                               "nombre": est.nombre, 
                               "apellido": est.apellido, 
                               "telefono": est.telefono, 
                               "numero_semestre": est.numero_semestre, 
                               "promedio_acumulado": est.promedio_acumulado, 
                               "serial_equipo": est.serial_equipo })

        df_inge = panditas.DataFrame(datos_inge)
        # el archivo se crea dentro de la carpeta datos
        # .to_csv es para crear un documento de texto separado por comas, index me quita los indices
        # encoding es para recibir caracteres especiales, me lo saque de internet :P
        df_inge.to_csv("datos/estudiantes_ingenieria.csv", index=False, encoding="utf-8")

        datos_dis = []
        for est in self.estudiantes_diseno:
            datos_dis.append({ "cedula": est.cedula, 
                              "nombre": est.nombre, 
                              "apellido": est.apellido, 
                              "telefono": est.telefono, 
                              "modalidad": est.modalidad, 
                              "cant_asignaturas": est.cant_asignaturas, 
                              "serial_equipoD": est.serial_equipoD })

        df_dis = panditas.DataFrame(datos_dis)
        df_dis.to_csv("datos/estudiantes_diseno.csv", index=False, encoding="utf-8")

        datos_eq = []
        for eq in self.inventario_equipos:
            if isinstance(eq, TabletaGrafica):
                datos_eq.append({"serial": eq.serial,
                                 "tipo": "tableta",
                                 "marca": eq.marca,
                                 "tamano": eq.tamano,
                                 "precio": eq.precio,
                                 "almacenamiento": eq.almacenamiento,
                                 "peso": eq.peso})

            if isinstance(eq, ComputadorPortatil):
                datos_eq.append({ "serial": eq.serial,
                                 "tipo": "portatil",
                                 "marca": eq.marca,
                                 "tamano": eq.tamano,
                                 "precio": eq.precio,
                                 "sistema_operativo": eq.sistema_operativo,
                                 "procesador": eq.procesador})

        df_eq = panditas.DataFrame(datos_eq)
        df_eq.to_csv("datos/inventario_equipos.csv", index=False, encoding="utf-8")

        print("\n Toda la información fue guardada correctamente")

    # iterrows es para recorrer cada fila del archivo
    # notna es para saber si un valor existe en el archivo
    def cargar_todo(self):
        self.asegurar_carpeta()

        ruta_inge = "datos/estudiantes_ingenieria.csv"

        if not os.path.exists(ruta_inge):
            df_vacio = panditas.DataFrame(columns=[
                "cedula", "nombre", "apellido", "telefono",
                "numero_semestre", "promedio_acumulado", "serial_equipo"])
            df_vacio.to_csv(ruta_inge, index=False, encoding="utf-8")

        df_inge = panditas.read_csv(ruta_inge, encoding="utf-8")
        self.estudiantes_ingenieria = []

        for _, fila in df_inge.iterrows():
            est = EstudianteIngenieria(
                cedula=fila["cedula"],
                nombre=fila["nombre"],
                apellido=fila["apellido"],
                telefono=fila["telefono"],
                numero_semestre=int(fila["numero_semestre"]),
                promedio_acumulado=float(fila["promedio_acumulado"]),
                serial_equipo=fila["serial_equipo"])
            
            self.estudiantes_ingenieria.append(est)

        ruta_dis = "datos/estudiantes_diseno.csv"

        if not os.path.exists(ruta_dis):
            df_vacio = panditas.DataFrame(columns=[
                "cedula", "nombre", "apellido", "telefono",
                "modalidad", "cant_asignaturas", "serial_equipoD"])
            
            df_vacio.to_csv(ruta_dis, index=False, encoding="utf-8")

        df_dis = panditas.read_csv(ruta_dis, encoding="utf-8")
        self.estudiantes_diseno = []

        for _, fila in df_dis.iterrows():
            est = EstudianteDiseno(
                cedula=fila["cedula"],
                nombre=fila["nombre"],
                apellido=fila["apellido"],
                telefono=fila["telefono"],
                modalidad=fila["modalidad"],
                cant_asignaturas=int(fila["cant_asignaturas"]),
                serial_equipoD=fila["serial_equipoD"])
            
            self.estudiantes_diseno.append(est)

        ruta_eq = "datos/inventario_equipos.csv"

        if not os.path.exists(ruta_eq):
            df_vacio = panditas.DataFrame(columns=[
                "serial", "tipo", "marca", "tamano", "precio",
                "almacenamiento", "peso",
                "sistema_operativo", "procesador"])
            
            df_vacio.to_csv(ruta_eq, index=False, encoding="utf-8")

        df_eq = panditas.read_csv(ruta_eq, encoding="utf-8")
        self.inventario_equipos = []

        for _, fila in df_eq.iterrows():
            tipo = fila["tipo"]
            serial = fila["serial"]
            marca = fila["marca"]
            tamano = float(fila["tamano"])
            precio = float(fila["precio"])

            if tipo == "tableta":
                if panditas.notna(fila["peso"]):
                    peso = float(fila["peso"])
                else: 
                    peso= 0.0

                equipo = TabletaGrafica(serial, marca, tamano, precio, peso)

                if panditas.notna(fila["almacenamiento"]):
                    equipo.almacenamiento = fila["almacenamiento"]

            elif tipo == "portatil":
                equipo = ComputadorPortatil(serial, marca, tamano, precio)

                if panditas.notna(fila["sistema_operativo"]):
                    equipo.sistema_operativo = fila["sistema_operativo"]

                if panditas.notna(fila["procesador"]):
                    equipo.procesador = fila["procesador"]

            self.inventario_equipos.append(equipo)


        print("\n Datos cargados exitosamente (archivos creados si no existian)\n")


    
    def registar_equipo(self):
        while True:
            print("\n--- Registrar equipo ---")
            print("Qué tipo de equipo requiere el estudiante:")
            print("1. Tableta gráfica")
            print("2. Computador portátil")
            opcion = input("Elige una opción: ")

            if opcion in ("1", "2"):
                break
            else:
                print("\nOpción inválida, selecciona solo 1 o 2.\n")

        serial= validar_texto("Serial: ")
        marca= validar_texto_sin_numeros("Marca (sin numeros): ")
        tamano= validar_flotante("Tamano: ")
        precio= validar_flotante("precio: ")

        for equipo in self.inventario_equipos:
            if equipo.serial == serial:
                print("\n Este equipo ya esta registrado")
                return equipo
            
        if opcion == "1":
            peso=validar_flotante("Peso: ")
            #aqui ya lo relaciono con la clase y le paso las variables a verificar
            equipo= TabletaGrafica(serial, marca, tamano, precio,peso)
            equipo.elegir_almacenamiento()
        elif opcion == "2":
            equipo= ComputadorPortatil(serial, marca, tamano, precio)
            equipo.elegir_sistema_operativo()
            equipo.elegir_procesador()
        
        self.inventario_equipos.append(equipo)
        print("El equipo se registro con exito :) ")
        self.guardar_todo()

    #buscar equipo por serial
    def buscar_equipo(self,serial):
        for equipo in self.inventario_equipos:
            if equipo.serial == serial:
                return equipo
        print("Equipo no encontrado en inventario")
        return None
    
    def registrar_estudiante(self):
        while True:
            print("\n--- Registrar estudiante ---")
            print("¿A qué facultad pertenece el estudiante?")
            print("1. Ingeniería")
            print("2. Diseño")
            tipo = input("\nElige una opción: ")

            if tipo in ("1", "2"):
                break
            else:
                print("\nOpción inválida, selecciona solo 1 o 2.\n")

        cedula= validar_cedula("Cedula: ")
        nombre= validar_texto_sin_numeros("Nombre: ")
        apellido= validar_texto_sin_numeros("Apellido: ")
        telefono= validar_texto("Telefono: ")

        for estudiante in self.estudiantes_diseno + self.estudiantes_ingenieria:
            if estudiante.cedula == cedula:
                print("\n Este estudiante ya esta registrado")
                return estudiante

        if tipo =="1":
            numero_semestre= validar_entero("Numero de semestre: ")
            promedio_acumulado= validar_flotante("Promedio acumulado: ")
            serial_equipo=validar_texto("Serial: ")
            #aqui ya lo relaciono con la clase y le paso las variables a verificar
            estudiante= EstudianteIngenieria(cedula, nombre, apellido,telefono, numero_semestre, promedio_acumulado,serial_equipo)
            self.estudiantes_ingenieria.append(estudiante)
            print("El estudiante se registro con exito :) ")
            self.guardar_todo()

        elif tipo== "2":
            modalidad= validar_modalidad("Modalidad (virtual o presencial): ")
            cant_asignaturas= validar_entero("Cantidad de asignaturas: ")
            serial_equipoD=validar_entero("Serial (solo numeros): ")
            estudiante= EstudianteDiseno(cedula, nombre, apellido,telefono, modalidad, cant_asignaturas, serial_equipoD)
            self.estudiantes_diseno.append(estudiante)
            print("El estudiante se registro con exito :) ")
            self.guardar_todo()



        #buscar estudiante por cedula
    
    def buscar_estudiante(self,cedula):
        
        for estudiante in self.estudiantes_diseno + self.estudiantes_ingenieria:
            if estudiante.cedula == cedula:
                return estudiante
        print("\n Estudiante no encontrado")
        return None
    

        # buscar en prestamos
    
    def equipos_prestados(self,serial):
        for equipo in self.prestamos:
            if equipo.equipo.serial == serial and not equipo.devuelto:
                return equipo 
        return None


    def agregar_prestamo(self):
        print("\n--- Registrar prestamo ---")

        cedula=validar_cedula("Cedula del estudiante: ")
        estudiante=self.buscar_estudiante(cedula)
        if estudiante is None:
            print("Estudiante no encontrado, porfavor registralo primero")
            return
        
        if self.estudiante_con_prestamos(cedula):
            print("\nEste estudiante ya tiene un préstamo activo")
            return

        serial=input("Serial del equipo: ")
        equipo=self.buscar_equipo(serial)
        if equipo is None:
            print("\n Este equipo no esta en el inventario")
            return 
        
        if self.equipos_prestados(serial):
            print("\n Este equipo ya esta prestado")
            return
        
        prest = Prestamo(estudiante, equipo)
        self.prestamos.append(prest)
        print("\n Prestamo registrado")
        self.guardar_todo()


    def devolver_equipo(self):
        print("\n--- Devolución de equipo ---")
        serial = input("Serial del equipo: ")

        for i, prestamo in enumerate(self.prestamos):
            if prestamo.equipo.serial == serial and not prestamo.devuelto:
                prestamo.devuelto = True
                self.equipos_devueltos.append(prestamo.equipo)
                del self.prestamos[i]
                print("\n Devolución registrada")
                return
        print("\n No se encontró préstamo activo para ese equipo.")

    
    def imprimir_inventario(self):
        print("\n=== Inventario Total ===")
        if not self.inventario_equipos:
            print("No hay equipos registrados.")
            return
        for equipo in self.inventario_equipos:
            print(f"\nSerial: {equipo.serial} | Marca: {equipo.marca} | Precio: {equipo.precio}")

    def mostrar_devueltos(self):
        print("\n=== Inventario Devueltos Totales ===")
        if not self.equipos_devueltos:
            print("No hay equipos devueltos.")
            return
        for equipo in self.equipos_devueltos:
            print(f"\nSerial: {equipo.serial} | Marca: {equipo.marca} ")

    #hu5 tambien
    def modificar_prestamo(self):
        print("\n--- Modificar prestamo ---")
        print("1. Buscar por cédula del estudiante")
        print("2. Buscar por serial del equipo")
        opcion = input("\n Elige una opción (1 o 2): ")
        prestamo_encontrado = None

        if opcion == "1":
            cedula = input("Cédula del estudiante: ")
            for prestamo in self.prestamos:
                if prestamo.estudiante.cedula == cedula and not prestamo.devuelto:
                    prestamo_encontrado = prestamo
                    break
        elif opcion == "2":
            serial = input("Serial del equipo: ")
            for prestamo in self.prestamos:
                if prestamo.equipo.serial == serial and not prestamo.devuelto:
                    prestamo_encontrado = prestamo
                    break
        else:
            print("\nOpción inválida.")
            return
        
        if prestamo_encontrado is None:
            print("\nNo se encontró un préstamo activo con esos datos")
            return
        
        while True: 
        #menu de modificacion
            print("\n--- Opciones de modificación ---")
            print("1. Cambiar datos del estudiante")
            print("2. Cambiar equipo prestado")
            print("3. Marcar prestamo como devuelto")
            print("4. Cancelar modificación")
            opcion_mod = input("Elige una opción: ")

            if opcion_mod == "1":
                estudiante= prestamo_encontrado.estudiante
                print(f"\n Estudiante actual: {estudiante.nombre} {estudiante.apellido} | telefono: {estudiante.telefono}")

                nuevo_nombre= input("Nuevo nombre (ENTER para dejar igual): ").strip()
                if nuevo_nombre != "":
                    nuevo_nombre= validar_texto_sin_numeros("Confirme su nombre : ")
                    estudiante.nombre=nuevo_nombre

                nuevo_apellido = input("Nuevo apellido (ENTER para dejar igual): ").strip()
                if nuevo_apellido != "":
                    nuevo_apellido=validar_texto_sin_numeros("Confirme su apellido: ")
                    estudiante.apellido=nuevo_apellido

                nuevo_telefono= input("Nuevo telefono (ENTER para dejar igual): ").strip()
                if nuevo_telefono != "":
                    nuevo_telefono= validar_texto("Confirme su numero de telefono: ")
                    estudiante.telefono=nuevo_telefono
                
                print("\n Datos actualizados correctamente")
                print(f"\n El estudiante  cambio sus datos a: {nuevo_nombre} - {nuevo_apellido}- {nuevo_telefono}")
                self.guardar_todo()

            elif opcion_mod == "2":
                nuevo_serial = validar_texto("\nIngrese el serial del nuevo equipo: ")
                nuevo_equipo = self.buscar_equipo(nuevo_serial)

                if nuevo_equipo is None:
                    print("\nNo existe un equipo con ese serial")
                    return
                if self.equipos_prestados(nuevo_serial):
                    print("\n Ese equipo ya está prestado a otro estudiante")
                    return None
                else: 
                    prestamo_encontrado.equipo = nuevo_equipo
                    print(f"\n El estudiante {prestamo_encontrado.estudiante.nombre} {prestamo_encontrado.estudiante.apellido} cambio al nuevo equipo: {nuevo_equipo.serial} - {nuevo_equipo.marca}")
                    self.guardar_todo()

            elif opcion_mod == "3":
                prestamo_encontrado.devuelto = True
                self.equipos_devueltos.append(prestamo_encontrado.equipo)
                print("\nEl préstamo ha sido marcado como devuelto.")
                self.guardar_todo()
                return
            
            elif opcion_mod=="4":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion invalida.")
        
    #hu5
    def estudiante_con_prestamos(self, cedula):
        for prestamo in self.prestamos:
            if prestamo.estudiante.cedula == cedula and not prestamo.devuelto:
                return True
        return False
    
    def mostrar_prestamos(self):
        print("\n=== Inventario de Prestamos  ===")
        if not self.prestamos:
            print("No hay equipos prestados")
            return
        for equipo in self.prestamos:
            print(f"\nSerial: {equipo.serial} | Estudiante: {equipo.estudiante.nombre} {equipo.estudiante.apellido} cedula: {equipo.estudiante.cedula}")

    def  imprimir_estudiantes(self):
        print("\n=== Listado de Estudiantes ===")
        if not self.estudiantes_diseno + self.estudiantes_ingenieria:
            print("No hay estudiantes registrados.")
            return
        for estudiante in self.estudiantes_diseno + self.estudiantes_ingenieria:
            if isinstance(estudiante, EstudianteIngenieria):
                print(f"Estudiant de Ingenieria: {estudiante.nombre} | {estudiante.apellido} | {estudiante.telefono} | {estudiante.numero_semestre} | {estudiante.promedio_acumulado} | {estudiante.serial_equipo}")
            if isinstance(estudiante, EstudianteDiseno):
                print(f"Estudiante de diseño: {estudiante.nombre} | {estudiante.apellido} | {estudiante.telefono} | {estudiante.modalidad} | {estudiante.cant_asignaturas} | {estudiante.serial_equipoD}")