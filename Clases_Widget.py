import tkinter as tk

# Clase Boton Para crear un Boton

class Colocar_Boton:
    def __init__(
        self
        ,ventana
        ,texto
        ,color_fondo
        ,color_letra
        ,tipo_letra
        ,ancho_boton
        ,alto_boton
        ,tipo_boton
        ,borde_boton
        ,comando = None
    ):
        self.ventana = ventana
        self.texto = texto
        self.color_fondo = color_fondo
        self.color_letra = color_letra
        self.tipo_letra = tipo_letra
        self.ancho_boton = ancho_boton
        self.alto_boton = alto_boton
        self.tipo_boton = tipo_boton
        self.borde_boton = borde_boton
        self.comando = comando
    
    def crear_boton(
        self
    ):
        boton = tk.Button(
            self.ventana
            ,text = self.texto
            ,bg = self.color_fondo
            ,fg = self.color_letra
            ,font = self.tipo_letra
            ,width = self.ancho_boton
            ,height = self.alto_boton
            ,relief = self.tipo_boton
            ,bd = self.borde_boton
            ,wraplength=100
            ,command = self.comando
        )

        boton.pack(
            side = tk.LEFT
            ,padx = 5
            ,pady = 5
            ,ipadx = 5
            ,ipady = 5
            ,fill = tk.NONE
            ,expand = False
        )

class Etiqueta:
    def __init__(self
        ,ventana
        ,texto
        ,color_fondo
        ,color_letra
        ,tipo_letra
        ,ancho_etiqueta
        ,alto_etiqueta
        ,tipo_etiqueta
        ,borde_etiqueta
    ):
        self.ventana = ventana
        self.texto = texto
        self.color_fondo = color_fondo
        self.color_letra = color_letra
        self.tipo_letra = tipo_letra
        self.ancho_etiqueta = ancho_etiqueta
        self.alto_etiqueta = alto_etiqueta
        self.tipo_etiqueta = tipo_etiqueta
        self.borde_etiqueta = borde_etiqueta

    def crear_etiqueta(
        self
    ):
        self.etiqueta = tk.Label(
            self.ventana
            ,text = self.texto
            ,bg = self.color_fondo
            ,fg = self.color_letra
            ,font = self.tipo_letra
            ,width = self.ancho_etiqueta
            ,height = self.alto_etiqueta
            ,relief = self.tipo_etiqueta
            ,bd = self.borde_etiqueta
            ,wraplength=100
        )

        self.etiqueta.pack(
            side = tk.LEFT
            ,padx = 5
            ,pady = 5
            ,ipadx = 5
            ,ipady = 5
            ,fill = tk.NONE
            ,expand = False
        )
    
    def eliminar_etiqueta(
        self
    ):
        if self.etiqueta.winfo_exist():
            self.etiqueta.destroy()

class Colocar_Entrada:
    def __init__(self,
        ventana
        ,text
        ,tipo_letra_entrada
        ,ancho_entrada
    ):
        self.ventana = ventana
        self.text = text
        self.tipo_letra_entrada = tipo_letra_entrada
        self.ancho_entrada = ancho_entrada
    
    def crear_entrada(
        self
    ):
        self.entry = tk.Entry(
            self.ventana
            ,font=self.tipo_letra_entrada
            ,width=self.ancho_entrada
    )

        self.entry.pack(
            side=tk.LEFT
            ,padx=5
            ,pady=5
            ,ipadx=5
            ,ipady=5
            ,fill=tk.NONE
            ,expand=False
        )

    def guardar_valor_ingresado(
        self
    ):
        self.entry.get()
    
    def vaciar_valor_ingresado(
        self
    ):
        self.entry.delete(0, tk.END)
