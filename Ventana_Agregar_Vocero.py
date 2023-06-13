import tkinter as tk
import Clases_Widget as Clase

def ventana(): # Agregar Vocero
    ventana = tk.Toplevel()
    ventana.title("Agregar Vocero")
    ventana.geometry("400x600+500+100")

    tipo_letra = ("Arial",11)
    ancho_boton = 16
    largo_boton = 1
    tipo_boton = "raised"
    borde_boton = 5

    # Y si creo un fragmento de fragmentos?

    frame = tk.Frame(
        ventana
        ,padx=10
        ,pady=10
        )
    frame.pack(side=tk.TOP)

    etiqueta = Clase.Colocar_Etiqueta(
        frame
        ,"Nombre"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
    )

    etiqueta = Clase.Colocar_Etiqueta(
        frame
        ,"Apellido"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
    )
    
    frame = tk.Frame(
        ventana
        ,padx=10
        ,pady=10
        )
    frame.pack(side=tk.TOP)

    insertar = Clase.Colocar_Entrada(
        frame
        ,"Nombre"
        ,10
    )

    insertar = Clase.Colocar_Entrada(
        frame
        ,"Apellido"
        ,10
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    etiqueta_nombre = Clase.Colocar_Etiqueta(
        frame
        ,"Cedula"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
    )

    etiqueta_apellido = Clase.Colocar_Etiqueta(
        frame
        ,"Telefono"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
    )
    
    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    insertar = Clase.Colocar_Entrada(
        frame
        ,"Cedula"
        ,10
    )

    insertar = Clase.Colocar_Entrada(
        frame
        ,"Telefono"
        ,10
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    etiqueta_nombre = Clase.Colocar_Etiqueta(
        frame
        ,"Correo"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
    )
    
    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    insertar = Clase.Colocar_Entrada(
        frame
        ,"Correo"
        ,50
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    etiqueta_nombre = Clase.Colocar_Etiqueta(
        frame
        ,"Consejo Comunal"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
    )
    
    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    insertar = Clase.Colocar_Entrada(
        frame
        ,"Consejo Comunal"
        ,50
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    etiqueta_nombre = Clase.Colocar_Etiqueta(
        frame
        ,"Equipo"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
    )
    
    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    insertar = Clase.Colocar_Entrada(
        frame
        ,"Equipo"
        ,50
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    boton = Clase.Colocar_Boton(
        frame
        ,"Guardar"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,None
    )

    boton = Clase.Colocar_Boton(
        frame
        ,"Salir"
        ,"white"
        ,"black"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,ventana.destroy
    )
