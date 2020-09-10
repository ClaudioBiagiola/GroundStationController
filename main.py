import tkinter
from tkinter import ttk, StringVar, PhotoImage, Image, messagebox,Tk
from tkinter import *
import getpass
# defino variables
import self as sel
# abro ventana

ventana=tkinter.Tk()
vp=Frame(ventana)
vp.grid(column= 0,row=0,padx=(10,10),pady=(10,10))
vp.grid_columnconfigure(0,weight=1)
vp.grid_rowconfigure(0,weight=1)
#vp.config(bg="grey")
#ventana.iconbitmap("logo.ico")
#ventana de inicio
#messagebox.showinfo(message="Espere, iniciando sistemas", title="Iniciando")
ventana.geometry("1080x720")

# titulo
ventana.title("Ground Stations Controller")
Titulo = tkinter.Label(vp, text="Ground Stations Controller", fg="black", font=("Arial", "24"))
Titulo.grid(row=0, column=1,columnspan=4,padx=(150,20),pady=(20,20))#centrar titulo

#texto
ingresar= tkinter.Label(vp,text="Ingresar Datos",fg="black", font=("Arial", "11"))
ingresar.grid(row=1, column=0,padx=(50,5),pady=(50,5),ipadx=0)

Obj= tkinter.Label(vp,text="Objetivo",fg="black", font=("Arial", "11"))
Obj.grid(row=2, column=0,padx=(50,5),pady=(20,5),sticky=W)

#datoobj=tkinter.StringVar()
Objetivo= ttk.Combobox(vp,width=30)
Objetivo.grid(row=2, column=1)
Objetivo["values"] = ["Sol", "Jupiter", "Centro Galaxtico", "Tu Vieja"]
Objetivo.bind("Selecionar objetivo")
value = Objetivo.get()
numero = Objetivo.current()
if numero >0: print("el dato"+value)


Horainin= tkinter.Label(vp,text="Hora de inicio",fg="black", font=("Arial", "11"))
Horainin.grid(row=3, column=0,padx=(50,5),pady=(20,10),sticky=W)

Horadeinin= Entry(vp,width=30)
Horadeinin.grid(row=3, column=1)

aclaracionhorainin= tkinter.Label(vp,text="ejemplo -----",fg="black", font=("Arial", "11"))
aclaracionhorainin.grid(row=4, column=1,padx=(5,5),pady=(5,5),sticky=W)

Horafin= tkinter.Label(vp,text="Hora de finalizacion",fg="black", font=("Arial", "11"))
Horafin.grid(row=5, column=0,padx=(50,5),pady=(20,10),sticky=W)

Horadefin= Entry(vp,width=30)
Horadefin.grid(row=5, column=1)

aclaracionhorafin= tkinter.Label(vp,text="ejemplo -----",fg="black", font=("Arial", "11"))
aclaracionhorafin.grid(row=6, column=1,padx=(5,5),pady=(5,5),sticky=W)

bntcali= Button(vp,text="Calibrar")
bntcali.grid(row=7,column=1,padx=(5,5),pady=(50,5),sticky=E)

bntinin= Button(vp,text="iniciar")
bntinin.grid(row=7,column=1,padx=(5,5),pady=(50,5))


bntfin= Button(vp,text="finalizar")
bntfin.grid(row=7,column=1,padx=(5,5),pady=(50,5),sticky=W)



# right text
estadoactual= tkinter.Label(vp,text="Estado actual",fg="black", font=("Arial", "11"))
estadoactual.grid(row=1, column=3,padx=(20,5),pady=(50,5))

Siguiendo= tkinter.Label(vp,text="Siguiento",fg="black", font=("Arial", "11"))
Siguiendo.grid(row=2, column=3,padx=(25,5),pady=(5,5))
datosiguiendo= Entry(vp,width=20)
datosiguiendo.grid(row=2, column=5,columnspan=2) #para insertar dato datossiguiendo.insert(posicion, valor)

