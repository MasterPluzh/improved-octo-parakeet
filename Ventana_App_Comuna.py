import tkinter as tk
import Clases_Widget as Clase
import Ventana_Menu_Opciones as Menu

# Ventana

ventana = tk.Tk()
ventana.iconbitmap("icono.ico")

# Funciones

def ventana_menu():
    for widget in ventana.winfo_children():
        widget.destroy()
    
    ventana.title("Menu de Incio")
    ventana.geometry("400x300+500+100")

    tipo_letra = ("Arial",16)
    ancho_boton = 10
    largo_boton = 2
    tipo_boton = "raised"
    borde_boton = 5
    
    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    boton_consejos_comunales = Clase.Colocar_Boton(
        frame
        ,"Consejos Comunales"
        ,"yellow"
        ,"red"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,lambda: Menu.ventana(1)
        )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    boton_voceros = Clase.Colocar_Boton(
        frame
        ,"Voceros"
        ,"blue"
        ,"yellow"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,lambda: Menu.ventana(2)
    )

    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP)

    boton_salir = Clase.Colocar_Boton(
        frame
        ,"Salir"
        ,"red"
        ,"blue"
        ,tipo_letra
        ,ancho_boton
        ,largo_boton
        ,tipo_boton
        ,borde_boton
        ,ventana.quit
    )


# Widgets
# tk.Button = Botones
# tk.Entry = Entradas
# tk.Label = Etiquetas

# Ventana que inicia todo

ventana_menu()

# ventana en buble

ventana.mainloop()
