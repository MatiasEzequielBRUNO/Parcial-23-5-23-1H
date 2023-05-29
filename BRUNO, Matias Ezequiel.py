import json
##importa la biblioteca json 
import re
#importo la biblioteca regex


def leer_archivo_json(nombre_archivo:str) -> list:
    lista = []
    with open(nombre_archivo,"r", encoding = "utf-8") as archivo:
        #abro el archivo en modo "r"read (lectura) para leerlo y en este caso copiar los datos
        #uso la sentencia with para que el interprete se encargue de cerrarlo automaticamente 
        #asi no depende de que yo haga el close para que se guarde todo
        #y lo voy a llamar "archivo" 
        #el encoding se usa para que reconozca los caracteres especiales de nuestro abecedario
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
    patron = r"[1-9]{1}$|10|11|12"
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


def validar_0_a_100 (numero:str):   #ver como validar con coma
    patron = r"^(100(\.0{1,2})?|[0-9]{1,2}(\.[0-9]{1,2})?)$"
    patron = re.match(patron, numero)
    #busco las condiciones del patron dentro del indice

    if(patron):
        #si el patron se cumple el flag se torna false y entonces no entra al while que esta en el menu
        numero = float(numero)    
        flag = False
        return  flag
    else: 
        flag = True
        return flag


def generar_archivo_csv(nombre_archivo:str, lista_valores:list, lista_ecabezados:list):
    #le paso por parametros el nombre o la ruta de donde va a guardar los datos para generar el csv
    #y tambien le paso la lista de donde voy a tomar los datos

    with open(nombre_archivo,"a") as archivo:
        #abro el archivo en modo "a" append para poder escribir el archivo y agregar siempre al final
        #uso la sentencia with para que el interprete se encargue de cerrarlo automaticamente 
        #asi no depende de que yo haga el close para que se guarde todo
        #y lo voy a llamar "archivo" 
        
        for indice in range(len(lista_ecabezados)):
            #recorro la lista_ecabezados que hice previamente ne el punto 2 para generar la primera linea con los encabezados 
            texto_linea = "{0}, ".format(lista_ecabezados[indice]).capitalize()                             
            #voy a crear la linea de texto con todos los elementos que la integran para formar el encabezado
            #en este caso son todos strings entonces no los tengo que castear pero hago que todos inicien con mayuscula
            archivo.write(texto_linea)
            #de esta manera en el archivo cargo linea a linea lo que fui generando
        #archivo.write("\n")
        #este ultimo write es para generar el salto de linea y asi separar el encabezado 

        for indice in range(len(lista_valores)):
            #recorro la lista que recibi por parametro
            texto_linea = str("{0}, ".format(lista_valores[indice]))
            #voy a crear la linea de texto con todos los elementos que la integran para formar el encabezado
            #en este caso NO son todos strings entonces los tengo que castear pero hago que todos inicien con
            # mayuscula debido a que tengo el nombrecon el resto no hay problema porque son numeros, 
            # el casteo a str es porque sino el programa se rompe y no escribe los numeros
            archivo.write(texto_linea)
            #de esta manera en el archivo cargo linea a linea lo que fui generando
        archivo.write("\n")
        #genero el salto de linea para que a cada encabezado le corresponda un valor 


def calculador_promedio (lista:list, clave1:str, clave2:str):
    lista_ingresada = lista[:]
    # Para calcular el promedio ingreso una lista a la cual le hago una copia para not rabajar sobre la original
    acumulador = 0
    promedio = 0
    for diccionario in lista_ingresada:
        #recorro cada diccionario de la lista de jugadores (la que ingrese)
        for clave,valor in diccionario[clave1].items():
            #recorro los diccionarios que estan dentro de uno de los diccionarios de la lista el cual elijo mediante
            # la clave1 tomando las claves y valores para luego utilizarlas
            if(clave == clave2):
                #si la clave que obtuve anteriormente es = a la clave2 que yo ingrese al llamar la funcion, ingreso al if
                acumulador += valor
                #y en el acumulador sumo el valor que obtuve anteriormente ya que este corresponde a la clave que yo buscaba
    promedio = acumulador / len(lista_ingresada)
    #para calcular el promedio se debe realizar la suma de todos los elementos y dividir el total por la cantidad de elementos sumados
    promedio = round(promedio, 2)
    #redondeo el resultado a 2 decimales
    return promedio


