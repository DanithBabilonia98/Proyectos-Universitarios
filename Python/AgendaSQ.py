from tkinter import *
from tkinter import messagebox
import sqlite3
lista=[]
db=sqlite3.connect("agenda.db")
cursor=db.cursor()
try:
    cursor.execute('''
CREATE TABLE IF NOT EXISTS datos(
nombre TEXT NOT NULL,
apellidoP TEXT NOT NULL ,
apellidoM TEXT NOT NULL,
correo TEXT NOT NULL,
telefono TEXT NOT NULL)
''')
except sqlite3.OperationalError:
    print("Tabla ya existe")
else:
    print("Tabla creada correctamente")
db.commit()
db.close()

def guardar():
    n = nombre.get()
    ap = app.get()
    am = apm.get()
    c = correo.get()
    t = telefono.get()
    conexion=sqlite3.connect("agenda.db")
    with conexion:
        cursor=conexion.cursor()
        cursor.execute("INSERT INTO datos (nombre, apellidoP, apellidoM, correo, telefono) VALUES(?,?,?,?,?)",( n,ap,am,c,t))
        mesaje="Creado correctamente!"
        messagebox.showinfo("*********",mesaje)
        conexion.commit()

def Mostrar():
    conexion=sqlite3.connect("agenda.db")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM datos")
    for x in cursor.fetchall():
        messagebox.showinfo("DATOS", x)      

def eliminar():
    eliminado = conteliminar.get()
    conexion=sqlite3.connect("agenda.db")
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM datos WHERE telefono = ?",(eliminado,))
    messagebox.showinfo("Eliminar","Elemento eliminado "+eliminado)
    conexion.commit()


def consultar():
    r = Text(ventana, width=80, height=15)
    lista.sort()
    valores = []
    r.insert(INSERT, "Nombre :\tApellidos P :\t\tApellido M :\t\tTeléfono :\t\tCorreo :\n")
    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[3])
        r.insert(INSERT, arreglo[0]+"\t"+arreglo[1]+"\t\t"+
        arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
    r.place(x=20,y=230)
    spinTelefono = Spinbox(ventana, value=(valores),textvariable=conteliminar).place(x=450,
    y=50)
    if lista ==[]:
            spinTelefono = Spinbox(ventana, value=(valores)).place(x=450,y=50)
    r.config(state=DISABLED)


def iniciarArchivo():
    archivo = open("ag.txt","a")
    archivo.close()


def cargar():
    archivo = open("ag.txt","r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1]=='\n':
                linea = linea[:-1]
        lista.append(linea)
        linea = archivo.readline()
    archivo.close()


def escribirContacto():
    archivo = open("ag.txt","w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close()


ventana= Tk()
nombre= StringVar()
app= StringVar()
apm=StringVar()
correo=StringVar()
telefono= StringVar()
conteliminar= StringVar()
colorFondo="#31B489"
colorLetra= "#FFF"
ventana.title('Agenda ')
ventana.geometry("700x500")
ventana.configure(background= colorFondo)

etiquetaTitulo= Label (ventana, text="Agenda " , font=("Helvetica", 14), 
bg= colorFondo, fg=colorLetra).place(x=270, y=10)
etiquetaN= Label(ventana, text="Nombre :", bg=colorFondo,
                 fg=colorLetra).place(x=50,y=50)
cajaN= Entry(ventana, textvariable=nombre).place(x=150, y=50)
etiquetaApp= Label(ventana, text="Apellido Paterno :", bg=colorFondo,
                 fg=colorLetra).place(x=50,y=80)
cajaApp= Entry(ventana,textvariable=app).place(x=150, y=80)
etiquetaApm= Label(ventana,text="Apellido Materno :", bg=colorFondo,
                 fg=colorLetra).place(x=50,y=110)
cajaApm= Entry (ventana,textvariable=apm).place(x=150,y=110)
etiquetaT= Label(ventana,text="Telefono :", bg=colorFondo,
                 fg=colorLetra).place(x=50,y=140)
cajaT= Entry(ventana,textvariable=telefono).place(x=150,y=140)
etiquetaC= Label (ventana, text="Correo :", bg=colorFondo,
                 fg=colorLetra).place(x=50, y=170)
cajaC= Entry(ventana,textvariable=correo).place(x=150,y=170)
etiquetaEliminar= Label(ventana, text="Teléfono", bg=colorFondo,
                 fg=colorLetra).place(x=370, y=50)
spinTelefono= Spinbox(ventana, textvariable=conteliminar).place(x=450, y=50)
botoGuardar= Button(ventana,text="Guardar", command=guardar, bg="#008",
                 fg="yellow").place(x=180, y=200)
botoEliminar=Button(ventana,text="Eliminar", command=eliminar, bg="#008",
                 fg="yellow").place(x=490, y=80)
botoMostrar=Button(ventana,text="Mostrar",command=Mostrar, bg="#008",
                 fg="Yellow").place(x=420,y=80)

mainloop()
