# LIBRERIAS
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

# VARIABLES GLOBALES
caracter = ""
raiz = Tk()
raiz.resizable(False, False)
i = 0

# ESTRUCTURA DE CONSTRUCCION DE PESTAÑA "TAREAS Y "NOTAS"
pestaña = ttk.Notebook(raiz)
pestaña.pack()
tareas = ttk.Frame(pestaña)
notas = ttk.Frame(pestaña)
pestaña.add(tareas, text='             LISTA DE TAREAS                  ')
pestaña.add(notas, text='                  NOTAS                       ')

# VARIABLES DE DATOS
accion_1 = StringVar()
accion_2 = StringVar()
accion_3 = StringVar()
texto_principal = StringVar()


# FUNCION DE CREACION DE PESTAÑAS DE AYUDA "ARCHIVO" "EDITAR" "HERRAMIENTAS" "AYUDA"
def pestañas():
    barramenu = Menu(raiz)  #
    raiz.config(menu=barramenu)
    archivomenu = Menu(barramenu, tearoff=0)
    archivomenu.add_command(label="Nuevo")
    archivomenu.add_command(label="Guardar")
    archivomenu.add_command(label="Guardar como")
    archivomenu.add_separator()
    archivomenu.add_command(label="Cerrar", command=cerrardocumento)
    archivomenu.add_command(label="Salir", command=saliraplicacion)

    archivoeditar = Menu(barramenu, tearoff=0)
    archivoeditar.add_command(label="Copiar")
    archivoeditar.add_command(label="Cortar")
    archivoeditar.add_command(label="Pegar")

    archivoherramientas = Menu(barramenu)

    archivoayuda = Menu(barramenu, tearoff=0)
    archivoayuda.add_command(label="Licencia", command=avisolicencia)
    archivoayuda.add_command(label="Acerca de...", command=infoadicional)

    barramenu.add_cascade(label="Archivo", menu=archivomenu)
    barramenu.add_cascade(label="Editar", menu=archivoeditar)
    barramenu.add_cascade(label="Herramientas", menu=archivoherramientas)
    barramenu.add_cascade(label="Ayuda", menu=archivoayuda)

    botonabrir = Button(tareas, text="Abrir fichero", command=abrefichero)
    botonabrir.grid(row=3, column=3)


# FUNCION PARA CREAR LAS ACCIONES A REALIZAR "ACCION-1" "ACCION-2" "ACCION-3"
def accion():
    global caracter
    global i
    global texto_principal
    i += 1
    if i == 1:
        micuadrotexto_1 = Entry(tareas, font=("Arial", 12), textvariable=accion_1)
        micuadrotexto_1.grid(row=2, column=0, padx=10, pady=10)
        micuadrotexto_1.config(justify="center")
        accion_1.set(texto_principal.get() + caracter)
        botonborrar_1 = Button(tareas, text="X", font=(12), width=3, height=1, command=lambda: borrar("1"))
        botonborrar_1.grid(row=2, column=1)
        texto_principal.set(caracter)
        return (micuadrotexto_1)
    if i == 2:
        micuadrotexto_2 = Entry(tareas, font=("Arial", 12), textvariable=accion_2)
        micuadrotexto_2.grid(row=3, column=0, padx=10, pady=10)
        micuadrotexto_2.config(justify="center")
        accion_2.set(texto_principal.get() + caracter)
        botonborrar_2 = Button(tareas, text="X", font=(12), width=3, height=1, command=lambda: borrar("2"))
        botonborrar_2.grid(row=3, column=1)
        texto_principal.set(caracter)
    if i == 3 and texto_principal != "":
        micuadrotexto_3 = Entry(tareas, font=("Arial", 12), textvariable=accion_3)
        micuadrotexto_3.grid(row=4, column=0, padx=10, pady=10)
        micuadrotexto_3.config(justify="center")
        accion_3.set(texto_principal.get() + caracter)
        botonborrar_3 = Button(tareas, text="X", font=(12), width=3, height=1, command=lambda: borrar("3"))
        botonborrar_3.grid(row=4, column=1)
        texto_principal.set(caracter)
    if i > 4:
        i = 3
        texto_principal.set(caracter)


# FUNCION PARA BORRAR DATOS POR MEDIO DEL BOTON
def borrar(num1):
    """
    borra el texto de la acticvidad anotada.
    : param string num1 : posicion del boton.
    :return ""

    """
    global caracter
    global i

    if num1 == "1":
        i = 0
        valor = messagebox.askquestion("SALIR", "¿Esta seguro que deseas eliminar?")
        if valor == "yes":
            accion_1.set("")

    if num1 == "2":
        i = 1
        valor = messagebox.askquestion("SALIR", "¿Esta seguro que deseas eliminar?")
        if valor == "yes":
            accion_2.set("")

    if num1 == "3":
        i = 2
        valor = messagebox.askquestion("SALIR", "¿Esta seguro que deseas eliminar?")
        if valor == "yes":
            accion_3.set("")


# FUNCION PARA AGREGAR INFORMACION EN LA PESTAÑA "AYUDA" "ACERCA DE..."
def infoadicional():
    messagebox.showinfo("TODOLIST", "Universidad nacional de Colombia")


# FUNCION PARA AGREGAR INFORMACION EN LA PESTAÑA "AYUDA" "LICENCIA"
def avisolicencia():
    messagebox.showwarning("LICENCIA", "Producto de bajo licencia no se que")


# FUNCION PARA SALIR DE LA APLICACION EN LA PESTAÑA "ARCHIVO" "SALIR"
def saliraplicacion():
    valor = messagebox.askokcancel("SALIR", "¿Deseas salir de la aplicación?")
    if valor == True:
        raiz.destroy()


# FUNCION PARA CERRAR EL DOCUMENTO EN LA PESTAÑA "ARCHIVO" "SALIR"
def cerrardocumento():
    valor = messagebox.askretrycancel("REINTENTAR", "No es posible cerrar, documento bloqueado")
    if valor == False:
        raiz.destroy()


# FUNCION PARA BUSCAR ARCHIVO EN EL BOTON "ABRIR FICHERO"
def abrefichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(
    ("Ficheros de Excel", ".jpg"), ("Ficheros de texto", ".docx"), ("Todos los ficheros", ".")))
    print(fichero)


# FUNCION PRINCIPAL
def main():
    pestañas()
    textocomentario = Entry(tareas, font=("Arial", 12), textvariable=texto_principal)
    textocomentario.grid(row=1, column=0, padx=5, pady=5)

    miLabel = Label(tareas, text="              TO DO LIST", font=("Caveat", 24))
    miLabel.grid(row=0, column=0, padx=5, pady=5, columnspan=3)

    botonenvio = Button(tareas, text="+", font=('Arial', 10), width=6, height=3, command=lambda: accion())
    botonenvio.grid(row=1, column=1)
    botonenvio.config(background="blue", fg="white")

    global k
    miLabel = Label(notas, text="          POST IT", font=("Caveat", 24))
    miLabel.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

    caja_texto = Text(notas, font=("Arial", 12), width=25, height=6)
    caja_texto.grid(padx=10, pady=10, row=1, column=0)

    botonenvio = Button(notas, text="+", font=('Arial', 10), width=6, height=3)
    botonenvio.grid(row=1, column=1)
    botonenvio.config(background="orange", fg="black")


main()
raiz.mainloop()