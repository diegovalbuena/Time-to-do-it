#libreras
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from bs4 import BeautifulSoup
from urllib.request import urlopen
from tkinter import filedialog
import webbrowser as wb

archivo_texto = open("Base de datos.txt", "a")
archivo_texto.close()

usuarios = {}
estado = ""

def menu_pantalla():
    """
    Crea la ventana principal donde funciona el login, en esta se realiza la creacion de las etiquetas y botones de esta ventana.
    :param none:
    :return: none
    """
    global pantalla
    #creacion ventana principal
    pantalla = Tk()
    pantalla.geometry("300x380")
    pantalla.title("Bienvenidos")
    pantalla.iconbitmap("ICOUNAL.ico")

    #insercion de imagen UNAL
    image = PhotoImage(file="GIFUNAL.gif")
    image = image.subsample(2,2)
    label = Label(image=image)
    label.pack()

    #creacion de labels
    Label(text="Acceso al sistema", bg="navy", fg="white", width="300", height="3", font=("Calibri",15)).pack()
    Label(text="").pack()
    Label(text="").pack()

    #creacion de botones
    Button(text="Iniciar sesion", height="3", width="30", command=inicio_sesion).pack()
    Button(text="Registrar", height="3", width="30", command=registrar).pack()

    pantalla.mainloop()


