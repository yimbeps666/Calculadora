import tkinter as tk

def suma():
    try:
        resultado.set(float(num1.get()) + float(num2.get()))
    except ValueError:
        resultado.set("Error")

def resta():
    try:
        resultado.set(float(num1.get()) - float(num2.get()))
    except ValueError:
        resultado.set("Error")

def multiplicacion():
    try:
        resultado.set(float(num1.get()) * float(num2.get()))
    except ValueError:
        resultado.set("Error")

def division():
    try:
        resultado.set(float(num1.get()) / float(num2.get()))
    except ValueError:
        resultado.set("Error")
    except ZeroDivisionError:
        resultado.set("Infinito")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Variables para almacenar los números y el resultado
num1 = tk.StringVar()
num2 = tk.StringVar()
resultado = tk.StringVar()

# Crear los campos de entrada
tk.Label(ventana, text="Número 1:").grid(row=0, column=0)
tk.Entry(ventana, textvariable=num1).grid(row=0, column=1)

tk.Label(ventana, text="Número 2:").grid(row=1, column=0)
tk.Entry(ventana, textvariable=num2).grid(row=1, column=1)

# Crear los botones de operaciones
tk.Button(ventana, text="Sumar", command=suma).grid(row=2, column=0)
tk.Button(ventana, text="Restar", command=resta).grid(row=2, column=1)
tk.Button(ventana, text="Multiplicar", command=multiplicacion).grid(row=3, column=0)
tk.Button(ventana, text="Dividir", command=division).grid(row=3, column=1)

# Mostrar el resultado
tk.Label(ventana, text="Resultado:").grid(row=4, column=0)
tk.Label(ventana, textvariable=resultado).grid(row=4, column=1)

# Iniciar la aplicación
ventana.mainloop()
