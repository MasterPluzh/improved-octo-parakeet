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
                if(consejo_or_vocero == 1): print("Agregar CONSEJO COMUNAL:\n")

                elif(consejo_or_vocero == 2):
                    print("Agregar VOCERO:\n")
                    Vocero = persona.Persona("", "", "", "", "", 0, "")
                    Vocero.addPersona()
                    Voceros.append(Vocero)
                    print("Datos del Vocero agregados")
                
                print("\n")
            
            # Opcion Quitar, ya sea Consejo Comunal o Vocero
            if(opcion == 2):
                if(consejo_or_vocero == 1): print("Quitar CONSEJO COMUNAL\n")

                elif(consejo_or_vocero == 2):
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

                print("\n")

            # Opcion Consulta, ya sea Consejo Comunal o Vocero
            if(opcion == 3):
                if(consejo_or_vocero == 1): print("Consultar CONSEJO COMUNAL\n")

                elif(consejo_or_vocero == 2):
                    print("Consultar VOCERO\n")

                print("\n")

            # Opcion Editar, ya sea Consejo Comunal o Vocero
            if(opcion == 4):
                editar = ""

                if(consejo_or_vocero == 1):
                    print("Actualizar CONSEJO COMUNAL\n")
                
                elif(consejo_or_vocero == 2):
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

                                Vocero.editarPersona()
                                Voceros.insert(i, Vocero)

                                print("\nDatos del Vocero actualizados")
                                break

                            i = i + 1
                            if i+1 > len(Voceros):
                                print("\nPersona no encontrada")
                                break
                
                print("\n")

            # Opcion Mostrar, ya sea Consejo Comunal o Vocero
            if(opcion == 5):
                if(consejo_or_vocero == 1):
                    print("Mostrar todos los CONSEJOS COMUNALES\n")
                
                elif(consejo_or_vocero == 2):
                    i = 0

                    if len(Voceros) == 0:
                        print("Opcion 5...\nNo hay voceros guardados")
                    
                    else:
                        print("Mostrar todos los VOCEROS\n")
                        i = 0
                        while True:
                            Voceros[i].mostrarPersona()
                            i = i + 1
                            if i+1 > len(Voceros):
                                break
                
                print("\n")

# Funcion Principal
def main():
    menu()

# Inicio
main()

# Juan = persona.Persona("Juan", "1", "1", "1", "1", 1, "1")
# lista_personas = []
# Juan.addPersona()
# lista_personas.append(Juan)
# Juan = persona.Persona("Pedro", "2", "2", "2", "2", 2, "2")
# Juan.addPersona()
# lista_personas.append(Juan)

# lista_personas[0].mostrarPersona()
# lista_personas[1].mostrarPersona()