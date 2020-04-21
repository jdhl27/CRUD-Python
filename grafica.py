#-------------------------------------------------------------------------------
# Name:        grafica
#
# Author:      Juan David Hdez
#
# Proyecto:    CRUD con interfaz Tkinter
# Created:     14/10/2019
# Copyright:   (c) Juan 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure



from funciones import *
from tkinter import messagebox
from tkinter.tix import *
from matplotlib import pyplot




cont=1                                                                          ## Variable para incrementar código automaticamente

objListas = ListaLigada()

## -------------------------------FUNCIONES-------------------------------------

def guardar():

    global cont
    codigo = cont
    nombre = txtNombre.get()
    edad = txtEdad.get()

    if(nombre != "" and edad!=""):
        if (edad.isnumeric()):
            objListas.agregarAlFinal(codigo, nombre, edad)                          ## Asignando datos a la lista

            txtNombre.delete(0, 'end')                                              ## Vaciando campos
            txtEdad.delete(0, 'end')
            txtNombre.focus()                                                       ## Enfocando cursor en input especifico
            cont +=1

            txtCodigo.config(state='normal')                                        ## Hablitando campo de texto

            edadPromedio = objListas.edadPromedio()

            lblTituloEdad = Label(window, text="EDAD PROMEDIO: ",                   ## Creando label Titulo Edad promedio
             font=("Bahnschrift Light Condensed", 18),bg="#151f29", fg="#fff71d")
            lblTituloEdad.place(x=140, y=525)

            lblEdadPromedio.config(text=edadPromedio)


            lblDatos.config(state='normal')                                         ## Hablitando labels
            lblCodigoDatos.config(state='normal')
            lblNombreDatos.config(state='normal')
            lblEdadDatos.config(state='normal')

            btnConsultar.config(state='normal', cursor="hand2")                     ## Hablitando botones
            btnModificar.config(state='normal', cursor="hand2")
            btnEliminar.config(state='normal', cursor="hand2")


            arr = objListas.listar()
            item = Text(window, width=40,height=10,bg="#0b2239",                    ## Creando Table de datos
                    font=("Bahnschrift Light Condensed", 13), fg="white")
            item.place(x=40, y=310)
            for i in range(len(arr)):
                item.insert(INSERT, "            " + str(arr[i][0]) + "	                     " + str(arr[i][1]) + "                          " + str(arr[i][2]) + "\n")
                item.insert(INSERT, "_______________________________________________________")
            messagebox.showinfo('EXITO', 'Registro Guardado')                       ## Mensaje de exito

            x1 = []
            y1 = []
            for i in range(len(arr)):
                x1.append("("+ str(arr[i][0]) + ")")
                y1.append(int(arr[i][2]))

            pyplot.bar(x1, y1, label='Edades', width=0.5, color='orange')
            pyplot.title("")
            pyplot.ylabel("Edad")
            pyplot.xlabel("Código")
            pyplot.show()
        else:
            messagebox.showerror('ERROR', 'Edad no es correcta')
            txtEdad.delete(0, 'end')
            txtEdad.focus()

    else:
        messagebox.showerror('ERROR', 'Llene los campos')
        if txtCodigo.get() == "":
            txtCodigo.focus()
        elif txtNombre.get() == "":
            txtNombre.focus()
        elif txtEdad.get() == "":
            txtEdad.focus()


def consultar():
    codigo = txtCodigo.get()
    if (codigo != ""):

        txtCodigo.delete(0,'end')
        txtNombre.delete(0,'end')
        txtEdad.delete(0,'end')
        codigo = int(codigo)
        sw = objListas.consultar(codigo)
        if (sw!=False):
            txtCodigo.insert(0, codigo)
            txtNombre.insert(0, sw[0])
            txtEdad.insert(0, sw[1])
        else:
            txtCodigo.insert(0, codigo)
            messagebox.showerror("Error", "El usuario no existe.",icon="warning")

    else:
        messagebox.showerror("Error", "Introduzca el código a consultar.",icon="error")
        txtCodigo.focus()