def ordenador_ascendente(lista:list, clave1:str, clave2:str)->list:
# Esta funcion se encarga de ordenar una lista de maner ascendente como lo dice su nombre
    lista_ingresada = lista[:]
    rango_a = len(lista_ingresada)
    flag_swap = True
    #realizo una copia de la lsita ingresada para no trabajar sobre la original
    #determino el rango para saber cuantos indices tiene la lista emdiante un len de la lista
    #y defino una bandera que nos va a serivr para saber cuando ya esta ordenada

    if (clave2 == None):
        #en este caso lo que hice esto debido a que yo necesitaba ordenar una lista alfabeticamente pero la clave a la que 
        #debia ingresar no tenia mas claves adentro entonces yo le doy por parametro la unica clave que necesito que utilice para 
        #obtener un valor y como la sgunda no es necesaria la utilizo como condicion para que solo en ese caso utilice esta
        #parte de la funcion
        lista_ingresada = sorted(lista_ingresada, key = lambda x : x[clave1]) #ANDA FLAMA PERO IMPORTANTISIMO ACLARAR QUE ES ESTO
        #la funcion sorted realiza una copia ordenada alfabeticamente de lista que se le ingresa por parametro, como en este caso yo 
        # necesitaba que el orden lo realice mediante el valor de una de las claves del diccionario (clave1) recurri a la funcion lambda
        # este tipo de funcion es anonima, a diferencia de las funciones regulares definidas, no necesitan el def y pueden ser utilizadas
        #para casos en los que pueden necesitarse una funcion para realizar una tarea unica en un momento especifico por lo que no es 
        #necesario realizar una funcion regular definida. En este caso yo la utlizo para asignarle una clave en el parametro a la 
        #funcion sorted para que trabaje con los valores de esa clave, ya que el parametro key es opcional pero solo acepta funciones tanto 
        #lambdas como definidas y como dije anteriormente no tiene sentido hacer una funcion definida porque incluzo el def nombre de la funcion
        #seria mas larga que el codigo mismo d ela funcion

        return lista_ingresada
        #una vez realizada la operacion retorna la lista en la cual guardo la copia de la lista ingresada por parametro

    else: 
        while(flag_swap):
            #mientras que la badnera sea True, vamos a permanecer dentro del while haciendo un bucle
            flag_swap = False
            #aca el valor de la bandera se cambia para saber si se realizó un cambio en el orden de la lista ya que si no se hiciera
            #ninguno la bandera permaneceria false y no volveriamos a entrar al while, esto es necesario porque si nunca cambiamos el
            #valor de la bandera a false, por mas que ya este ordenada la lista permaneceriamos atrapados indefinidamente en el while 
            rango_a = rango_a - 1
            #por cada vuelta que hago en el while al rango lo reduzco en 1 debido a que de la manera en la que ordena los elementos esta
            #funcion, al mayor de los elementos que comparó los manda a la ultima posicion de los elementos que comparó, entonces en la 
            #primera vuelta el mayor de la lista va a quedar ultimo y no es necesario en la segunda vuelta volver a comparar ese elemento
            #porque ya se encuentra en l posicion correcta, este artilugio logra segun lo visto en las clases una reduccion del 50% del 
            #tiempo de ordenamiento. Decidi utilizar esta funcion ya que era un poco mas simple y la cantidad de elementos a ordenar no era
            #muy grande entonces la crei adecuada. Una analogia seria utilizar un camion para llevar solamente un balde de piedras

            for indice_A in range(rango_a):
                #con el for lo que voy haciendo es que en cada vuelta me de un indice el cual voy a utilizar para comparar
                if  lista_ingresada[indice_A][clave1][clave2] > lista_ingresada[indice_A+1][clave1][clave2]:
                    #este if me dice que si el primer elemento (indice_a) es mayor al elemento siguiente (indice_a + 1), ingrese
                    lista_ingresada[indice_A],lista_ingresada[indice_A+1] = lista_ingresada[indice_A+1],lista_ingresada[indice_A]
                    #y realice un swap alternando la posicion entre ambos elementos y desplazando al elemento mayor a la posicion del 
                    #elemento con el cual es comparado
                    flag_swap = True
                    #en este punto al haberse realizado un cambio en el orden le asignamos el valor true para que vuelva a ingresar al while
                    #ya que podrian quder elementos por ordenar, una vez que todo este ordenado ingresa una vez mas al while porque la bandera
                    #es True pero los elementos a compara no cumplen con la condicion del if por lo que la bandera queda en False por la 
                    #asignacion previa al if y ahi no vuelve a ingresar mas al while

    return lista_ingresada
    #por ultimo se retorna una copia de la lista ingresada pero ordenada de menor a mayor