Desde= tkinter.Label(vp,text="Desde",fg="black", font=("Arial", "11"))
Desde.grid(row=3, column=3,padx=(25,5),pady=(5,5))
datosdesde= Entry(vp,width=20)
datosdesde.grid(row=3, column=5,columnspan=2) #para insertar dato datossiguiendo.insert(posicion, valor)

Hasta= tkinter.Label(vp,text="Hasta",fg="black", font=("Arial", "11"))
Hasta.grid(row=4, column=3,padx=(25,5),pady=(5,5))
datoshasta= Entry(vp,width=20)
datoshasta.grid(row=4, column=5,columnspan=2) #para insertar dato datossiguiendo.insert(posicion, valor)

Azimut= tkinter.Label(vp,text="Azimut:",fg="black", font=("Arial", "11"))
Azimut.grid(row=5, column=3,padx=(30,5),pady=(5,5))
datosazimut= Entry(vp,width=10)
datosazimut.grid(row=5, column=4) #para insertar dato datossiguiendo.insert(posicion, valor)

Elevacion= tkinter.Label(vp,text="Elevacion:",fg="black", font=("Arial", "11"))
Elevacion.grid(row=5, column=5,padx=(5,5),pady=(5,5),sticky=W)
datosazimut= Entry(vp,width=10)
datosazimut.grid(row=5, column=6) #para insertar dato datossiguiendo.insert(posicion, valor)



# logo
logo = tkinter.PhotoImage(file="logo2.png")
log = tkinter.Label(ventana,image=logo)
log.grid(row=0, column=3,sticky=NE,padx=(5,0),pady=(25,5))

#blog
#inivert = ttk.PanedWindow(vp, orient=VERTICAL)
#inivert.grid(row=1, column=0,columnspan=3,rowspan=5, sticky="nsew")
#inihoriz = ttk.PanedWindow(inivert, orient=HORIZONTAL)
##inivert.add(inihoriz)
#form_frame = ttk.Labelframe(inihoriz,)
#form_frame.columnconfigure(1, weight=1)
#inihoriz.add(form_frame, weight=1)

blogvert = ttk.PanedWindow(vp, orient=VERTICAL)
blogvert.grid(row=6, column=3,columnspan=3,rowspan=3, sticky="nsew",pady=(5,50))
bloghoriz = ttk.PanedWindow(blogvert, orient=HORIZONTAL)
blogvert.add(bloghoriz)
console_frame = ttk.Labelframe(bloghoriz, text="Consola")
console_frame.columnconfigure(2, weight=1)
console_frame.rowconfigure(1, weight=5)
bloghoriz.add(console_frame, weight=1)

Creditos= tkinter.Label(vp,text="Creditos",fg="black", font=("Arial", "11"))
Creditos.grid(row=6, column=3,padx=(10,5),pady=(25,5),sticky=W)
#mensaje = tkinter.StringVar()
#mensaje.Label(vp, text='Message:').grid(column=, row=1, sticky=W)
#mensaje.Entry(vp, textvariable=mensaje, width=25).grid(column=1, row=1, sticky=(W, E))


#Creditos
Creditos= tkinter.Label(vp,text="Creditos",fg="black", font=("Arial", "11"))
Creditos.grid(row=8, column=0,padx=(20,5),pady=(150,5),sticky=W)


#bntcali= Button(vp,text="Calibrar")
#bntcali.grid(row=4,column=0)

#bntinin= Button(vp,text="iniciar")
#bntinin.grid(row=4,column=3)


#bntfin= Button(vp,text="finalizar")
#bntfin.grid(row=4,column=5)

#fecha_init= Entry(vp,width=10)
#fecha_init.grid(row=3, column=3)

#v = "hola"

#etiqueta2 = tkinter.Label(vp, text= v, fg="black", font=("Arial", "16"))
#etiqueta2.grid(row=3, column=6)

ventana.mainloop()
