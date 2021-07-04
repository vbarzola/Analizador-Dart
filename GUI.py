
import random as rd
import tkinter as tk
from sintactico import analizar_sintac
from index import analizar_lexico


def validar_mensaje_errores(output, tipo):
    print("output", output)
    output_codigo.config(state=tk.NORMAL)
    output_codigo.delete('1.0', tk.END)
    if output != '':
        output_codigo.insert(1.0, output)
    else:
        output_codigo.insert(1.0, f"No hay errores en el analizador {tipo}")
    output_codigo.config(state=tk.DISABLED)


def analizar_lex_event():
    text = input_codigo.get("1.0", "end-1c")
    output = analizar_lexico(text)
    validar_mensaje_errores(output, "lexico")


def analizar_sint_event():
    text = input_codigo.get("1.0", "end-1c")
    estado_output = analizar_sintac(text)
    n_err_sint = estado_output.err_sintacticos
    err_sint = estado_output.descr_err_sintacticos
    text = input_codigo.get("1.0", "end-1c")
    validar_mensaje_errores(err_sint, "sintáctico")


def obtener_ejemplo_random(input):
    indice = rd.randint(1, 8)
    with open(f'./ejemplos/ejemplo{indice}.txt') as f:
        ejemplo = ''.join(f.readlines())
        input.delete('1.0', tk.END)
        input.insert(1.0, ejemplo)


ventana = tk.Tk()
ventana.title("Analizador Dart")
ventana.geometry("1200x690")
ventana.resizable(False, False)
ventana.config(bg="#323233")

canvas = tk.Canvas(ventana, bg="#02589B", width=1200,
                   height=30, bd=0, highlightthickness=0, relief='ridge')
canvas.pack()

# TITULO
photo_dart = tk.PhotoImage(file="./imagenes/nuevo.png")
titulo = tk.Label(
    ventana, text='Lenguaje de programación Dart ', font="Arial 40", bg="#323233", fg='#2CB7F6', image=photo_dart, compound=tk.RIGHT)
titulo.place(x=70, y=60)

# INPUT
canvas_input_img = tk.Canvas(ventana, width=510,
                             height=415, bd=0, highlightthickness=0, relief='ridge', bg="#323233")

input_img = tk.PhotoImage(file="./imagenes/input_text.png")
canvas_input_img.create_image(255, 207.5, image=input_img)
input_codigo = tk.Text(ventana, height=24, width=57,
                       bg="#C4C4C4", fg="#27868B",  bd=0, highlightthickness=0, relief='ridge', wrap="word")

canvas_input_img.place(x=55, y=140)
input_codigo.place(x=75, y=160)

# OUTPUT
canvas_output_img = tk.Canvas(ventana, width=510,
                              height=415, bd=0, highlightthickness=0, relief='ridge', bg="#323233")
canvas_output_img.place(x=595, y=140)
output_img = tk.PhotoImage(file="./imagenes/input_text.png")
canvas_output_img.create_image(255, 207.5, image=output_img)
output_codigo = tk.Text(ventana, height=24, width=57,
                        bg="#C4C4C4", fg="#616161",  bd=0, highlightthickness=0, relief='ridge', wrap="word")
output_codigo.place(x=615, y=160)

# BOTONES
photo = tk.PhotoImage(file="./imagenes/play_arrow.png")
boton_random = tk.Button(
    ventana, text="RANDOM", bg='#6A6A6A', fg='white', padx=5, pady=1,  command=lambda: obtener_ejemplo_random(input_codigo))
boton_lexico = tk.Button(
    ventana, text="Analizador léxico", bg='#6A6A6A', fg='white', image=photo, compound=tk.LEFT, padx=5, pady=5, command=analizar_lex_event)
boton_sintactico = tk.Button(
    ventana, text="Analizador sintactico", bg='#6A6A6A', fg='white', image=photo, compound=tk.LEFT, padx=5, pady=5, command=analizar_sint_event)

boton_random.place(x=270, y=565)
boton_lexico.place(x=440, y=600)
boton_sintactico.place(x=600, y=600)

ventana.mainloop()
