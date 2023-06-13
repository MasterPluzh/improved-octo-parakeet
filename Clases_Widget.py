import tkinter as tk

# Clase Boton Para crear un Boton

class Colocar_Boton:
    def __init__(self
        ,ventana
        ,texto,color_fondo,color_letra
        ,tipo_letra,ancho_boton
        ,alto_boton
        ,tipo_boton
        ,borde_boton
        ,comando=None
    ):

        boton = tk.Button(
            ventana
            ,text=texto
            ,bg=color_fondo
            ,fg=color_letra
            ,font=tipo_letra
            ,width=ancho_boton
            ,height=alto_boton
            ,relief=tipo_boton
            ,bd=borde_boton
            ,wraplength=100
            ,command=comando
        )

        boton.pack(
            side=tk.LEFT
            ,padx=5
            ,pady=5
            ,ipadx=5
            ,ipady=5
            ,fill=tk.NONE
            ,expand=False
        )

class Colocar_Etiqueta:
    def __init__(self,ventana
        ,texto,color_fondo,color_letra
        ,tipo_letra,ancho_boton
        ,alto_boton
        ,tipo_boton
        ,borde_boton
    ):

        etiqueta = tk.Label(
            ventana
            ,text=texto
            ,bg=color_fondo
            ,fg=color_letra
            ,font=tipo_letra
            ,width=ancho_boton
            ,height=alto_boton
            ,relief=tipo_boton
            ,bd=borde_boton
            ,wraplength=100
        )

        etiqueta.pack(
            side=tk.LEFT
            ,padx=5
            ,pady=5
            ,ipadx=5
            ,ipady=5
            ,fill=tk.NONE
            ,expand=False
        )

class Colocar_Entrada:
    def __init__(self,
        ventana
        ,text
        ,ancho_entrada
    ):
        entry = tk.Entry(
            ventana
            ,width=ancho_entrada
        )
        entry.pack(
            side=tk.LEFT
            ,padx=5
            ,pady=5
            ,ipadx=5
            ,ipady=5
            ,fill=tk.NONE
            ,expand=False
        )
