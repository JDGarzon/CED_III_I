import tkinter as tk
from PIL import Image, ImageTk
import novel as nv
# Crear una instancia de la ventana principal
ventana = tk.Tk()
ventana.title("Game")
nv.setDestroy(lambda: ventana.destroy())
# Cambiar el tamaño de la ventana a 800x400 píxeles
ventana.geometry("1200x600")

# Cargar la imagen de fondo
imagen_fondo = Image.open("text.jpg")  # Cambia la ruta a tu imagen de fondo
imagen_fondo = imagen_fondo.resize((1200, 600), Image.ANTIALIAS)  # Ajusta el tamaño a la ventana
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un widget Canvas para mostrar la imagen de fondo
canvas = tk.Canvas(ventana, width=1200, height=600)
canvas.grid(row=0, column=0)

# Colocar la imagen de fondo en el Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=imagen_fondo)

# Crear un área de texto
area_texto = tk.Text(canvas, height=17, width=80,borderwidth=0,relief="flat",wrap=tk.WORD,  bg="SystemButtonFace",font=("Times New Roman", 16, "italic"))
area_texto.place(x=160, y=100)  # Ajusta la posición del área de texto
area_texto.insert(tk.END, nv.dialogos(0,"1"))
area_texto.config(state=tk.DISABLED)
# Función para cerrar la ventana

text_name = tk.Text(canvas, height=2, width=25,borderwidth=0,relief="flat",wrap=tk.WORD,  bg="SystemButtonFace",font=("Times New Roman", 12, "italic"))
text_name.place(x=160, y=530) 
text_name.insert(tk.END, "Escribe el nombre")

def cerrar_ventana():
    nv.destroyer.executeDestroy()

def opcionA():
    area_texto.config(state=tk.NORMAL)
    area_texto.delete('1.0', tk.END)
    area_texto.insert(tk.END, nv.advance("a",nv.current))
    area_texto.config(state=tk.DISABLED)

def opcionB():
    area_texto.config(state=tk.NORMAL)
    area_texto.delete('1.0', tk.END)
    area_texto.insert(tk.END, nv.advance("b",nv.current))
    area_texto.config(state=tk.DISABLED)

def cambiar():
    nv.changeName(text_name.get("1.0",tk.END))

# Crear un botón "Cerrar" y centrarlo en la ventana
boton_A = tk.Button(ventana, text="  A  ", command=opcionA, font=("Arial", 14))
boton_A.grid(row=1, column=0, pady=20)

boton_B = tk.Button(ventana, text="  B  ", command=opcionB, font=("Arial", 14))
boton_B.grid(row=1, column=0, pady=20)

boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana, font=("Arial", 14))
boton_cerrar.grid(row=1, column=0, pady=20)

boton_cambiar = tk.Button(ventana, text="Cambiar", command=cambiar, font=("Arial", 14))
boton_cambiar.grid(row=1, column=0, pady=20)

# Centrar el botón "Cerrar" en el Canvas
a=560
canvas.create_window(a, 550, window=boton_A)
canvas.create_window(a+100, 550, window=boton_B)
canvas.create_window(1100, 550, window=boton_cerrar)
canvas.create_window(100, 550, window=boton_cambiar)
# Iniciar el bucle principal de la aplicación
ventana.mainloop()