def mayor_cantidad(lista_original:list, clave1, clave2)->list:
    lista = lista_original[:]
    if(len(lista)<=1):
        return lista
    #esta funcion recorre la lista de elemento ingresando a la/las claves correspondientes y comparando los valores de las mismas
    #buscando el valor mas grande y retornando el indice del elemento correspondiente para poder utilizar la informacion completa
    # del elemento y no solo el valor por el cual se comparo.
    #el primer if comprueba que la lista no tenga mas de 1 el elemento, ya que si solo tuviera 1, ese elemento seria el mayor y si 
    # no tuviera nada la lista estaira vacia, en ambos casos retorna la lista tal cual la recibió
    else:
        indice = 0
        mayor_indice = 0
        if(clave2 == None):
            #esto lo hago porque en el punto 17 necesito comparar los jugadores en base a la cantidad de logros obtenidos y como el 
            #el valor de la clave logros es una lista y no un diccionario,no contiene mas claves en su interior entonces el codgio se rompia
            #a su vez aproveche eso utilizando la clave2 como una especie de bandera para que solo en ese caso ingrese a este if
            mayor = len(lista[indice][clave1])
            #le asigno el largo de la lista de logros del primer elemento de la copia de la lista ingresada para poder comparar con otros elementos
            #de dicha lista
            for elemento in lista:
                #recorro la lista elemento a elemento
                elemento = len(elemento[clave1])   
                #guardando el largo de a lista logros como dato para comparar  
                if(elemento > mayor):
                    #Realizo la comparacion y si un elemento es mayor al elemento de referencia (mayor) ingreso al if
                    mayor_indice = indice
                    #guardo el indice correspondiente a ese elemento
                    mayor = elemento
                    #y guardo el elemento en referencia para poder compararlo con los elementos que quedan
                
                indice +=1
                #sumo 1 al indice para saber en que posicion me encuentro de la lista
            
            return mayor_indice
            #devuelvo el indice correspondiente al elemento mas grande
           
        else:    
            #se realiza lo mismo que en la parte anterior solo que en este caso no se trabaja con el largo de una lista como dato para comparar
            #sino que se utiliza el valor alojado dentro de la clave que esta dentro del diccionario dentro del diccionario de cada elemento de la lista
            mayor = lista[indice][clave1][clave2]
            for elemento in lista:
                
                elemento = elemento[clave1][clave2]
                if(elemento > mayor):
                    mayor_indice = indice
                    mayor = elemento
                
                indice +=1
            return mayor_indice
        


def comparador_mayor_al_valor_ingresado(lista:list, numero:float, clave1, clave2)->list:
    #esta funcion trabaja de la misma manera que la de mayor cantidad solo que esta vez nosotros le pasamos por parametro el valro que va a ser de 
    #referencia para comparar con los otros elementos y en vez de retornar solo 1 indice, guarda una lista con los indices de los elementos que 
    #cumplan los requisitos y despues la retorna para poder utilizar tambien la informacion completa de los elementos que son mayores al valor ingresado
    lista_ingresada = lista[:]
    lista_promedio = []
    indice = 0
    mayor = numero
    for elemento in lista_ingresada:
        
        elemento = elemento[clave1][clave2]
        if(elemento > mayor):
            lista_promedio.append(indice)
            
        indice +=1
    
    return lista_promedio


