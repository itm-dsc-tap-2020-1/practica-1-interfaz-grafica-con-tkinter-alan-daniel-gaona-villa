import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox


def funcion_click():
    
    if(entrada.get() == '' or entrada1.get() == '' or entrada2.get() == '' 
    or entrada3.get() == '' or coloniaSelect.get() == ''
    or ciudadSelect.get() == '' or municipioSelect.get() == ''): 
        accion.configure(text="Faltan Campos")
    else:
        accion.configure(text="LISTO")
        mBox.showinfo('Datos Personales', entrada.get()+'\n'+entrada1.get()+'\n'+entrada2.get()+'\n'+entrada3.get()+'\n'+coloniaSelect.get()+'\n'+ciudadSelect.get()+'\n'+municipioSelect.get())        

def imprimir():

   Imprimir = tk.Toplevel(ventana)
   Imprimir.title("Imprimir")

def funcion_click2():
    
    if(objetivoTxt.get() == ''): 
        imprimirReg.configure(text="Faltan Campos")
    else:
        imprimirReg.configure(text="LISTO")

def funcion_click3():
   
        imprimirReg.configure(text="LISTO")        
   
def funcion_msg():
	mBox.showinfo('Mensaje de python en una caja de texto', 'Fue creada el día Miercoles 19 de Febrero 2019 por el alumno Alan Daniel Gaona Villa')


#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------


#------ Ventana FORMULARIO
ventana = tk.Tk()
ventana.title("Sistema de Registro")
ventana.geometry("320x450")
ventana.resizable(0,0)

#------ Menu
menubar = Menu(ventana)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label= "Imprimir", command = imprimir)
filemenu.add_command(label = "Salir", command = ventana.quit)
menubar.add_cascade(label = "Sistema", menu = filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "Acerca de", command = funcion_msg)
menubar.add_cascade(label = "Ayuda", menu = editmenu)


ventana.config(menu = menubar)


#------ Pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand='yes')
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='Datos Personales')
notebook.add(frame2, text='Preferencias')

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------


#------- TITULO
ttk.Label(frame1, text="Sistema Escalar", font = ("Agency FB", 10)).grid(column=10,row=0)
ttk.Label(frame1, text="Captura de Alumnos", font = ("Agency FB", 10)).place(x=10,y=15)


#------- TextBox Nombre
ttk.Label(frame1, text="Nombre:").place(x=30,y=50)
nombre = tk.StringVar()
entrada = ttk.Entry(frame1, width = 12, textvariable=nombre)
entrada.place(x=150,y=50)

#------- TextBox ApellidoP
ttk.Label(frame1, text="Apellido Paterno:").place(x=30,y=90)
nombre1 = tk.StringVar()
entrada1 = ttk.Entry(frame1, width = 12, textvariable=nombre1)
entrada1.place(x=150,y=90)

#------- TextBox ApellidoM
ttk.Label(frame1, text="Apellido Materno:").place(x=30,y=130)
nombre2 = tk.StringVar()
entrada2 = ttk.Entry(frame1, width = 12, textvariable=nombre2)
entrada2.place(x=150,y=130)

#------- TextBox Dirección
ttk.Label(frame1, text="Dirección:").place(x=30,y=170)
direccion = tk.StringVar()
entrada3 = ttk.Entry(frame1, width = 12, textvariable=direccion)
entrada3.place(x=150,y=170)

#------- TextBox Colonia
ttk.Label(frame1, text="Colonia:").place(x=30,y=210)
colonia = tk.StringVar()
coloniaSelect = ttk.Combobox(frame1, width=10, textvariable=colonia)
coloniaSelect['values'] = ("José María Izazaga", "Ejidal Tres Puentes", "Manzanito")
coloniaSelect.place(x=150,y=210)
#------- TextBox Ciudad
ttk.Label(frame1, text="Ciudad:").place(x=30,y=250)
ciudad = tk.StringVar()
ciudadSelect = ttk.Combobox(frame1, width=10, textvariable=ciudad)	
ciudadSelect['values'] = ("Morelia", "Apatzingan", "Hidalgo")
ciudadSelect.place(x=150,y=250)

#------- TextBox Municipio
ttk.Label(frame1, text="Municipio:").place(x=30,y=290)
municipio = tk.StringVar()
municipioSelect = ttk.Combobox(frame1, width=10, textvariable=municipio)
municipioSelect['values'] = ("Morelia", "Apatzingan", "Hidalgo")
municipioSelect.place(x=150,y=290)

#------- Boton REGISTRAR
accion = ttk.Button(frame1, text="Registrar", command = funcion_click)
accion.place(x=200,y=350)


#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------


#------ CheckButtons
ttk.Label(frame2, text= "Pasatiempos").place(x = 10, y = 10)
opcion = tk.IntVar()
aux = opcion.get()
check = tk.Checkbutton(frame2, text = "ejemplo1", variable = opcion)
check.deselect()
check.place(x=10,y=40)

opcion = tk.IntVar()
check = tk.Checkbutton(frame2, text = "ejemplo1", variable = opcion)
check.deselect()
check.place(x=120,y=40)

opcion = tk.IntVar()
check = tk.Checkbutton(frame2, text = "ejemplo1", variable = opcion)
check.deselect()
check.place(x=225,y=40)

#------- RadioButtons
ttk.Label(frame2, text= "Estado").place(x = 10, y = 70)
opcion = tk.IntVar()
aux2 = opcion.get()  
radio1 = tk.Radiobutton(frame2, text= "Soltero", variable= opcion, value=1)
radio1.place(x=10,y=100)
radio2 = tk.Radiobutton(frame2, text= "Viudo", variable= opcion, value=2)
radio2.place(x=120,y=100)
radio3 = tk.Radiobutton(frame2, text= "Casado", variable= opcion, value=3)
radio3.place(x=225,y=100)

#------- TextBox
ttk.Label(frame2, text = "Objetivo de la vida").place(x = 10, y = 150)
objetivoLargo = tk.StringVar()
objetivoTxt = tk.Entry(frame2, textvariable = objetivoLargo, width = 20)
objetivoTxt.place(x = 10, y = 170)

#------- Boton Imprimir
imprimirReg = tk.Button(frame2, text = "Imprimir Datos", command = funcion_click2)
imprimirReg.place(x = 180, y = 161)


ventana.mainloop()