def inicio_sesion():
    """
    Abre otra ventana donde el usuario puede introducir sus datos e iniciar sesion.
    :param none:
    :return: none
    """
    global pantalla1
    global nombreusuario_verify
    global contrasenausuario_verify

    #creacion ventana
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de sesion")
    pantalla1.iconbitmap("ICOUNAL.ico")

    #label superior
    Label(pantalla1, text="Por favor ingrese su usuario y contraseña "
                          "\n a continuacion",
          bg="navy", fg="white", width="300", height="3", font=("Calibri",15)).pack()
    Label(pantalla1, text="").pack()

    #variables de las entradas
    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()

    # label y recuadro de entrada usuario
    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    # label y recuadro de entrada contraseña
    Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry = Entry(pantalla1, show ="*", textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    # creacion boton inicio sesion
    Button(pantalla1, text="Iniciar sesion", command=antiguo_usuario).pack()

def registrar():
    """
    Abre otra ventana donde el usuario puede introducir sus datos y crear un usuario nuevo.
    :param none:
    :return: none
    """
    global pantalla2
    global nombreusuario_entry
    global contrasena_entry

    # creacion ventana
    pantalla2 =Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("ICOUNAL.ico")

    #label superior
    Label(pantalla2, text="Por favor ingrese su usuario y contraseña "
                          "\n a continuacion, no ingresar usuario "
                          "\n o contraseña con espacio",
          bg="navy", fg="white", width="300", height="3", font=("Calibri",15)).pack()
    Label(pantalla2, text="").pack()

    # variables de las entradas
    nombreusuario_entry=StringVar()
    contrasena_entry=StringVar()

    # label y recuadro de entrada usuario
    Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry = Entry(pantalla2, textvariable=nombreusuario_entry)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    # label y recuadro de entrada usuario
    Label(pantalla2, text="Contraseña").pack()
    contrasena_entry = Entry(pantalla2, show ="*", textvariable=contrasena_entry)
    contrasena_entry.pack()
    Label(pantalla2).pack()

    #creacion boton registro
    Button(pantalla2, text="Registrar", command=nuevo_usuario).pack()
def nuevo_usuario():
    """
    llama el documento tipo .txt llamado "base de datos", en el cual se corrobora si la informacion ingresada ya se
    encuentra registrada, de lo contrario registrar dicha informacion y mostrara el aviso correspondiente.
    :param none:
    :return: none
    """
    global usuarios
    global nombreusuario_entry
    global contrasena_entry
    log = True

    #llamado del archivo y creacion del usuario
    crear_login = nombreusuario_entry.get()
    crear_contraseña = contrasena_entry.get()
    archivo_texto = open("Base de datos.txt", "r")
    for line in archivo_texto.readlines():
        line = str(line)
        line = line.split(' ')
        if crear_login in line[0] and len(line) != 2:
            messagebox.showinfo(message="Cuenta con dicho usuario ya existe", title="Aviso")
            log = False
    archivo_texto.close()
    if log == True:
        usuarios[crear_login] = crear_contraseña
        messagebox.showinfo(message="Usuario creado", title="Aviso")
        archivo_texto = open("Base de datos.txt", "a")
        archivo_texto.write("\n" + crear_login + " " + crear_contraseña)
        archivo_texto.close()
    pantalla2.destroy()

def antiguo_usuario():
    """
    Compara la informacion que suministra el usuario en las cacillas de inicio y las compara con el archivo del archivo
    "bases de datos", si estos coinsiden o si no muestra el aviso correspondiente.
    :param none:.
    :return: none
    """
    global usuarios
    global nombreusuario_verify
    global contrasenausuario_verify
    log = True

    #llamado del archivo y comparacion de informacion
    login = nombreusuario_verify.get()
    contraseña = contrasenausuario_verify.get()
    archivo_texto = open("Base de datos.txt","r")
    for line in archivo_texto.readlines():
        line = str(line)
        line = line.split(" ")
        if login in line[0] and contraseña in line[1]:
            messagebox.showinfo(message="Login correcto", title="Aviso")
            pantalla1.destroy()
            pantalla.destroy()
            ventana()
            log = False
    if log == True:
        messagebox.showinfo(message="Usuario no existe o contraseña incorrecta", title="Aviso")
        pantalla1.destroy()
    archivo_texto.close()

def ventana():
    """
    Genera la ventana princiapl del programa en la cual se posicionan todos los botones, recuadros de entrada
    y labels principales del manejo del
    apartado de tareas y del programa en general.
    :param none:
    :return: none
    """
    global fecha
    global nombre_archivo
    global ruta_archivo
    global datos_archivos
    fecha = ''
    nombre_archivo = ''
    ruta_archivo = ''
    datos_archivos = []

    #creacion ventana y pestañas
    raiz = Tk()
    raiz.title("TIME TO DO IT")
    raiz.geometry('780x450')
    raiz.resizable(False, False)
    menu(raiz)
    pestaña = ttk.Notebook(raiz)
    pestaña.pack()
    tareas = ttk.Frame(pestaña)
    notas = ttk.Frame(pestaña)
    pestaña.add(tareas, text='                      LISTA DE TAREAS                  ')
    pestaña.add(notas, text='                          LISTA DE NOTAS                       ')

    #labels de entradas
    label_etiqueta = Label(tareas, text= 'Etiqueta', font=("Arial", 12))
    label_etiqueta.place(x=5, y=0)
    label_tarea = Label(tareas, text='Tarea', font=("Arial", 12))
    label_tarea.place(x=160, y=0)
    label_fecha = Label(tareas, text='Fecha', font=("Arial", 12))
    label_fecha.place(x=480, y=0)
    label_archivo = Label(tareas, text='Archivo', font=("Arial", 12))
    label_archivo.place(x=650, y=0)

    #cajetines de entrada
    entrada_etiqueta = Entry(tareas, font=("Arial", 12), width='10')
    entrada_etiqueta.place(x=5, y=20)
    entrada_tarea = Entry(tareas, font=("Arial", 12), width='30')
    entrada_tarea.place(x=160, y=20)
    entrada_fecha = Button(tareas, text='Establecer fecha', command=lambda: obtener_fecha(), bg='grey70', fg= 'black')
    entrada_fecha.place(x=480, y=20)
    entrada_archivo = Button(tareas, text='Agregar archivo', command=lambda: agregar_archivo(), bg='gray70', fg= 'black')
    entrada_archivo.place(x=650, y=20)

    #listado de tareas
    lista_tareas = ttk.Treeview(tareas, columns=('#1', '#2', '#3'))
    lista_tareas.grid(padx=5, pady=100)

    lista_tareas.column("#0", width=120, minwidth=120)
    lista_tareas.heading('#0', text='Etiqueta')
    lista_tareas.column("#1", width=370, minwidth=370)
    lista_tareas.heading('#1', text='Tarea')
    lista_tareas.column("#2", width=120, minwidth=120)
    lista_tareas.heading('#2', text='Fecha')
    lista_tareas.column("#3", width=150, minwidth=150)
    lista_tareas.heading('#3', text='Archivo')

    #llamado funsion para la creacion listado de notas
    cuadro_notas(notas)

    #botones de control
    boton_entrada = Button(tareas, text='Añadir tarea', bg='lawngreen', fg='black',
                           command=lambda: entradas(entrada_etiqueta,
                                                    entrada_tarea,
                                                    lista_tareas,
                                                    orden_tareas.get()))
    boton_entrada.place(x=30, y=60)

    boton_eliminar = Button(tareas, text='Eliminar tarea(s) seleccionada(s)', bg='orangered', fg='black',
                            command=lambda: eliminar_tarea(lista_tareas))
    boton_eliminar.place(x=200, y=60)

    orden_tareas = ttk.Combobox(tareas, state="readonly")
    orden_tareas.set('Ordenar por:')
    orden_tareas.place(x=450, y=60)
    orden_tareas['values'] = ('Etiquetas', 'Fechas')

    # botones inferiores
    boton_corferias = Button(tareas, text='Programacion corferias 2021', bg='deepskyblue', fg='black', command=lambda: corferias())
    boton_corferias.place(x=500, y=360)
    boton_archivos= Button(tareas, text="Abrir Archivo", bg='sandy brown', fg='black', command=lambda: ver_archivo())
    boton_archivos.place(x=150, y=360)

    raiz.mainloop()

def menu(raiz):
    """
    Inserta un menu de opciones en cascada, el cual posee otros caracteres como en este caso la opcion de cerra el programa.
    :param tk[raiz]: funcion principal que contiene la ejecucion del programa.
    :return: none
    """
    barramenu = Menu(raiz)
    raiz.config(menu=barramenu)
    archivomenu = Menu(barramenu)
    barramenu.add_cascade(label='Menu', menu=archivomenu)
    archivomenu.add_command(label="Salir", command=lambda:saliraplicacion(raiz))

def saliraplicacion(raiz):
    """
    Contiene la opcion de cerrar el programa de forma segura..
    :param tk[raiz]: funcion principal que contiene la ejecucion del programa.
    :return: none
    """
    valor = messagebox.askokcancel("SALIR", "¿Deseas salir de la aplicación?")
    if valor == True:
        raiz.quit()

def obtener_fecha():
    """
    Genera la ventana que muestra el calendario para asi llamar a la opcion de generar la fecha seleccionada.
    :param none:
    :return: none
    """
    #creacion de ventana
    cal = Tk()
    cal.title("calendario")

    #creacion de calendario
    calendario = Calendar(cal, selectmode='day')
    calendario.pack(pady=20)

    #creaacion boton de envio info
    boton_de_envio = Button(cal, text='Establecer', command=lambda: dar_fecha(calendario, cal), bg='grey70')
    boton_de_envio.pack(pady=10)

def dar_fecha(calendario,cal):
    """
    Genera la fecha que el ususario seleccciona con el cursor.
    :param tkcalendar[calendario]: variable que contiene al calendario generado por la libreria tkcalentar
    :param tk[cal]: ventana del calendario
    :return: none
    """
    global fecha
    fecha = calendario.selection_get()
    cal.destroy()

def entradas(entrada_etiqueta, entrada_tarea, lista_tareas, modo_orden):
    """
    Realiza el procesamiento de los datos de entrada del apartado de tareas.
    :param entrada_etiqueta[string]: entrada del recuadro de la etiqueta
    :param entrada_tarea[string]: entrada del recuadro de la tarea
    :param lista_tareas[Treeview]: arbol que contiene laos valores de las tareas.
    :param modo_orden[string]: seleccion entre ordenamiento por fecha y etiqueta.
    :return: none
    """
    global datos_archivos
    global nombre_archivo
    global ruta_archivo

    #añade la informacion de la tarea
    if entrada_tarea.get() != '':
        lista_tareas.insert(parent='', index=END, text=entrada_etiqueta.get(),
                            values=(entrada_tarea.get(), fecha, nombre_archivo))
        if nombre_archivo != '':
            datos_archivos.append([nombre_archivo, ruta_archivo])
            nombre_archivo = ''
            ruta_archivo = ''

        #llama la funcion para ordenar las tareas
        lista, dicci = orden(lista_tareas, modo_orden)

        #elimina informacion de los recuadros de entrada
        entrada_etiqueta.delete(0, END)
        entrada_tarea.delete(0, END)

        #elimina tareas anteriores en la lista de tareas
        for elemento in lista_tareas.get_children():
            lista_tareas.delete(elemento)

        #re ingresa las tareas ya ordenadas
        for guia in lista:
            for datos in dicci[guia]:
                if modo_orden == 'Etiquetas':
                    lista_tareas.insert(parent='', index=END, text=guia,
                                        values=(datos[1], datos[2], datos[3]))
                else:
                    lista_tareas.insert(parent='', index=END, text=datos[0],
                                        values=(datos[1], guia, datos[3]))

def orden(lista_tareas, modo_orden='Fecha'):
    """
    Organiza las tareas del arbol de tareas.
    :param lista_tareas[Treeview]: arbol que contiene laos valores de las tareas.
    :param modo_orden[string]: seleccion entre ordenamiento por fecha y etiqueta.
    :return: lista
    :return: diccionario
    """
    lista = []
    diccionario = {}

    #obtiene la informacion de las tareas
    for elemento in lista_tareas.get_children():
        etiqueta_lista = lista_tareas.item(elemento, 'text')
        tarea_lista = lista_tareas.item(elemento, 'values')[0]
        fecha_lista = lista_tareas.item(elemento, 'values')[1]
        archivo_lista = lista_tareas.item(elemento, 'values')[2]

        #organiza las tareas deacuerdo al orden seleccionado
        if modo_orden == 'Etiquetas':
            if not(etiqueta_lista in  diccionario):
                lista.append(etiqueta_lista)
                diccionario[etiqueta_lista] = [[etiqueta_lista,tarea_lista, fecha_lista, archivo_lista]]
            else:
                diccionario[etiqueta_lista].append([etiqueta_lista, tarea_lista, fecha_lista, archivo_lista])
        else:
            if not(fecha_lista in  diccionario):
                lista.append(fecha_lista)
                diccionario[fecha_lista] = [[etiqueta_lista, tarea_lista, fecha_lista, archivo_lista]]
            else:
                diccionario[fecha_lista].append([etiqueta_lista, tarea_lista, fecha_lista, archivo_lista])

    lista.sort()
    return lista, diccionario

def eliminar_tarea(lista_tareas):
    """
    Realiza la accion de eliminar la tarea que el usuario seleccione con el cursor.
    :param lista_tareas[Treeview]: arbol que contiene laos valores de las tareas.
    :return: none
    """
    #obtiene la seleccion del cursor
    seleccion = lista_tareas.selection()
    valor = messagebox.askokcancel("eliminar", "¿esta seguro de borrar esta(s) tarea(s)?",)
    #elimina el o los elementos
    if valor == True:
        for elemento in seleccion:
            for k in datos_archivos:
                if (lista_tareas.item(seleccion, 'values')[2]) == k[0]:
                    datos_archivos.remove(k)
            lista_tareas.delete(elemento)

#----------------------------------------------------------

def agregar_archivo():
    """
    Despliga el explorador de archivos para seleccionar el archivo que va a agregar.
    :param none:
    :return: none
    """
    global ruta_archivo
    global nombre_archivo
    ruta_archivo = filedialog.askopenfilename(title="Agregar", initialdir="C:/", filetypes =(("Todos los archivos","*.*"),
                                                                                        ("Archivos pdf","*.pdf"),
                                                                                        ("Archivos de texto","*.txt")))
    nombre_archivo = (ruta_archivo.split("/"))[-1]

def ver_archivo():
    """
    Despliega la ventana con la lista de archivos que se tiene.
    :param none:
    :return: none
    """
    # creacion ventana
    vent_arch = Tk()
    vent_arch.title("Archivos")
    vent_arch.geometry('600x250')
    vent_arch.resizable(False, False)

    #creacion boton para abrir archivo
    boton_abrir_archivo = Button(vent_arch, text='Abrir archivo',
                                 command=lambda: abrir_archivo(lista_archivos), bg='grey70')
    boton_abrir_archivo.place(x=500, y=100)


    # listado de archivos
    lista_archivos = ttk.Treeview(vent_arch, columns=('#1', '#2'))
    lista_archivos.grid(padx=10, pady=10)

    lista_archivos.column("#0", width=150, minwidth=150)
    lista_archivos.heading('#0', text='Nombre')
    lista_archivos.column("#1", width=300, minwidth=300)
    lista_archivos.heading('#1', text='Ruta')
    lista_archivos.column("#2", width=0, minwidth=0)
    lista_archivos.heading('#2', text='')

    #inserta archivos
    for elemento in datos_archivos:
        lista_archivos.insert(parent='', index=END, text=elemento[0],
                            values=(elemento[1]))

def abrir_archivo(lista_archivos):
    """
    Abre la visualizacion del archivo seleccionado.
    :param none:
    :return: none
    """
    select = lista_archivos.selection()
    if select != ():
        wb.open_new(lista_archivos.item(select, 'values')[0])

#--------------------------------------------------------

def cuadro_notas(notas):
    """
    Genera todos los botones, recuadros de entrada y labels del apartado de notas.
    :param frame[notas]: pestaña del apartado de notas
    :return: none
    """
    # labels de entradas
    label_etiqueta = Label(notas, text='Etiqueta', font=("Arial", 12))
    label_etiqueta.place(x=102, y=10)
    label_nota = Label(notas, text='Nota', font=("Arial", 12))
    label_nota.place(x=250, y=1)

    # cajetines de entrada
    entrada_etiqueta = Entry(notas, font=("Arial", 12), width='10')
    entrada_etiqueta.place(x=100, y=30)
    entrada_nota = Text(notas, width= 55, height= 8)
    entrada_nota.place(x=250, y=25)


    # listado de tareas
    lista_notas = ttk.Treeview(notas, columns=('#1', '#2'))
    lista_notas.grid(padx=50, pady=170)

    lista_notas.column("#0", width=200, minwidth=200)
    lista_notas.heading('#0', text='Etiqueta')
    lista_notas.column("#1", width=450, minwidth=450)
    lista_notas.heading('#1', text='Nota')
    lista_notas.column("#2", width=0, minwidth=0)
    lista_notas.heading('#2', text='')

    #botones de control
    boton_entrada = Button(notas, text='Añadir nota', bg='lawngreen', fg='black',
                           command=lambda: ent_text(entrada_etiqueta,
                                                    entrada_nota,
                                                    lista_notas))
    boton_entrada.place(x=110, y=70)

    boton_eliminar = Button(notas, text='Eliminar nota(s) seleccionada(s)', bg='orangered', fg='black',
                            command=lambda: eliminar_nota(lista_notas))
    boton_eliminar.place(x=50, y=120)

def  ent_text(entrada_etiqueta, entrada_nota, lista_notas):
    """
    Realiza el procesamiento de los datos de entrada del apartado de notas
    :param entrada_etiqueta[string]: entrada del recuadro de la etiqueta
    :param entrada_tarea[string]: entrada del recuadro de la tarea
    :param lista_tareas[Treeview]: arbol que contiene laos valores de las tareas.
    :param modo_orden[string]: seleccion entre ordenamiento por fecha y etiqueta.
    :return: none
    """
    if entrada_nota.get(1.0, END) != '':
        vacio = ''
        #insercion de  notas nuevas
        lista_notas.insert(parent='', index=END, text=entrada_etiqueta.get(),
                           values=(entrada_nota.get(1.0, END), vacio))

        #llamado de la funcion de ordenamineto
        lista, dicci = ord_etiq(lista_notas)

        #borra texto de los recuadro de entrada
        entrada_etiqueta.delete(0, END)
        entrada_nota.delete(1.0, END)

        #borra las notas del la lista de notas
        for elemento in lista_notas.get_children():
            lista_notas.delete(elemento)

        #reinserta las notas ordenadas
        for guia in lista:
            for datos in dicci[guia]:
                lista_notas.insert(parent='', index=END, text=guia,
                                    values=(datos[1]))
def ord_etiq(lista_notas):
    """
    Organiza la informacion del arbol de notas.
    :param lista_notas[Treeview]: arbol que contiene laos valores de las tareas.
    :return: lista
    :return: diccionario
    """
    lista = []
    diccionario = {}

    #ordenamiento de las notas
    for elemento in lista_notas.get_children():
        etiqueta_lista = lista_notas.item(elemento, 'text')
        nota_lista = lista_notas.item(elemento, 'value')
        if not(etiqueta_lista in  diccionario):
            lista.append(etiqueta_lista)
            diccionario[etiqueta_lista] = [[etiqueta_lista,nota_lista]]
        else:
            diccionario[etiqueta_lista].append([etiqueta_lista, nota_lista])
    lista.sort()
    return lista, diccionario

def eliminar_nota(lista_notas):
    """
    Organiza la informacion del arbol de tareas.
    :param lista_notas[Treeview]: arbol que contiene laos valores de las tareas.
    :return: none
    """
    #obtencion seleccion cursor
    seleccion = lista_notas.selection()
    valor = messagebox.askokcancel("eliminar", "¿esta seguro de borrar esta(s) nota(s)?")

    #eliminado notas seleccionadas
    if valor == True:
        for elemento in seleccion:
            lista_notas.delete(elemento)

#-----------------------------------------------

def corferias():
    """
    genera la ventana principal con la lista de eventos.
    :param none:
    :return: none
    """
    #creacion ventana
    vent_cor = Tk()
    vent_cor.title("Cronograma corferias")
    vent_cor.geometry('850x520')
    vent_cor.resizable(False, False)

    #creacion recuadro de texto
    texto_descrip = Text(vent_cor, width= 100, height=10 )
    texto_descrip.place(x=25, y=300)

    #creacion botones de previsualizacion
    boton_descrip = Button(vent_cor, text= 'Mas sobre la convencion selecionada',
                           command=lambda: info_even(texto_descrip, lista_convenciones), bg='grey70')
    boton_descrip.place(x=300, y=20)

    boton_link = Button(vent_cor, text= 'Obtener link',
                        command=lambda: info_link(texto_descrip, lista_convenciones), bg='grey70')
    boton_link.place(x=30, y=20)

    #creacion arbol de comvenciones
    lista_convenciones = ttk.Treeview(vent_cor, columns=('#1', '#2'))
    lista_convenciones.grid(padx=20, pady=50)

    lista_convenciones.column("#0", width=250, minwidth=250)
    lista_convenciones.heading('#0', text='Link')
    lista_convenciones.column("#1", width=300, minwidth=300)
    lista_convenciones.heading('#1', text='Informacion')
    lista_convenciones.column("#2", width=250, minwidth=250)
    lista_convenciones.heading('#2', text='Fecha')

    #llavado de funciones
    pagina()
    num1 = informacion()
    datos(num1[0],num1[1],num1[2],  lista_convenciones)

def info_link(texto_descrip, lista_convenciones):
    """
    Organiza la informacion del arbol de tareas.
    :param Text[texto_descripcion]: recuadro de visualizacion de texto
    :param Treeview[lista_convenciones]: arbol que contiene la informacion de las convenciones.
    :return: none
    """
    #obtencion de la seleccion del cursor
    texto_descrip.delete(1.0, END)
    select = lista_convenciones.selection()

    #envio informacion de la casilla del link
    if select != ():
        texto_descrip.insert(0.0, lista_convenciones.item(select, 'text'))
    else:
        texto_descrip.insert(0.0, 'Seleccione una convencion')

def info_even(texto_descrip, lista_convenciones):
    """
    Organiza la informacion del arbol de tareas.
    :param Text[texto_descripcion]: recuadro de visualizacion de texto
    :param Treeview[lista_convenciones]: arbol que contiene la informacion de las convenciones.
    :return: none
    """
    # obtencion de la seleccion del cursor
    texto_descrip.delete(1.0, END)
    select = lista_convenciones.selection()

    # envio informacion de la casilla de informacion del evento
    if select != ():
        texto_descrip.insert(0.0, lista_convenciones.item(select, 'values')[0])
    else:
        texto_descrip.insert(0.0, 'Seleccione una convencion')

def pagina():
    """
    Extrae la información del sitio web guardandola en el archivo .txt llamado "Archivo_corferias"
    :param none:
    :return: none.
    """
    url = "https://corferias.com/?doc=calendario_ferial&ids=4&intAno=2021&intIdioma=1&StrIdioma=es"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    texto = soup.get_text()
    lineas = [linea for linea in texto.split('\n') if linea != '']
    texto_limpio = '\n'.join(lineas)
    archivo_externo = open("Archivo_corferias.txt","w")
    archivo_externo.write(texto_limpio)
    archivo_externo.close()

def informacion():
    """
    Busca  en el  "archivo_corferias" la informacion del nombre o el link, la descripcion
     y la fecha del evento, añade esta informacion a  listas.
    :param none:
    :return: links | fechas | informacion.
    """
    archivo_externo = open("Archivo_corferias.txt", "r")
    j = 0
    links=[]
    fechas=[]
    informacion=[]
    link = [" "]
    for line in archivo_externo.readlines():
        j = j + 1
        line = str(line)
        line = line.split(' ')
        if line[0] == "Del":
            links.append(link)
            fechas.append(line)
        elif link[0] == "Información" and link[1] == "General\n":
            informacion.append(line[0:(len(line)-4)])
        link = line
    archivo_externo.close()
    return links,fechas,informacion

def datos(links,fechas,informacion, arbol):
    """
    Muestra de forma organizada los datos de cada convencion y los guarda en un archivo .txt llamado
    "Archivo_datos_convenciones".
    :param list[string] links: lista de los links de los eventos.
    :param list[string] fechas: lista de las fechas de los eventos.
    :param list[string] informacion: lista de la descripcion de los eventos.
    :return: none
    """
    archivo= open("Archivo_datos_convenciones.txt","w")
    for j in range(len(links)):
        archivo.write(" CONVENCION " + str(j + 1) + "\n")
        link = ''
        for i in links[j]:
            archivo.write(" " + i)
            link += str(i) + " "
        descripcion = ''
        for i in informacion[j]:
            archivo.write(i + " ")
            descripcion += str(i) + " "
        fecha_conv = ''
        for i in fechas[j]:
            archivo.write(" " + i + " ")
            fecha_conv += (i) + " "
        archivo.write("//////////////////" + "\n")
        arbol.insert(parent='', index=END, text=link, values=(descripcion, fecha_conv))

    archivo.close()

def main():
    menu_pantalla()
main()