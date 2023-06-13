import tkinter as tk

# Ventana

ventana = tk.Tk()
ventana.iconbitmap("icono.ico")

# Clase Boton Para crear un Boton

class Colocar_Boton:
    def __init__(self,ventana,texto,color_fondo,color_letra,comando=None):
        boton = tk.Button(
            ventana
            ,text=texto
            ,bg=color_fondo
            ,fg=color_letra
            ,font=("Arial",16)
            ,width=10
            ,height=2
            ,relief="raised"
            ,bd=5
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

# Funciones

def ventana_menu():
    for widget in ventana.winfo_children():
        widget.destroy()
    
    ventana.title("Menu de Incio")
    ventana.geometry("250x300+550+100")

    frame = tk.Frame(ventana), frame.pack(side=tk.TOP)

    boton_opcion_consejo_comunal = Colocar_Boton(
        frame
        ,"Consejos Comunales"
        ,"yellow"
        ,"red"
        ,lambda: ventana_control_opciones(1)
        )

    frame = tk.Frame(ventana), frame.pack(side=tk.TOP)

    boton_opcion_vocero = Colocar_Boton(
        frame
        ,"Voceros"
        ,"blue"
        ,"yellow"
        ,lambda: ventana_control_opciones(1)
        )

    frame = tk.Frame(ventana), frame.pack(side=tk.TOP)

    boton_salir = Colocar_Boton(
        frame
        ,"Salir"
        ,"red"
        ,"blue"
        ,ventana.quit
        )

def ventana_control_opciones(consejo_or_vocero):
    for widget in ventana.winfo_children():
        widget.destroy()
    
    if consejo_or_vocero == 1:
        ventana.title("Control de Consejos Comunales")
    
    elif consejo_or_vocero == 2:
        ventana.title("Control de Voceros")

    # ventana.title("Control de Voceros")
    ventana.geometry("400x300+475+100")

    frame_1 = tk.Frame(ventana),frame_1.pack(side=tk.TOP)

    boton_opcion_agregar = Colocar_Boton(
        frame_1
        ,"Agregar"
        ,"white"
        ,"black"
        ,None
        )

    boton_opcion_quitar = Colocar_Boton(
        frame_1
        ,"Quitar"
        ,"white"
        ,"black"
        ,None
        )

    frame_2 = tk.Frame(ventana)
    frame_2.pack(side=tk.TOP)

    boton_opcion_editar = Colocar_Boton(
        frame_2
        ,"Editar"
        ,"white"
        ,"black"
        ,None
        )

    boton_opcion_consultar = Colocar_Boton(
        frame_2
        ,"Consultar"
        ,"white"
        ,"black"
        ,None
        )

    frame_3 = tk.Frame(ventana),frame_3.pack(side=tk.TOP)

    boton_opcion_mostrar = Colocar_Boton(
        frame_3
        ,"Mostrar"
        ,"white"
        ,"black"
        ,None
        )

    boton_opcion_volver = Colocar_Boton(
        frame_3
        ,"Volver"
        ,"white"
        ,"black"
        ,ventana_menu
        )

# Widgets
# tk.Button = Botones
# tk.Entry = Entradas
# tk.Label = Etiquetas

# Ventana que inicia todo

ventana_menu()

# ventana en buble

ventana.mainloop()
