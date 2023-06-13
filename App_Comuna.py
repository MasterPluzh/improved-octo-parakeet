import tkinter as tk

# Ventana

ventana = tk.Tk()
ventana.iconbitmap("icono.ico")

# Funciones

def ventana_menu():
    for widget in ventana.winfo_children():
        widget.destroy()
    
    ventana.title("Menu de Incio")
    ventana.geometry("250x300+550+100")

    boton_opcion_consejo_comunal = tk.Button(
        ventana
        ,text="Consejos Comunales"
        ,bg="yellow"
        ,fg="red"
        ,font=("Arial", 16)
        ,width=10
        ,height=2
        ,relief="raised"
        ,bd=5,wraplength=100
        ,command=lambda: ventana_control_opciones(1)
        )
    boton_opcion_consejo_comunal.pack(
        side=tk.TOP
        ,padx=5
        ,pady=5
        ,ipadx=5
        ,ipady=5
        ,fill=tk.NONE
        ,expand=False
        )

    boton_opcion_voceros = tk.Button(
        ventana
        ,text="Voceros"
        ,bg="blue"
        ,fg="yellow"
        ,font=("Arial", 16)
        ,width=10,height=2
        ,relief="raised"
        ,bd=5
        ,wraplength=100
        ,command=lambda: ventana_control_opciones(2)
        )
    boton_opcion_voceros.pack(
        side=tk.TOP
        ,padx=5
        ,pady=5
        ,ipadx=5
        ,ipady=5
        ,fill=tk.NONE
        ,expand=False
        )

    boton_salir = tk.Button(
        ventana
        ,text="Salir"
        ,bg="red"
        ,fg="yellow"
        ,font=("Arial", 16)
        ,width=10
        ,height=2
        ,relief="raised"
        ,bd=5
        ,wraplength=100
        ,command=ventana.quit
        )
    boton_salir.pack(
        side=tk.TOP
        ,padx=5
        ,pady=5
        ,ipadx=5
        ,ipady=5
        ,fill=tk.NONE
        ,expand=False
        )

def ventana_control_opciones(consejo_or_vocero):
    for widget in ventana.winfo_children():
        widget.destroy()
    
    if consejo_or_vocero == 1: ventana.title("Control de Consejos Comunales")
    elif consejo_or_vocero == 2: ventana.title("Control de Voceros")

    # ventana.title("Control de Voceros")
    ventana.geometry("400x300+475+100")

    frame_1 = tk.Frame(ventana)
    frame_1.pack(side=tk.TOP)

    boton_opcion_agregar = tk.Button(
        frame_1,
        text="Agregar"
        ,bg="white"
        ,fg="black"
        ,font=("Arial",16)
        ,width=10
        ,height=2
        ,relief="raised"
        ,bd=5
        ,wraplength=100
        )
    boton_opcion_agregar.pack(
        side=tk.LEFT
        ,padx=5
        ,pady=5
        ,ipadx=5
        ,ipady=5
        ,fill=tk.NONE
        ,expand=False
        )

    boton_opcion_quitar = tk.Button(
        frame_1,text="Quitar"
        ,bg="white"
        ,fg="black"
        ,font=("Arial",16)
        ,width=10
        ,height=2
        ,relief="raised"
        ,bd=5
        ,wraplength=100
        )
    boton_opcion_quitar.pack(
        side=tk.LEFT
        ,padx=5
        ,pady=5
        ,ipadx=5
        ,ipady=5
        ,fill=tk.NONE
        ,expand=False
        )

    frame_2 = tk.Frame(ventana)
    frame_2.pack(side=tk.TOP)

    boton_opcion_editar = tk.Button(
        frame_2
        ,text="Editar"
        ,bg="white"
        ,fg="black"
        ,font=("Arial",16)
        ,width=10,
        height=2,
        relief="raised"
        ,bd=5
        ,wraplength=100
        )
    boton_opcion_editar.pack(
        side=tk.LEFT
        ,padx=5
        ,pady=5
        ,ipadx=5
        ,ipady=5
        ,fill=tk.NONE
        ,expand=False
        )

    boton_opcion_consultar = tk.Button(
        frame_2
        ,text="Consultar"
        ,bg="white"
        ,fg="black"
        ,font=("Arial",16)
        ,width=10
        ,height=2
        ,relief="raised"
        ,bd=5
        ,wraplength=100
        )
    boton_opcion_consultar.pack(
        side=tk.LEFT
        ,padx=5
        ,pady=5
        ,ipadx=5
        ,ipady=5
        ,fill=tk.NONE
        ,expand=False
        )

    frame_3 = tk.Frame(ventana)
    frame_3.pack(side=tk.TOP)

    boton_opcion_mostrar = tk.Button(
        frame_3
        ,text="Mostrar"
        ,bg="white"
        ,fg="black"
        ,font=("Arial",16)
        ,width=10
        ,height=2
        ,relief="raised"
        ,bd=5
        ,wraplength=100
        )
    boton_opcion_mostrar.pack(
        side=tk.LEFT
        ,padx=5
        ,pady=5
        ,ipadx=5
        ,ipady=5
        ,fill=tk.NONE
        ,expand=False
        )

    boton_volver = tk.Button(
        frame_3
        ,text="Volver"
        ,bg="white"
        ,fg="black"
        ,font=("Arial",16)
        ,width=10
        ,height=2
        ,relief="raised"
        ,bd=5
        ,wraplength=100
        ,command=ventana_menu
        )
    boton_volver.pack(
        side=tk.TOP
        ,padx=5
        ,pady=5
        ,ipadx=5
        ,ipady=5
        ,fill=tk.NONE
        ,expand=False
        )

# Widgets
# tk.Button = Botones
# tk.Entry = Entradas
# tk.Label = Etiquetas

# Ventana que inicia todo

ventana_menu()

# ventana en buble

ventana.mainloop()