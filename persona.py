# Clase Persona
class Persona:
    def __init__(self, nombre, apellido, cedula, telefono, correo, consejo, equipo): # Atributos de la clase
        self.nombre = nombre # Nombre del Vocero
        self.apellido = apellido # Apellido del Vocero
        self.cedula = cedula # Cedula de Identidad
        self.telefono = telefono # Numero de Telefono del Vocero
        self.correo = correo # Correo Electronico del Vocero
        self.consejo = consejo # Consejo Comunal al que pertenece (Por codigo)
        self.equipo = equipo # Unidad o Comite al que pertenece en el Consejo Comunal
    
    # Datos de la Persona de la Persona, Funcions Get y Set

    # Nombre
    def setNombre(self, nombre): self.nombre = nombre
    
    def getNombre(self): return self.nombre

    # Apellido
    def setApellido(self, apellido): self.apellido = apellido
    
    def getApellido(self): return self.apellido

    # Cedula de Identidad
    def setCedula(self, cedula): self.cedula = cedula

    def getCedula(self): return self.cedula

    # Número de Teléfono
    def setTelefono(self, telefono): self.telefono = telefono
    
    def getTelefono(self): return self.telefono

    # Correo Electrónico
    def setCorreo(self, correo): self.correo = correo
    
    def getCorreo(self): return self.correo

    # Consejo Comunal al que pertenece
    def setConsejo(self, consejo): self.consejo = consejo
    
    def getConsejo(self): return self.consejo

    # Unidad o Comité al que pertenece dentro de la comuna
    def setEquipo(self, equipo): self.equipo = equipo
    
    def getEquipo(self): return self.equipo

    def vacio(self): return self.getCedula() == ""

    # Ingresar datos de una Persona
    # editar recibe valores del 0 al n numero, el 0 representa que se esta agregando
    # o editando una persona
    # si es cualquier otro numero, se esta editando un atributo en especifico
    def Ingresar_Datos_Persona(self, editar, nombre, apellido, cedula, telefono, correo, consejo, equipo):
        if editar == 0 or editar == 1: self.setNombre(nombre = input("Nombre: "))

        if editar == 0 or editar == 2: self.setApellido(apellido = input("Apellido: "))

        if editar == 0 or editar == 3: self.setCedula(cedula = input("Cedula de Identidad: "))

        if editar == 0 or editar == 4: self.setTelefono(telefono = input("Numero de Telefono: "))

        if editar == 0 or editar == 5: self.setCorreo(correo = input("Correo Electronico: "))

        if editar == 0 or editar == 6: self.setConsejo(consejo = input("Consejo Comunal: "))

        if editar == 0 or editar == 7: self.setEquipo(equipo = input("Unidad o Comite: "))
    
    # Agregar Persona (Opcion 1 del Menu Vocero)
    def Agregar_Persona(self):
        # Editar/Nombre/Apellido/Cedula/Telefono/Correo/ConsejoComunal/UnidadOComite
        self.Ingresar_Datos_Persona(0, "", "", "", "", "", 0, "")
    
    # Mostrar datos de una Persona (Opcion 3 y 5 del Menu Vocero)
    def Mostrar_Persona(self):
        print("Nombre y Apellido:", self.getNombre(), self.getApellido())
        print("Cedula:", self.getCedula())
        print("Telefono:", self.getTelefono())
        print("Correo:", self.getCorreo())
        print("Consejo Comunal:", self.getConsejo())
        print("Unidad o Comite:", self.getEquipo(), "\n")
    
    # Actualizar datos de una persona (Opcion 4 del Menu Vocero)
    def Editar_Persona(self):
        que_editar = 0
        opcion = int(input("Actualizar (1) un dato o (2) todos los datos\n\nOpcion: "))
        
        if opcion == 1:
            print("(1) Nombre\n(2) Apellido\n(3) Cedula\n(4) Telefono\n(5) Correo\n(6) Consejo Comunal\n(7) Equipo\n")
            que_editar = int(input("Opcion: "))
        
        if opcion == 1 or opcion == 2: self.Ingresar_Datos_Persona(que_editar, "", "", "", "", "", 0, "")

# Funciones

def Agregar_La_Persona(Vocero, Voceros): # Opcion 1 Agregar
    print("Agregar VOCERO:\n")
    Vocero = Persona("", "", "", "", "", 0, "")
    Vocero.Agregar_Persona()
    Voceros.append(Vocero)
    print("Datos del Vocero agregados")

def Eliminar_La_Persona(Vocero, Voceros): # Opcion 2 Eliminar
    i = 0
    if len(Voceros) == 0:
        print("Opcion 2...\nNo hay voceros guardados")
    else:
        print("Quitar VOCERO")
        i = 0
        editar = input("\nCedula del Vocero: ")
        while True:
            if Voceros[i].getCedula() == editar:
                Vocero = Voceros[i]
                Voceros.remove(Vocero)
                print("\nDatos del Vocero eliminados")
                break
            i = i + 1
            if i+1 > len(Voceros):
                print("\nPersona no encontrada")
                break

def Consultar_La_Persona(Voceros): # Opcion 3 Mostrar una Persona
    i = 0
    if len(Voceros) == 0:
        print("Opcion 3...\nNo hay voceros guardados")
    else:
        print("Consulta VOCERO")
        i = 0
        editar = input("\nCedula del Vocero: ")
        while True:
            if Voceros[i].getCedula() == editar:
                Voceros[i].Mostrar_Persona()
                break
            i = i + 1
            if i+1 > len(Voceros):
                print("\nPersona no encontrada")
                break

def Editar_La_Persona(Vocero, Voceros): # Opcion 4 Editar
    i = 0
    if len(Voceros) == 0:
        print("Opcion 4...\nNo hay voceros guardados")
    else:
        print("Actualizar VOCERO")
        i = 0
        editar = input("\nCedula del Vocero: ")
        while True:
            if Voceros[i].getCedula() == editar:
                Vocero = Voceros[i]
                Voceros.remove(Vocero)
                Vocero.Editar_Persona()
                Voceros.insert(i, Vocero)
                print("\nDatos del Vocero actualizados")
                break
            i = i + 1
            if i+1 > len(Voceros):
                print("\nPersona no encontrada")
                break

def Mostrar_Las_Personas(Voceros): # Opcion 5 Mostrar
    i = 0
    if len(Voceros) == 0:
        print("Opcion 5...\nNo hay voceros guardados")
    else:
        print("Mostrar todos los VOCEROS\n")
        i = 0
        while True:
            Voceros[i].Mostrar_Persona()
            i = i + 1
            if i+1 > len(Voceros):
                break