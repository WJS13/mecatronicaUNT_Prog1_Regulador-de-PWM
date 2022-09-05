import tkinter as tk
from tkinter import ttk, messagebox
from tokenize import String
from turtle import color, right, width
from time import *
from serial import *
from PIL import ImageTk, Image
import serial, time

#--------------root--------------

raiz=tk.Tk()

raiz.title("Regulador de Voltaje 1.0")

raiz.resizable(False,False)

raiz.geometry("290x230")

raiz.config(bg="#637A85")

raiz.iconbitmap("alto_voltaje.ico")

#--------------Variables---------

datos_impresos=tk.StringVar()
dato_fuente=tk.StringVar()
dato_porcentual=tk.StringVar()
dato_salida=tk.StringVar()
puerto=tk.StringVar()

#--------------Functions ("voltaje" va de 0 a 255)--------------

def mserror_valores():
    error_valores=messagebox.showinfo("Error", """Por favor, ingrese
    valores válidos""")

def mserror_puertos():
    error_puertos=messagebox.showinfo("Error", """El arduino no se encuentra conectado al puerto especificado,
    conecte el arduino o ingrese un puerto diferente""")

def iniciar():

    try:
        porcentaje = float(barra.get()*10)
        entrada = float(dato_fuente.get())
        voltaje_entregado=porcentaje*entrada/100
        if voltaje_entregado >=0.0 and voltaje_entregado<=entrada:
            dato_porcentual.set(str(int(porcentaje))+"%")
            dato_salida.set(round(voltaje_entregado,2))
            voltaje_arduino = serial.Serial("COM5",9600)
            enviado = str(int(porcentaje*255/100))
            voltaje_arduino.write((enviado+'\n').encode())
        actualizar = miframe.after(100,iniciar)
    except SerialException:
        mserror_puertos()
    except:
        mserror_valores()

#--------------frame principal--------------

miframe=tk.Frame(raiz, width=10, height=50, cursor="plus")

miframe.grid(row=0, column=0, padx=0, pady=0)

miframe.config(bd=20)

#--------------Ejecución de gráfica--------------

ingresa_puerto=tk.Label(miframe, text="Nombre del puerto:")
ingresa_puerto.grid(row=0,column=0)

nombre_puerto=ttk.Entry(miframe, textvariable=puerto, width=6)
nombre_puerto.grid(row=0,column=1, padx=3, pady=3)

#--row 0--
indicacion_vol=tk.Label(miframe, text="Voltaje de la fuente: ",justify=tk.CENTER)
indicacion_vol.grid(row=1, column=0, padx=1, pady=1)

voltaje1=ttk.Entry(miframe, textvariable=dato_fuente, justify=tk.CENTER, width=6)
voltaje1.grid(row=1,column=1, padx=3, pady=3)


#--row 1--
etq_barra=tk.Label(miframe, text="Ajuste porcentual: ",justify=tk.CENTER)
etq_barra.grid(row=2, column=0, padx=1, pady=1, columnspan = 2)


#--row 2--
barra = ttk.Scale(miframe, to = 10, from_ = 0, orient = 'horizontal',length = 250 , style = 'Horizontal.TScale')
barra.grid(row=3,column=0, columnspan = 2)


#--row 3--
voltaje1=ttk.Entry(miframe, textvariable=dato_porcentual, justify=tk.CENTER,width=6)
voltaje1.grid(row=4,column=0, padx=3, pady=3,columnspan = 2)


#--row 4--
indicacion_est=tk.Label(miframe, text="Voltaje establecido: ",justify=tk.CENTER)
indicacion_est.grid(row=5, column=0, padx=1, pady=1)

voltaje2=ttk.Entry(miframe, textvariable=dato_salida, justify=tk.CENTER, width=6)
voltaje2.grid(row=5,column=1, padx=3, pady=3)


#--row 5--
boton_voltaje=ttk.Button(miframe, text="Iniciar", command=iniciar)
boton_voltaje.grid(row=6, column=0, padx=10, pady=10, columnspan = 2)


raiz.mainloop()

