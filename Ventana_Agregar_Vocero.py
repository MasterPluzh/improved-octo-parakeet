import tkinter as tk
import Clases_Widget as Clase

def ventana(): # Agregar Vocero
    ventana = tk.Toplevel()
    ventana.title("Agregar Vocero")
    ventana.geometry("500x600+450+50")

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

    frame_1 = tk.Frame(
        ventana
        ,padx=10
        ,pady=10
        )
    frame_1.pack(side=tk.TOP)

    frame_2 = tk.Frame(
        ventana
        ,padx=10
        ,pady=10
        )
    frame_2.pack(side=tk.TOP)

    frame_3 = tk.Frame(ventana)
    frame_3.pack(side=tk.TOP)

    frame_4 = tk.Frame(ventana)
    frame_4.pack(side=tk.TOP)

    frame_5 = tk.Frame(ventana)
    frame_5.pack(side=tk.TOP)

    frame_6 = tk.Frame(ventana)
    frame_6.pack(side=tk.TOP)

    frame_7 = tk.Frame(ventana)
    frame_7.pack(side=tk.TOP)

    frame_8 = tk.Frame(ventana)
    frame_8.pack(side=tk.TOP)

    frame_9 = tk.Frame(ventana)
    frame_9.pack(side=tk.TOP)

    frame_10 = tk.Frame(ventana)
    frame_10.pack(side=tk.TOP)

    frame_11 = tk.Frame(ventana)
    frame_11.pack(side=tk.TOP)

    def guardar_persona():
        nombre = insertar_nombre.guardar_valor_ingresado()
        apellido = insertar_apellido.guardar_valor_ingresado()
        cedula = insertar_cedula.guardar_valor_ingresado()
        telefono = insertar_telefono.guardar_valor_ingresado()
        correo = insertar_correo.guardar_valor_ingresado()
        consejo_comunal = insertar_consejo_comunal.guardar_valor_ingresado()
        equipo = insertar_equipo.guardar_valor_ingresado()

        if nombre == None or apellido == None:
            etiqueta_faltan_datos.crear_etiqueta()
        elif cedula == 1:
            etiqueta_guardado.crear_etiqueta()
    
    def vaciar_persona():
        insertar_nombre.vaciar_valor_ingresado()
        insertar_apellido.vaciar_valor_ingresado()
        insertar_cedula.vaciar_valor_ingresado()
        insertar_telefono.vaciar_valor_ingresado()
        insertar_correo.vaciar_valor_ingresado()
        insertar_consejo_comunal.vaciar_valor_ingresado()
        insertar_equipo.vaciar_valor_ingresado()

        etiqueta_guardado.eliminar_etiqueta()
        etiqueta_faltan_datos.eliminar_etiqueta()

    boton_guardar = Clase.Colocar_Boton(
        frame_11
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

    boton_vaciar = Clase.Colocar_Boton(
        frame_11
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
        frame_11
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

    insertar_nombre = Clase.Colocar_Entrada(
        frame_2
        ,"Nombre"
        ,tipo_letra_entrada
        ,18
    )

    insertar_apellido = Clase.Colocar_Entrada(
        frame_2
        ,"Apellido"
        ,tipo_letra_entrada
        ,18
    )

    insertar_cedula = Clase.Colocar_Entrada(
        frame_4
        ,"Cedula"
        ,tipo_letra_entrada
        ,18
    )

    insertar_telefono = Clase.Colocar_Entrada(
        frame_4
        ,"Telefono"
        ,tipo_letra_entrada
        ,18
    )

    insertar_correo = Clase.Colocar_Entrada(
        frame_6
        ,"Correo"
        ,tipo_letra_entrada
        ,38
    )

    insertar_consejo_comunal = Clase.Colocar_Entrada(
        frame_8
        ,"Consejo Comunal"
        ,tipo_letra_entrada
        ,38
    )

    insertar_equipo = Clase.Colocar_Entrada(
        frame_10
        ,"Equipo"
        ,tipo_letra_entrada
        ,38
    )

    etiqueta_nombre = Clase.Etiqueta(
        frame_1
        ,"Nombre"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )

    etiqueta_apellido = Clase.Etiqueta(
        frame_1
        ,"Apellido"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )

    etiqueta_guardado = Clase.Etiqueta(
        frame_1
        ,"Persona Guardada"
        ,"green"
        ,"white"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )

    etiqueta_faltan_datos = Clase.Etiqueta(
        frame_1
        ,"Faltan Datos"
        ,"red"
        ,"white"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )

    etiqueta_cedula = Clase.Etiqueta(
        frame_3
        ,"Cedula"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )

    etiqueta_telefono = Clase.Etiqueta(
        frame_3
        ,"Telefono"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )

    etiqueta_correo = Clase.Etiqueta(
        frame_5
        ,"Correo"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )

    etiqueta_consejo_comunal = Clase.Etiqueta(
        frame_7
        ,"Consejo Comunal"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )

    etiqueta_equipo = Clase.Etiqueta(
        frame_9
        ,"Equipo"
        ,"white"
        ,"black"
        ,tipo_letra_etiqueta
        ,ancho_etiqueta
        ,largo_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    )

    etiqueta_nombre.crear_etiqueta()
    etiqueta_apellido.crear_etiqueta()
    insertar_nombre.crear_entrada()
    insertar_apellido.crear_entrada()

    etiqueta_cedula.crear_etiqueta()
    etiqueta_telefono.crear_etiqueta()
    insertar_cedula.crear_entrada()
    insertar_telefono.crear_entrada()

    etiqueta_correo.crear_etiqueta()
    insertar_correo.crear_entrada()

    etiqueta_consejo_comunal.crear_etiqueta()
    insertar_consejo_comunal.crear_entrada()

    etiqueta_equipo.crear_etiqueta()
    insertar_equipo.crear_entrada()

    boton_guardar.crear_boton()
    boton_vaciar.crear_boton()
    boton_salir.crear_boton()