def modificar():
    codigo = txtCodigo.get()
    nombre = txtNombre.get()
    edad = txtEdad.get()
    if (codigo != "" and nombre != "" and edad!=""):
        if (edad.isnumeric()):
            codigo = int(codigo)
            sw = objListas.modificar(codigo,nombre,edad)
            if (sw!=False):
                edadPromedio = objListas.edadPromedio()

                lblTituloEdad = Label(window, text="EDAD PROMEDIO: ",               ## Creando label Titulo Edad promedio
                    font=("Bahnschrift Light Condensed", 18),bg="#151f29",
                    fg="#fff71d")
                lblTituloEdad.place(x=140, y=525)

                lblEdadPromedio.config(text=edadPromedio)

                arr = objListas.listar()
                item = Text(window, width=40,height=10,bg="#0b2239",                ## Creando Table de datos
                    font=("Bahnschrift Light Condensed", 13), fg="white")
                item.place(x=40, y=310)
                for i in range(len(arr)):
                    item.insert(INSERT, "            " + str(arr[i][0]) + "	                     " + str(arr[i][1]) + "                          " + str(arr[i][2]) + "\n")
                    item.insert(INSERT, "_______________________________________________________")

                messagebox.showinfo("Información","Usuario modificado.",icon="info")
                x1 = []
                y1 = []
                for i in range(len(arr)):
                    x1.append("(" + str(arr[i][0]) + ")")
                    y1.append(int(arr[i][2]))

                pyplot.bar(x1, y1, label='Edades', width=0.5, color='orange')
                pyplot.title("")
                pyplot.ylabel("Edad")
                pyplot.xlabel("Código")
                pyplot.show()
            else:
                txtCodigo.insert(0, codigo)
                messagebox.showerror("Error", "El usuario no existe.",icon="warning")
        else:
            messagebox.showerror('ERROR', 'Edad no es correcta')
            txtEdad.delete(0, 'end')
            txtEdad.focus()
    else:
        messagebox.showerror("Error", "Complete todos los campos.",icon="error");
        if txtCodigo.get() == "":
            txtCodigo.focus()
        elif txtNombre.get() == "":
            txtNombre.focus()
        elif txtEdad.get() == "":
            txtEdad.focus()



def eliminar():
    codigo = txtCodigo.get()
    if len(codigo) != 0:
        codigo = int(codigo)
        sw = objListas.eliminar(codigo)                                         ## Retorna un boleano si lo eliminó o no
        if (sw):

            edadPromedio = objListas.edadPromedio()

            lblTituloEdad = Label(window, text="EDAD PROMEDIO: ",               ## Creando label Titulo Edad promedio
                font=("Bahnschrift Light Condensed", 18),bg="#151f29",
                fg="#fff71d")
            lblTituloEdad.place(x=140, y=525)


            lblEdadPromedio.config(text=edadPromedio)

            arr = objListas.listar()
            item = Text(window, width=40,height=10,bg="#0b2239",                ## Creando Table de datos
                font=("Bahnschrift Light Condensed", 13), fg="white")
            item.place(x=40, y=310)
            for i in range(len(arr)):
                item.insert(INSERT, "            " + str(arr[i][0]) + "	                     " + str(arr[i][1]) + "                          " + str(arr[i][2]) + "\n")
                item.insert(INSERT, "_______________________________________________________")

            messagebox.showinfo("Información","Usuario borrado.",icon="info")

            x1 = []
            y1 = []
            for i in range(len(arr)):
                x1.append("("+ str(arr[i][0]) + ")")
                y1.append(int(arr[i][2]))

            pyplot.bar(x1, y1, label='Edades', width=0.5, color='orange')
            pyplot.title("")
            pyplot.ylabel("Edad")
            pyplot.xlabel("Código")
            pyplot.show()


            txtCodigo.delete(0, 'end')
            txtNombre.delete(0, 'end')
            txtEdad.delete(0, 'end')
            txtCodigo.focus()
        else:
            messagebox.showerror("Error", "El usuario no existe.",icon="warning")
    else:
        messagebox.showerror("Error", "Introduzca el código del usuario a eliminar.",icon="error")
        txtCodigo.focus()



##-----------------------------GRAFICA------------------------------------------


