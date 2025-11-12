import re

#empezar  validaciones
#valida letras y espacios - r es para que tome la cadena literal, espacios es el \s, + para que puedan haber muchas letras, 
    # y $ para marcar el final del texto, ^ para empezar la cadena- r.match es para validar el texto, r valida si y match verifica que si este con las reglas de r, {3, 60} longitud min max
def validar_texto(mensaje):
    while True:
        atributo = input(mensaje).strip()
        if re.match(r'^[A-Za-záéíóúÁÉÍÓÚñÑ0-9\s]{3,60}$' , atributo):
            return atributo
        print("Solo se permiten letras, numeros y espacios, porfavor asegurate de que los datos esten completos (minimo 3 caracteres)")

def validar_texto_sin_numeros(mensaje):
    while True:
        atributo = input(mensaje).strip()
        if re.match(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s]{3,60}$', atributo):
            return atributo
        print("Solo se permiten letras y espacios, porfavor asegurate de que los datos esten completos (minimo 3 caracteres)")

def validar_entero(mensaje):
    while True:
        atributo = input(mensaje).strip()
        if atributo.isdigit():
            return int(atributo)
        print("Escribe solo números enteros, sin letras ni símbolos.") 

def validar_flotante(mensaje):
    while True:
        atributo = input(mensaje).strip()
        try:
            return float(atributo)
        except ValueError:
            print("Escribe un número válido (usa punto, no coma).")


def validar_modalidad(mensaje):
    while True:
        atributo = input(mensaje).strip().lower()
        if atributo in ["virtual", "presencial"]:
            return atributo
        print("La modalidad debe ser 'virtual' o 'presencial'")




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
            print("3. Window 11")

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

    
    def registar_equipo(self):
        print("\n--- Registrar equipo ---")
        print("Que tipo de eqipo requiere el estudiante: \n1. Tableta grafica \n2. Computador portatil")
        opcion= input("Elige una opcion: ")

        serial= validar_texto("Serial: ")
        marca= validar_texto_sin_numeros("Marca (sin numeros): ")
        tamano= validar_flotante("Tamano: ")
        precio= validar_flotante("precio: ")
         
        for equipo in self.inventario_equipos:
            if equipo.serial == serial:
                print("\n Equipo ya esta registrado")
                return equipo
        

        if opcion =="1":
            peso=validar_flotante("Peso: ")
            #aqui ya lo relaciono con la clase y le paso las variables a verificar
            equipo= TabletaGrafica(serial, marca, tamano, precio,peso)
            equipo.elegir_almacenamiento()
        elif opcion== "2":
            equipo= ComputadorPortatil(serial, marca, tamano, precio)
            equipo.elegir_sistema_operativo()
            equipo.elegir_procesador()
        else:
            print("Opcion invalida")
            return
        
        self.inventario_equipos.append(equipo)
        print("El equipo se registro con exito :) ")

    #buscar equipo por serial
    def buscar_equipo(self,serial):
        for equipo in self.inventario_equipos:
            if equipo.serial == serial:
                return equipo
        print("Equipo no encontrado en inventario")
        return None
    
    def registrar_estudiante(self):
        print("\n--- Registrar estudiante ---")
        print("A que facultad pertenece el estudiante:  \n1. Ingenieria \n2. Diseño")
        tipo= input("\n Elige una opcion: ")

        cedula= validar_entero("Cedula: ")
        nombre= validar_texto_sin_numeros("Nombre: ")
        apellido= validar_texto_sin_numeros("Apellido: ")
        telefono= validar_texto("Telefono: ")

        if tipo =="1":
            numero_semestre= validar_entero("Numero de semestre: ")
            promedio_acumulado= validar_flotante("Promedio acumulado: ")
            serial_equipo=validar_texto("Serial: ")
            #aqui ya lo relaciono con la clase y le paso las variables a verificar
            estudiante= EstudianteIngenieria(cedula, nombre, apellido,telefono, numero_semestre, promedio_acumulado,serial_equipo)
            self.estudiantes_ingenieria.append(estudiante)
            print("El estudiante se registro con exito :) ")

        elif tipo== "2":
            modalidad= validar_modalidad("Modalidad (virtual o presencial): ")
            cant_asignaturas= validar_entero("Cantidad de asignaturas: ")
            serial_equipoD=validar_entero("Serial (solo numeros): ")
            estudiante= EstudianteDiseno(cedula, nombre, apellido,telefono, modalidad, cant_asignaturas, serial_equipoD)
            self.estudiantes_diseno.append(estudiante)
            print("El estudiante se registro con exito :) ")
        else:
            print("Opcion invalida, no se registro ningun estudiante")
            return



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
        print("\n Equipo no registrado en prestamos")
        return None


    def agregar_prestamo(self):
        print("\n--- Registrar prestamo ---")

        cedula=validar_entero("Cedula del estudiante: ")
        estudiante=self.buscar_estudiante(cedula)
        if estudiante is None:
            print("Estudiante no encontrado, porfavor registralo primero")
            return
        
        serial=input("Serial del equipo: ")
        equipo=self.buscar_equipo(serial)
        if equipo is None:
            print("\n Este equipo no esta en el inventario")
            return 
        
        if self.equipos_prestados(serial):
            print("\n Este equipo ya esta prestado")
            return
        
        prest = {"estudiante": estudiante, "equipo": equipo}
        
        self.prestamos.append(prest)
        print("\n Prestamo registrado")


    def devolver_equipo(self):
        print("\n--- Devolución de equipo ---")
        serial = input("Serial del equipo: ")

        for equipo in self.prestamos:
            if equipo.equipo.serial == serial and not equipo.devuelto:
                equipo.devuelto = True
                self.equipos_devueltos.append(equipo.equipo)
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
            print("\nNo se encontró un préstamo activo con esos datos.")
            return
        
        #mostrar informacion
        print("\n--- Préstamo encontrado ---")
        print(f"Estudiante: {prestamo_encontrado.estudiante.nombre} {prestamo_encontrado.estudiante.apellido}")
        print(f"Cedula: {prestamo_encontrado.estudiante.cedula}")
        print(f"Equipo : {prestamo_encontrado.equipo.serial} - {prestamo_encontrado.equipo.marca}")
        
        #menu de modificacion
        print("\n--- Opciones de modificación ---")
        print("1. Marcar como devuelto")
        print("2. Cambiar equipo prestado")
        print("3. Cancelar modificación")
        opcion_mod = input("Elige una opción: ")

        if opcion_mod == "1":
            prestamo_encontrado.devuelto = True
            self.equipos_devueltos.append(prestamo_encontrado.equipo)
            print("\nEl préstamo ha sido marcado como devuelto.")
        elif opcion_mod == "2":
            nuevo_serial = input("\nIngrese el serial del nuevo equipo: ")
            nuevo_equipo = self.buscar_equipo(nuevo_serial)

            if nuevo_equipo is None:
                print("\nNo existe un equipo con ese serial")
                return
            if self.equipos_prestados(nuevo_serial):
                print("\n Ese equipo ya está prestado a otro estudiante")
                return None

            prestamo_encontrado.equipo = nuevo_equipo
            print(f"\n El estudiante {prestamo_encontrado.estudiante.nombre} {prestamo_encontrado.estudiante.apellido} cambio al nuevo equipo: {nuevo_equipo.serial} - {nuevo_equipo.marca}")

        elif opcion_mod == "3":
            print("Modificación cancelada")
        else:
            print("Opción inválida.")
        
