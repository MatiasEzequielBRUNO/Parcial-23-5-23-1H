import json
##importa la biblioteca json 
import re
#importo la biblioteca regex

def leer_archivo_json(nombre_archivo:str) -> list:
    lista = []
    with open(nombre_archivo,"r") as archivo:
        #abro el archivo en modo "r"read (lectura) para leerlo y en este caso copiar los datos
        #uso la sentencia with para que el interprete se encargue de cerrarlo automaticamente 
        #asi no depende de que yo haga el close para que se guarde todo
        #y lo voy a llamar "archivo" 

        diccionario = json.load(archivo)
        #con el load lo que hago es cargar el archivo en la variable, en este caso diccionario

        lista = diccionario["jugadores"]
        #asi cargo la lista que esta dentro del diccionario a la lista que voy a utilizar

    return lista

def validar_menu (respuesta):
    #esta funcion valida que la opcion ignresada solo sea un numero de los que se muestan en el menu
    patron = r"[1]?[0-9]{1}$|20|23"  
    #en este regex doy la posibilidad de cero o una ocurrencia del 1, que al final tenga del 0 al 9 
    #y doy la posibilidad de la opcion 20 y 23 
    patron = re.match(patron, respuesta)
    #busco las condiciones del patron dentro de la respuesta

    if(patron):
        #si el patron se cumple el flag se torna false y entonces no entra al while que esta en el menu
        flag = False
        return flag
    else:
        flag = True
        return flag

def validar_indice (indice:str, lista:list):
    patron = r"[1-9]+"
    patron = re.match(patron, indice)
    #busco las condiciones del patron dentro del indice

    if(patron):
        #si el patron se cumple el flag se torna false y entonces no entra al while que esta en el menu
        indice = int(indice)-1
        if(indice in lista):
            #lo hago de esta manera para que sea dinamico, si el indice esta en la lista no entro al while
            flag = False
            return  flag
    else: 
        flag = True
        return flag

def generar_archivo_csv(nombre_archivo:str, lista:list):
    #le paso por parametros el nombre o la ruta de donde va a guardar los datos para generar el csv
    #y tambien le paso la lista de donde voy a tomar los datos

    with open(nombre_archivo,"a") as archivo:
        #abro el archivo en modo "a" append para poder escribir el archivo y agregar siempre al final
        #uso la sentencia with para que el interprete se encargue de cerrarlo automaticamente 
        #asi no depende de que yo haga el close para que se guarde todo
        #y lo voy a llamar "archivo" 
        
        for indice in range(len(lista_aux)):
            #recorro la lista_aux que hice previamente ne el punto 2 para generar la primera linea con los encabezados 
            texto_linea = "{0}, ".format(lista_aux[indice]).capitalize()                             
            #voy a crear la linea de texto con todos los elementos que la integran para formar el encabezado
            #en este caso son todos strings entonces no los tengo que castear pero hago que todos inicien con mayuscula
            archivo.write(texto_linea)
            #de esta manera en el archivo cargo linea a linea lo que fui generando
        archivo.write("\n")
        #este ultimo write es para generar el salto de linea y asi separar el encabezado 

        for indice in range(len(lista)):
            #recorro la lista que recibi por parametro
            texto_linea = str("{0}, ".format(lista[indice]))
            #voy a crear la linea de texto con todos los elementos que la integran para formar el encabezado
            #en este caso NO son todos strings entonces los tengo que castear pero hago que todos inicien con
            # mayuscula debido a que tengo el nombrecon el resto no hay problema porque son numeros, 
            # el casteo a str es porque sino el programa se rompe y no escribe los numeros
            archivo.write(texto_linea)
            #de esta manera en el archivo cargo linea a linea lo que fui generando
        archivo.write("\n")
        #genero el salto de linea para que a cada encabezado le corresponda un valor 

lista = leer_archivo_json("1 cuatrimestre\Para el examen\dt.json")
flag_while = True
flag_2 = False

while (flag_while == True):
    flag = True
    print("\nMenu de opciones:")
    print("1) Mostrar la lista de todos los jugadores del Dream Team")
    print("2) Seleccionar un jugador por su índice y mostrar sus estadísticas completas")
    print("3) Guardar las estadísticas de ese jugador en un archivo CSV")
    print("4) Buscar un jugador y ver sus logros")
    print("0) Salir")

    respuesta = input("Ingrese el punto a probar con el numero indicado\n")
    flag = validar_menu(respuesta)

    while(flag):
        respuesta = input("Ingrese nuevamente el punto a probar con el numero indicado\n")
        flag = validar_menu(respuesta)
    
    respuesta = int(respuesta)

    if(respuesta == 1):
        for diccionario in lista:
            print("{0} - {1}".format(diccionario["nombre"], diccionario["posicion"]))

    if(respuesta == 2):
        flag_2 = True
        lista_csv = []
        lista_aux = []

        for diccionario in lista:
            print("{0}): {1}".format(lista.index(diccionario)+1, diccionario["nombre"]))
            #recorro la lista y muestro el indice de cada diccionario y el valor de la clave nombre de cada uno

        indice = input("Seleccione el indice el indice del jugador\n")
        flag = validar_indice(indice, lista)
        while(flag):
            indice = input("Ingrese nuevamente el indice del jugador\n")
            flag = validar_indice(indice, lista)
        #una vez que se selecciona el jugador mediante el indice de la lista y es valido
        indice = int(indice)-1

        diccionario_jugador = lista[indice]
        nombre_jugador = (diccionario_jugador["nombre"])
        print("{0}".format(nombre_jugador))
        lista_csv.append(nombre_jugador)
        lista_aux.append("nombre")
        #aprovecho que ya estoy en ese diccionario y agrego el nombre a la lista csv 

        for clave, valor in diccionario_jugador["estadisticas"].items():
            print("{0}:  {1}".format(clave, valor))
            lista_aux.append(clave)
            lista_csv.append(valor)
        #y despues imprimo por pantalla las estadisticas del jugador, como ya estoy recorriendo el diccionario
        #que voy a encesitar en el punto 3, aprovecho y voy cargando los valores en la lista csv y las claves
        #en la lista aux que me van a servir para armar el encabezado del documento csv

    if(respuesta == 3):
        if(flag_2 == True):
            generar_archivo_csv("1 cuatrimestre\Para el examen\{0}.csv".format(nombre_jugador), lista_csv)
            #solamente si el paso 2 se ejecuto voy a poder hacer el 3. Mediante el nombre del jugador que eligio
            #y la lista csv cargada con los valores de las claves del dicionario estadisticas voy a generar un csv 

        else:
            print("Debe realizar el paso 2 primero")
    
    if(respuesta == 4):
        pass
    
    
    if(respuesta == 0):
        flag_while = False
