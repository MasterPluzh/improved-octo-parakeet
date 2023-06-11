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
    def inDatos(self, editar, nombre, apellido, cedula, telefono, correo, consejo, equipo):
        if editar == 0 or editar == 1: self.setNombre(nombre = input("Nombre: "))

        if editar == 0 or editar == 2: self.setApellido(apellido = input("Apellido: "))

        if editar == 0 or editar == 3: self.setCedula(cedula = input("Cedula de Identidad: "))

        if editar == 0 or editar == 4: self.setTelefono(telefono = input("Numero de Telefono: "))

        if editar == 0 or editar == 5: self.setCorreo(correo = input("Correo Electronico: "))

        if editar == 0 or editar == 6: self.setConsejo(consejo = input("Consejo Comunal: "))

        if editar == 0 or editar == 7: self.setEquipo(equipo = input("Unidad o Comite: "))
    
    def mostrarPersona(self): # Mostrar datos de una Persona
        print("Nombre y Apellido:", self.getNombre(), self.getApellido())
        print("Cedula:", self.getCedula())
        print("Telefono:", self.getTelefono())
        print("Correo:", self.getCorreo())
        print("Consejo Comunal:", self.getConsejo())
        print("Unidad o Comite:", self.getEquipo(), "\n")

    # Agregar Persona (Opcion 1 del Menu Vocero)
    def addPersona(self):
        # Editar/Nombre/Apellido/Cedula/Telefono/Correo/ConsejoComunal/UnidadOComite
        self.inDatos(0, "", "", "", "", "", 0, "")
    
    # Actualizar datos de una persona (Opcion 4 del Menu Vocero)
    def editarPersona(self):
        que_editar = 0
        opcion = int(input("Actualizar (1) un dato o (2) todos los datos\n\nOpcion: "))
        
        if opcion == 1:
            print("(1) Nombre\n(2) Apellido\n(3) Cedula\n(4) Telefono\n(5) Correo\n(6) Consejo Comunal\n(7) Equipo\n")
            que_editar = int(input("Opcion: "))
        
        if opcion == 1 or opcion == 2: self.inDatos(que_editar, "", "", "", "", "", 0, "")