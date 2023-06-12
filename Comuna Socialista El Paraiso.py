# Clase Comuna

# Clase Consejo Comunal

import persona # modulo de personas/voceros

# Menu de Opciones
def menu():
    MaxVoceros = 3
    Vocero = persona.Persona("", "", "", "", "", 0, "")
    Voceros = []

    while True:
        print("MENU DE OPCIONES\n")
        consejo_or_vocero = int(input(" 1.Consejos Comunales\n 2.Voceros\n 0.Salir\n\nOpcion: "))
        print("\n")
        
        if(consejo_or_vocero == 0): break
        
        # Primer sub menu, Agregar, Quitar, Consltar, Actualizar, Mostrar
        while True:
            if(consejo_or_vocero == 1): print("CONSEJOS COMUNALES\n")

            if(consejo_or_vocero == 2): print("VOCEROS\n")
            
            print("  1.Agregar")
            print("  2.Quitar")
            print("  3.Consultar")
            print("  4.Actualizar")
            print("  5.Mostrar todos")
            print("  0.Anterior\n")
            opcion = int(input("Opcion: "))
            print("\n")
            
            if(opcion == 0): break
            
            # Opcion Agregar, ya sea Consejo Comunal o Vocero
            if(opcion == 1):
                if(consejo_or_vocero == 1):
                    print("Agregar CONSEJO COMUNAL:\n")

                elif(consejo_or_vocero == 2): persona.Agregar_La_Persona(Vocero, Voceros)
                
                print("\n")
            
            # Opcion Quitar, ya sea Consejo Comunal o Vocero
            if(opcion == 2):
                if(consejo_or_vocero == 1):
                    print("Quitar CONSEJO COMUNAL\n")

                elif(consejo_or_vocero == 2): persona.Eliminar_La_Persona(Vocero, Voceros)

                print("\n")

            # Opcion Consulta, ya sea Consejo Comunal o Vocero
            if(opcion == 3):
                if(consejo_or_vocero == 1):
                    print("Consultar CONSEJO COMUNAL\n")

                elif(consejo_or_vocero == 2): persona.Consultar_La_Persona(Voceros)

                print("\n")

            # Opcion Editar, ya sea Consejo Comunal o Vocero
            if(opcion == 4):
                editar = ""

                if(consejo_or_vocero == 1):
                    print("Actualizar CONSEJO COMUNAL\n")
                
                elif(consejo_or_vocero == 2): persona.Editar_La_Persona(Vocero, Voceros)
                
                print("\n")

            # Opcion Mostrar, ya sea Consejo Comunal o Vocero
            if(opcion == 5):
                if(consejo_or_vocero == 1):
                    print("Mostrar todos los CONSEJOS COMUNALES\n")
                
                elif(consejo_or_vocero == 2): persona.Mostrar_Las_Personas(Voceros)
                
                print("\n")

# Funcion Principal
def main():
    menu()

# Inicio
main()