def ranking_estadisticas (lista:list, clave:str, valor)->int:
    #esta funcion recibe por parametro una lista, una clave y un valor que va a utilizar para comparar
    for diccionario in lista:
        #recorre los diccionarios de la lista
        if(diccionario[clave] == valor):
            #si el valor de la clave del diccionario es = al valor ingresado para comparar, ingresa al if 
            posicion = lista.index(diccionario)+1
            #y guarda la posicion de la lista de ese diccionario 
            return posicion
            #y retorna la posicion, esto lo vamos a ulitizar para saber en que posicion quedo cada jugador para el bonus


def buscar_valores(lista:list, palabra:str, clave1):
    patron = r".*{0}.*".format(palabra)
    #esta funcion busca palabras similares a la ingresada, con el patron lo que yo digo es que busque cualquier cadena que 
    #contenga la palabra en cualquier posición dentro de la cadena
    lsita_coincidencias = []
    for elemento in lista:
        #recorro la lista para buscar los elementos que coincidan
        buscar_valor = re.search(patron, elemento[clave1], re.IGNORECASE)
        #hago la comparacion usando ignorecase para que ignore mayusculas y minusculas
        if(buscar_valor):
            #si el valor de la clave del elemento coincide, va a ingresar al if 
            lsita_coincidencias.append(elemento)
            #y va a agregar al elemento a la lista que va a retornar
    return lsita_coincidencias


def validar_palabras (palabra:str):
    #esta funcion valida que la plabra ingresada solo tenga letras 
    flag = True
    if palabra.isalpha():
        flag = False
    return flag


#############################################################################################################################

lista_jugadores = leer_archivo_json("Para el examen\dt.json")
flag_while_menu = True
flag_2 = False