window = Tk()
window.tk.call('wm', 'resizable', window._w, False, False)
window.iconbitmap("search.ico")
window.title("Formulario")
window.configure(background="#151f29")
window.geometry('370x570+350+80') ##(ancho x altura + EjeX + EjeY)



lblTitulo = Label(window, text="FORMULARIO", font=("Bahnschrift SemiBold Condensed", 40),  fg="#50e6ff",bg="#151f29")
lblTitulo.grid(row=0, column=1)

## CODIGO(lbl, txt)
lblCodigo = Label(window, text="Codigo:" ,font=("Bahnschrift Light Condensed", 18), fg="#ff9349",bg="#151f29")
lblCodigo.grid(row=1, column=0)

txtCodigo = Entry(window,width=25, bg="#0b2239",borderwidth = 1, fg="white",font=("Bahnschrift Light Condensed", 13),state='disable')
txtCodigo.grid(row=1, column=1)

## NOMBRE(lbl, txt)
lblNombre = Label(window, text="Nombre:", font=("Bahnschrift Light Condensed", 18), fg="#ff9349",bg="#151f29",anchor="center")
lblNombre.grid(row=2, column=0,sticky="NW")

txtNombre = Entry(window,width=25,bg="#0b2239",borderwidth = 1,fg="white", font=("Bahnschrift Light Condensed", 13))
txtNombre.grid(row=2, column=1)
txtNombre.focus()


## EDAD(lbl, txt)
lblEdad = Label(window, text="Edad:", font=("Bahnschrift Light Condensed", 18), fg="#ff9349",bg="#151f29")
lblEdad.grid(row=3, column=0)

txtEdad = Entry(window,width=25,bg="#0b2239",borderwidth = 1,fg="white",font=("Bahnschrift Light Condensed", 13))
txtEdad.grid(row=3, column=1)

## ESPACIO
lblEspacio = Label(window, text="", font=("Bahnschrift Light Condensed", 18),bg="#151f29")
lblEspacio.grid(row=4, column=0)

## ESPACIO
lblEspacio = Label(window, text="", font=("Bahnschrift Light Condensed", 18),bg="#151f29")
lblEspacio.grid(row=5, column=0)

## BOTON GUARDAR
btnGuardar = Button(window, text="Guardar", bg="#42c146", fg="white", cursor="hand2", relief=RIDGE ,command=guardar)
btnGuardar.place(x=30, y=195)


## BOTON CONSULTAR,
btnConsultar= Button(window, text="Consultar", bg="#151f29", fg="white",relief=RIDGE, state='disable', command=consultar)
btnConsultar.place(x=100, y=195)


## BOTON MODIFICAR
btnModificar = Button(window, text="Modificar", bg="#151f29", fg="white",relief=RIDGE, state='disable', command=modificar)
btnModificar.place(x=180, y=195)


## BOTON ELIMINAR
btnEliminar= Button(window, text="Eliminar", bg="#e3220f", fg="white", relief=RIDGE,command=eliminar, state='disable')
btnEliminar.place(x=260, y=195)


## TITULO DATOS
lblDatos = Label(window, text="DATOS", font=("Bahnschrift Light Condensed", 18),fg="#50e6ff",bg="#151f29", state='disable')
lblDatos.grid(row=6, column=1)

## TITULO CODIGO DATOS
lblCodigoDatos = Label(window, text="CÓDIGO", font=("Bahnschrift Light Condensed", 15),fg="#ff9349",bg="#151f29", state='disable')
lblCodigoDatos.place(x=60, y=278)

## TITULO NOMBRE DATOS
lblNombreDatos = Label(window, text="NOMBRE", font=("Bahnschrift Light Condensed", 15),fg="#ff9349",bg="#151f29", state='disable')
lblNombreDatos.place(x=156, y=278)

## TITULO EDAD DATOS
lblEdadDatos = Label(window, text="EDAD", font=("Bahnschrift Light Condensed", 15),fg="#ff9349",bg="#151f29", state='disable')
lblEdadDatos.place(x=250, y=278)

## EDAD PROMEDIO
lblEdadPromedio = Label(window, text="",font=("Bahnschrift Light Condensed", 18),bg="#151f29",fg="white")
lblEdadPromedio.place(x=285, y=525)



## MOSTRAR LA VENTANA

window.mainloop()