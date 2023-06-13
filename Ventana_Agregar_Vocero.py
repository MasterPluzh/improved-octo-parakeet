import tkinter as tk
import Clases_Widget as Clase

def ventana(): # Agregar Vocero
    ventana = tk.Toplevel()
    ventana.title("Agregar Vocero")
    ventana.geometry("500x550+400+50")

    # Caracteristicas Boton
    tipo_letra_boton = ("Arial",14)
    ancho_boton = 14
    largo_boton = 1
    tipo_boton = "raised"
    borde_boton = 5

    # Caracteristicas para las etiquetas
    tipo_letra_etiqueta = ("Arial",13)
    ancho_etiqueta = 12
    largo_etiqueta = 1
    tipo_etiqueta = "groove"
    borde_etiqueta = 5

    # Caracteristicas para las entradas
    tipo_letra_entrada = ("Arial", 12)

    # Y si creo un fragmento de fragmentos?

    frame = tk.Frame(
        ventana
        ,padx=10
        ,pady=10
        )
    frame.pack(side=tk.TOP)

    etiqueta_nombre = Clase.Colocar_Etiqueta(
        frame
        ,"Nombre"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )

    etiqueta_apellido = Clase.Colocar_Etiqueta(
        frame
        ,"Apellido"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )
    
    frame = tk.Frame(
        ventana
        ,padx=10
        ,pady=10
        )
    frame.pack(side=tk.TOP)

    insertar_nombre = Clase.Colocar_Entrada(
        frame
        ,"Nombre"
        ,tipo_letra_entrada
        ,18
    )

    insertar_apellido = Clase.Colocar_Entrada(
        frame
        ,"Apellido"
        ,tipo_letra_entrada
        ,18
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    etiqueta_cedula = Clase.Colocar_Etiqueta(
        frame
        ,"Cedula"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )

    etiqueta_telefono = Clase.Colocar_Etiqueta(
        frame
        ,"Telefono"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )
    
    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    insertar_cedula = Clase.Colocar_Entrada(
        frame
        ,"Cedula"
        ,tipo_letra_entrada
        ,18
    )

    insertar_telefono = Clase.Colocar_Entrada(
        frame
        ,"Telefono"
        ,tipo_letra_entrada
        ,18
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    etiqueta_correo = Clase.Colocar_Etiqueta(
        frame
        ,"Correo"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )
    
    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    insertar_correo = Clase.Colocar_Entrada(
        frame
        ,"Correo"
        ,tipo_letra_entrada
        ,38
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    etiqueta_consejo_comunal = Clase.Colocar_Etiqueta(
        frame
        ,"Consejo Comunal"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )
    
    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    insertar_consejo_comunal = Clase.Colocar_Entrada(
        frame
        ,"Consejo Comunal"
        ,tipo_letra_entrada
        ,38
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    etiqueta_equipo = Clase.Colocar_Etiqueta(
        frame
        ,"Equipo"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )
    
    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    insertar_equipo = Clase.Colocar_Entrada(
        frame
        ,"Equipo"
        ,tipo_letra_entrada
        ,38
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    def guardar_persona():
        nombre = insertar_nombre.guardar_valor_ingresado()
        apellido = insertar_apellido.guardar_valor_ingresado()
        cedula = insertar_cedula.guardar_valor_ingresado()
        telefono = insertar_telefono.guardar_valor_ingresado()
        correo = insertar_correo.guardar_valor_ingresado()
        consejo_comunal = insertar_consejo_comunal.guardar_valor_ingresado()
        equipo = insertar_equipo.guardar_valor_ingresado()
    
    boton_guardar = Clase.Colocar_Boton(
        frame
        ,"Guardar"
        ,"white"
        ,"black"
        ,tipo_letra_boton
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,guardar_persona
    )

    def vaciar_persona():
        insertar_nombre.vaciar_valor_ingresado()
        insertar_apellido.vaciar_valor_ingresado()
        insertar_cedula.vaciar_valor_ingresado()
        insertar_telefono.vaciar_valor_ingresado()
        insertar_correo.vaciar_valor_ingresado()
        insertar_consejo_comunal.vaciar_valor_ingresado()
        insertar_equipo.vaciar_valor_ingresado()

    boton_vaciar = Clase.Colocar_Boton(
        frame
        ,"Vaciar"
        ,"white"
        ,"black"
        ,tipo_letra_boton
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,vaciar_persona
    )

    boton_salir = Clase.Colocar_Boton(
        frame
        ,"Salir"
        ,"white"
        ,"black"
        ,tipo_letra_boton
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,ventana.destroy
    )
