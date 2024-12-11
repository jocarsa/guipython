import tkinter as tk

ventana = tk.Tk()
ventana.title("Programa de Jose Vicente")
ventana.geometry("512x512")

barra_menu = tk.Menu(ventana)

menu_archivo = tk.Menu(
    barra_menu,
    tearoff=0
    )
barra_menu.add_cascade(
    label="Archivo",
    menu=menu_archivo
    )

ventana.config(menu=barra_menu)

panel_bienvenida = tk.Frame(ventana)
panel_bienvenida.pack()

titulo = tk.Label(
    panel_bienvenida,
    text="Programa de Jose Vicente"
    )
titulo.pack(padx=50,pady=50)

ventana.mainloop()