while (flag_while_menu == True):
    flag = True
    print("\nMenu de opciones:")
    print("1) Mostrar la lista de todos los jugadores del Dream Team")
    print("2) Seleccionar un jugador por su índice y mostrar sus estadísticas completas")
    print("3) Guardar las estadísticas de ese jugador en un archivo CSV")
    print("4) Buscar un jugador y ver sus logros")
    print("5) Promedio de puntos por partido del Dream Team")
    print("6) Ver si el jugador es miembro del Salón de la Fama del Baloncesto")
    print("7) Jugador con la mayor cantidad de rebotes totales")
    print("8) Jugador con la mayor porcentaje de tiros de campo")
    print("9) Jugador con la mayor cantidad de asistencias totales")
    print("10) Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor")
    print("11) Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor")
    print("12) Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor")
    print("13) Jugador con la mayor cantidad de robos totales")
    print("14) Jugador con la mayor cantidad de bloqueos totales")
    print("15) Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor")
    print("16) Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido")
    print("17) Mostrar el jugador con la mayor cantidad de logros obtenidos")
    print("18) Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor")
    print("19) Jugador con la mayor cantidad de temporadas jugadas")
    print("20) Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor")
    print("23) Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking: Puntos, Rebotes, Asistencias y Robos, y exportar a csv")
    print("0) Salir")

    opcion = input("Ingrese el punto a probar con el numero indicado\n")
    flag = validar_menu(opcion)

    while(flag):
        opcion = input("Ingrese nuevamente el punto a probar con el numero indicado\n")
        flag = validar_menu(opcion)
    
    #primero le pido al usuario que ingrese una opcion y la valido mediante una funcion, una vez validada casteo la opcion para que acceda a cada punto
    opcion = int(opcion)

    if(opcion == 1):
        for diccionario in lista_jugadores:
            print("{0} - {1}".format(diccionario["nombre"], diccionario["posicion"]))
            #recorre los diccionarios de la lista accediendo a los nombres y posiciones y los imprime por pantalla

    if(opcion == 2):
        flag_2 = True
        lista_csv_valores_2 = []
        lista_aux_2 = []

        for diccionario in lista_jugadores:
            print("{0}) {1}".format(lista_jugadores.index(diccionario)+1, diccionario["nombre"]))
            #recorro la lista y muestro el indice de cada diccionario y el valor de la clave nombre de cada uno

        indice = input("Seleccione el indice el indice del jugador\n")
        flag = validar_indice(indice, lista_jugadores)
        while(flag):
            indice = input("Ingrese nuevamente el indice del jugador\n")
            flag = validar_indice(indice, lista_jugadores)
        #una vez que se selecciona el jugador mediante el indice de la lista y es valido
        indice = int(indice)-1
        #le resto 1 al indice porque por pantalla muestro a partir del 1 pero en las listas va a partir de 0
        diccionario_jugador = lista_jugadores[indice]
        #guardo el diccionario correspondiente al indice elegido
        nombre_jugador = (diccionario_jugador["nombre"])
        #y el nombre del jugador
        print("{0}".format(nombre_jugador))
        #imprimo el nombre del jugador por pantalla
        lista_csv_valores_2.append("\n{0}".format(nombre_jugador))
        lista_aux_2.append("nombre")
        #aprovecho que ya estoy en ese diccionario y agrego el nombre a la lista csv y la clave nombre en la aux
        #para despues usar esta lista para los encabezados

        for clave, valor in diccionario_jugador["estadisticas"].items():
            print("{0}:  {1}".format(clave, valor))
            lista_aux_2.append(clave)
            lista_csv_valores_2.append(valor)
        #y despues imprimo por pantalla las estadisticas del jugador, como ya estoy recorriendo el diccionario
        #que voy a encesitar en el punto 3, aprovecho y voy cargando los valores en la lista csv y las claves
        #en la lista aux que me van a servir para armar el encabezado del documento csv
        
    if(opcion == 3):
        if(flag_2 == True):
            generar_archivo_csv("Para el examen\{0}.csv".format(nombre_jugador), lista_csv_valores_2, lista_aux_2)
            #solamente si el paso 2 se ejecuto voy a poder hacer el 3. Mediante el nombre del jugador que eligio
            #y la lista csv cargada con los valores de las claves del dicionario estadisticas voy a generar un csv 

        else:
            print("Debe realizar el paso 2 primero")
    
    if(opcion == 4):
        #ingreso el nombre del jugador, recorro la lista con un for y tengo que buscar los jugadores que tengan un 
        #nombre que coincida con el nombre ingresado y luego mostrar el logro de cada uno de los que coincidio
        nombre_jugador_ingresado = input("Ingrese el nombre del jugador para ver sus logros\n")
        flag = validar_palabras(nombre_jugador_ingresado)
        while (flag):
            nombre_jugador_ingresado = input("Ingrese nuevamente el nombre del jugador para ver sus logros\n")
            flag = validar_palabras(nombre_jugador_ingresado)
        clave1 = "nombre"    
        lista_aux_4 = buscar_valores(lista_jugadores, nombre_jugador_ingresado, clave1)
        #valido que hayan ingresado solamente letras y despues en la lsita guardo las coincidencias 

        while(len(lista_aux_4) == 0):
            nombre_jugador_ingresado = input("No hay conicidencias, por favor ingrese nuevamente el nombre\n")
            flag = validar_palabras(nombre_jugador_ingresado)
            while (flag):
                nombre_jugador_ingresado = input("Ingrese nuevamente el nombre del jugador para ver sus logros\n")
                flag = validar_palabras(nombre_jugador_ingresado)   
            lista_aux_4 = buscar_valores(lista_jugadores, nombre_jugador_ingresado, clave1)
        #si no hubo coincidencias doy la opcion para que vuelva a ingresar nuevamente un jugador

        for jugador in lista_aux_4:
            print("\nJugador: {0}".format(jugador["nombre"]))
            print("Logros:")
            for elementos in jugador["logros"]:
                print("-{0}".format(elementos))
        #una vez que hay al menos una coincidencia imprimpo por pantalla el nombre y los logros recorriendo la lsita de logros

    if(opcion == 5):
        clave1 = "estadisticas"
        clave2 = "promedio_puntos_por_partido"
        promedio = calculador_promedio(lista_jugadores, clave1, clave2)
        lista_jugadores_ordenada = ordenador_ascendente(lista_jugadores, clave1, clave2)
        print("El promedio total de puntos por partido del equipo es: {0}".format(promedio))
        for diccionario in lista_jugadores_ordenada:
            print("{0}: \t\tPromedio: {1}".format(diccionario["nombre"].capitalize(), diccionario[clave1][clave2]))
        #con el promedio lo que hago es calcular el promedio del equipo completo del dream team y luego ordeno la lista para 
        #que sea mas comodo visualemnte y la imprimo por pantalla 


    if(opcion == 6):
        nombre_jugador_ingresado = input("Ingrese el nombre del jugador para ver si es miembro del salon de la fama\n")
        flag = validar_palabras(nombre_jugador_ingresado)
        while (flag):
            nombre_jugador_ingresado = input("Ingrese nuevamente el nombre del jugador para ver si es miembro del salon de la fama\n")
            flag = validar_palabras(nombre_jugador_ingresado)
        clave1 = "nombre"
        lista_aux_6 = buscar_valores(lista_jugadores, nombre_jugador_ingresado, clave1)

        while(len(lista_aux_6) == 0):
            nombre_jugador_ingresado = input("No hay conicidencias, por favor ingrese nuevamente el nombre\n")
            flag = validar_palabras(nombre_jugador_ingresado)
            while (flag):
                nombre_jugador_ingresado = input("Ingrese nuevamente el nombre del jugador para ver sus logros\n")
                flag = validar_palabras(nombre_jugador_ingresado)    
            lista_aux_6 = buscar_valores(lista_jugadores, nombre_jugador_ingresado, clave1)
        #hasta este parte es igual al punto 4

        palabra = "Miembro del Salon de la Fama del Baloncesto"
        for jugador in lista_aux_6:
                print("\nJugador: {0}".format(jugador["nombre"]))
                for elementos in jugador["logros"]:
                    if(palabra == elementos):
                        print("-{0}".format(elementos))
        #recorro la lista de jugadores y dentro de la lista de logros busco que haya una coincidencia con la variable plabra
        # para saber si son miembros del salon de la fama 

    if(opcion == 7):
        clave1 = "estadisticas"
        clave2 = "rebotes_totales"
        indice = mayor_cantidad(lista_jugadores, clave1, clave2)
        print("El jugador es: {0}\tRebotes totales: {1}".format(lista_jugadores[indice]["nombre"], lista_jugadores[indice][clave1][clave2]))
        #busco dentro de las estadisticas el aprametro que quiero usar de referencia y busco el mayor y lo imprimo
    
    if(opcion == 8):
        clave1 = "estadisticas"
        clave2 = "porcentaje_tiros_de_campo"
        indice = mayor_cantidad(lista_jugadores, clave1, clave2)
        print("El jugador es: {0}\tPorcentaje de tiros de campo: {1}%".format(lista_jugadores[indice]["nombre"], lista_jugadores[indice][clave1][clave2]))
        #igual al 7

    if(opcion == 9):
        clave1 = "estadisticas"
        clave2 = "asistencias_totales"
        indice = mayor_cantidad(lista_jugadores, clave1, clave2)
        print("El jugador es: {0}\tAsistencias totales: {1}".format(lista_jugadores[indice]["nombre"], lista_jugadores[indice][clave1][clave2]))
        #igual al 7

    if(opcion == 10):
        numero = input("Ingrese un promedio\n")
        flag = validar_0_a_100(numero)
        while(flag):
            numero = input("Ingrese nuevamente el promedio\n")
            flag = validar_0_a_100(numero)
        #se pide que ingrese un numero para poder comparar mas adelante y se valida que ese numero sea valido

        numero = float(numero)
        clave1 = "estadisticas"
        clave2 = "promedio_puntos_por_partido"
        lista_promedios = comparador_mayor_al_valor_ingresado(lista_jugadores, numero, clave1, clave2)
        #luego busco todos los jugadores que tengan promedio o porcentaje (segun el ejercicio) mayor al ingresado
        
        for indice in lista_promedios:
            print("Jugador: {0}\tPromedio: {1}".format(lista_jugadores[indice]["nombre"], lista_jugadores[indice][clave1][clave2]))
        #finalmente recorro la lista de jugadores encontrados y la imprimo por pantalla
    
    if(opcion == 11):
        numero = input("Ingrese un promedio\n")
        flag = validar_0_a_100(numero)
        while(flag):
            numero = input("Ingrese nuevamente el promedio\n")
            flag = validar_0_a_100(numero)
            
        numero = float(numero)
        clave1 = "estadisticas"
        clave2 = "promedio_rebotes_por_partido"
        lista_promedios = comparador_mayor_al_valor_ingresado(lista_jugadores, numero, clave1, clave2)
        
        for indice in lista_promedios:
            print("Jugador: {0}\tPromedio: {1}".format(lista_jugadores[indice]["nombre"], lista_jugadores[indice][clave1][clave2]))
        #igual al 10

    if(opcion == 12):
        numero = input("Ingrese un promedio\n")
        flag = validar_0_a_100(numero)
        while(flag):
            numero = input("Ingrese nuevamente el promedio\n")
            flag = validar_0_a_100(numero)
        
        numero = float(numero)
        clave1 = "estadisticas"
        clave2 = "promedio_asistencias_por_partido"
        lista_promedios = comparador_mayor_al_valor_ingresado(lista_jugadores, numero, clave1, clave2)
        
        for indice in lista_promedios:
            print("Jugador: {0}\tPromedio: {1}".format(lista_jugadores[indice]["nombre"], lista_jugadores[indice][clave1][clave2]))
        #igual al 10

    if(opcion == 13):
        clave1 = "estadisticas"
        clave2 = "robos_totales"
        indice = mayor_cantidad(lista_jugadores, clave1, clave2)
        print("El jugador es: {0}\tRobos totales: {1}".format(lista_jugadores[indice]["nombre"], lista_jugadores[indice][clave1][clave2]))
        #igual al 7

    if(opcion == 14):
        clave1 = "estadisticas"
        clave2 = "bloqueos_totales"
        indice = mayor_cantidad(lista_jugadores, clave1, clave2)
        print("El jugador es: {0}\tBloqueos totales: {1}".format(lista_jugadores[indice]["nombre"], lista_jugadores[indice][clave1][clave2]))
        #igual al 7

    if(opcion == 15):
        numero = input("Ingrese un porcentaje\n")
        flag = validar_0_a_100(numero)
        while(flag):
            numero = input("Ingrese nuevamente el porcentaje\n")
            flag = validar_0_a_100(numero)
        numero = float(numero)
        clave1 = "estadisticas"
        clave2 = "porcentaje_tiros_libres"
        lista_promedios = comparador_mayor_al_valor_ingresado(lista_jugadores, numero, clave1, clave2)
        
        for indice in lista_promedios:
            print("Jugador: {0}\t %{1}".format(lista_jugadores[indice]["nombre"], lista_jugadores[indice][clave1][clave2]))
        #igual al 10

    if(opcion == 16):
        clave1 = "estadisticas"
        clave2 = "promedio_puntos_por_partido"
        lista_jugadores_ordenada = ordenador_ascendente(lista_jugadores, clave1, clave2)
        del lista_jugadores_ordenada [0]
        promedio = calculador_promedio(lista_jugadores_ordenada, clave1, clave2)
        print("El promedio total de puntos por partido del equipo es: {0}".format(promedio))
        for diccionario in lista_jugadores_ordenada:
            print("{0}: \t\tPromedio: {1}".format(diccionario["nombre"], diccionario[clave1][clave2]))
        #es igual al 5 solo que en este caso elimine el primer jugador de la lista ya que es el que menor promedio tiene
        #porque la lista va de menor a mayor y el ejercicio pedia que elimine al que menor promedio tenia

    if(opcion == 17):
        clave1 = "logros"
        clave2 = None
        indice = mayor_cantidad(lista_jugadores, clave1, clave2)
        cantidad_de_logros = len(lista_jugadores[indice][clave1])
        jugador = lista_jugadores[indice]["nombre"]
        print("El jugador con mas logros es: {0}\tCon {1} logros".format(jugador, cantidad_de_logros))
        for logros in lista_jugadores[indice][clave1]:
            print(logros) 
        #busco el indice correspondiente al jugador con mas logro en la lsita jugadores y despues recorro los logros de ese jugador
        #para poder imprimirlos por pantalla

    if(opcion == 18):
        numero = input("Ingrese un porcentaje\n")
        flag = validar_0_a_100(numero)
        while(flag):
            numero = input("Ingrese nuevamente el porcentaje\n")
            flag = validar_0_a_100(numero)
        numero = float(numero)
        clave1 = "estadisticas"
        clave2 = "porcentaje_tiros_triples"
        lista_promedios = comparador_mayor_al_valor_ingresado(lista_jugadores, numero, clave1, clave2)
        
        for indice in lista_promedios:
            print("Jugador: {0}\t%{1}".format(lista_jugadores[indice]["nombre"], lista_jugadores[indice][clave1][clave2]))
        #igual al 10

    if(opcion == 19):
        clave1 = "estadisticas"
        clave2 = "temporadas"
        indice = mayor_cantidad(lista_jugadores, clave1, clave2)
        print("El jugador es: {0}\tTemporadas: {1}".format(lista_jugadores[indice]["nombre"], lista_jugadores[indice][clave1][clave2]))
        #igual al 7

    if(opcion == 20): 
        
        clave1 = "posicion"
        clave2 = None
        lista_jugadores_ordenada = ordenador_ascendente(lista_jugadores, clave1, clave2)
        clave1 = "estadisticas"
        clave2 = "porcentaje_tiros_de_campo"
        numero = input("Ingrese un porcentaje\n")
        flag = validar_0_a_100(numero)
        while(flag):
            numero = input("Ingrese nuevamente el porcentaje\n")
            flag = validar_0_a_100(numero)
        numero = float(numero)
        lista_indices = comparador_mayor_al_valor_ingresado(lista_jugadores_ordenada, numero, clave1, clave2)
        
        for indice in lista_indices:
            print("{0}: \t\tPosicion: {1}".format(lista_jugadores_ordenada[indice]["nombre"].capitalize(), lista_jugadores_ordenada[indice]["posicion"]))
        #este es una combiancion ya que primero ordeno la lista alfabeticamente y luego comparo quienes de esa lista tienen un  porcentaje mayor al que 
        # ingreso el usuario y guardo los indices de cada uno en otro lista, luego recorro la lista de indices e imprimo solamente los jugadores 
        # de la lista ordenada que se encuentren en la posicion del indice  

    if(opcion == 23):
        lista_aux_23 = ["jugador","Puntos","rebotes","asistencias","robos"]
        lista_csv_valores_23 = []
        clave1 = "estadisticas"
        lista_claves2 = ["puntos_totales","rebotes_totales","asistencias_totales","robos_totales"]
        clave3 = "nombre"
        #me genere una lista auxiliar que va a tener los encabezados para el csv y una lista de claves para hacer todo mas dinamico
        for diccionario in lista_jugadores:     
            nombre = diccionario["nombre"]      
            lista_csv_valores_23.append("\n{0}".format(nombre))
            #1) hago un for que recorra los nombres y de paso ya me guardo el nombre en la lista de valores del csv
            #la manera en la que ecribi el format es a proposito para que con cada nuevo nombre genere un salto de linea sin generarme un 
            #elemento nuevo porque estuve probando agregar luego del segundo for un \n y me quedaba una , adelante de cada linea y descubri que 
            #si usaba ; excel lo interpretaba como un salto de columna 

            for clave2 in lista_claves2:    #ordeno descendente segun la clave
                #recorro la lista de calves para hacer una lista que este ordenada de mayor a menor segun cada clave 
                lista_jugadores_ordenada_asc = ordenador_ascendente(lista_jugadores, clave1, clave2) 
                lista_jugadores_ordenada_des = list(reversed(lista_jugadores_ordenada_asc))
                #la funcion reversed lo que hace es invertir el orden de la lista que se le pasa por parametro, a esta lista invertida la transformo
                #en una nueva lista y la guardo dentro de la variable
                posicion = ranking_estadisticas(lista_jugadores_ordenada_des, clave3, nombre)     
                #luego con la funcion busco dentro de la lista ordenada de mayor a menor la posicion en la que se encuentra el jugador  
                lista_csv_valores_23.append(posicion)
                #y me guardo el indice

        #nota:        
        #los ; excel los reconoce como salto de columna pero me deja una , escrita
        #los \n entiende que son salto de fila pero me deja una , escrita
        
        generar_archivo_csv("Para el examen\{0}.csv".format("Bonus"), lista_csv_valores_23, lista_aux_23)
        #por ultimo genero el csv             

    if(opcion == 0):
        flag_while_menu = False


  
    
     