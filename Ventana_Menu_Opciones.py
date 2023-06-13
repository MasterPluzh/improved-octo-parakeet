import tkinter as tk
import Clases_Widget as Clase
import Ventana_Agregar_Vocero as Vocero_Opcion_1

def ventana(consejo_or_vocero): # Control de Opciones
    ventana = tk.Toplevel()

    if consejo_or_vocero == 1:
        ventana.title("Control de Consejos Comunales")
    
    elif consejo_or_vocero == 2:
        ventana.title("Control de Voceros")
    
    ventana.geometry("400x300+500+100")

    tipo_letra = ("Arial",16)
    ancho_boton = 10
    largo_boton = 2
    tipo_boton = "raised"
    borde_boton = 5

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    if consejo_or_vocero == 1:
        comando = Vocero_Opcion_1.ventana
    
    elif consejo_or_vocero == 2:
        comando = Vocero_Opcion_1.ventana
    
    boton_opcion_agregar = Clase.Colocar_Boton(
        frame
        ,"Agregar"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,comando
    )

    boton_opcion_quitar = Clase.Colocar_Boton(
        frame
        ,"Quitar"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,None
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    boton_opcion_editar = Clase.Colocar_Boton(
        frame
        ,"Editar"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,None
    )

    boton_opcion_consultar = Clase.Colocar_Boton(
        frame
        ,"Consultar"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,None
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    boton_opcion_mostrar = Clase.Colocar_Boton(
        frame
        ,"Mostrar"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,None
    )

    boton_opcion_volver = Clase.Colocar_Boton(
        frame
        ,"Volver"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,ventana.destroy
    )
