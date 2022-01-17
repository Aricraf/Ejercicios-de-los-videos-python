from typing import Match

opcion=0
def menu():
    opc= int(input("EJERCICIOS DEL VIDEO      \n " +
                   "32  AL 39               \n " +
                   "MENU PRINCIPAL            \n " +  
                   "1.- EJERCICIO NUMERO #32:    \n " +
                   "2.- EJERCICIO NUMERO #33:    \n " +
                   "3.- EJERCICIO NUMERO #34:    \n " +
                   "4.- EJERCICIO NUMERO #35:    \n " +
                   "5.- EJERCICIO NUMERO #35.1:  \n " +
                   "6.- EJERCICIO NUMERO #37:    \n " +
                   "7.- EJERCICIO NUMERO #38:    \n " +          
                   "8.- EJERCICIO NUMERO #38.1:  \n " +  
                   "9.- EJERCICIO NUMERO #38.2:  \n " +  
                   "10- EJERCICIO NUMERO #39:    \n " + 
                   "11- EJERCICIO NUMERO #39.1:  \n " +  
                   "12- EJERCICIO NUMERO #39.2:  \n " +  
                   
                    "ELIJA UNA OPCION:  "))
    return opc 
while opcion !=6:
    opcion = menu ()
    
    if opcion==1 :
        # A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
        # #  Finalizar al ingresar el número 0, el cual no debe guardarse.
        # # B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
        # # eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
        # # C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
        # # D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original 
        # # que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
        # # E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, 
        # # cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. 
        # # Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

        from funciones import*
        #1
        numeros=[]
        nro=int(input("Numero:  "))
        while nro!=0:
            numeros.append(nro)
            nro=int(input("Numeri: "))
         #2
        eliminar=int(input("Numero a eliminar:  "))   
        if eliminar in numeros:
            numeros.remove(eliminar)
        else:
            print("Ese numero no esta entre los ingresados")
        #3
        print("Sumatoria de los numeros: ", sumatoria(numeros))
        #4
        limite=int(input("Filtrar numeros menores a: "))
        for  n in numerosMenores(numeros, limite):
             print (n)
        #5
        print("Frecuencias: ")
        for tupla in frecuencias(numeros):
            print(tupla[0],"aparece", tupla[1], "veces")
            
    elif opcion==2:
        
        # Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas 
        # # con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), 
        # # ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, 
        # # "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. 
        # # Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), 
        # # ("Madrid","España")] Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
        # # -Agregar pasajeros a la lista de viajeros.
        # # -Agregar ciudades a la lista de ciudades.
        # # -Dado el DNI de un pasajero, ver a qué ciudad viaja.
        # # -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
        # # -Dado el DNI de un pasajero, ver a qué país viaja.
        # # -Dado un país, mostrar cuántos pasajeros viajan a ese país.
        # # -Salir del programa.
        from funciones import*
        pasajero=[ ]
        cuidad=[ ]
        while True:
            print("1.- Agregar pasajeros")
            print("2.- Agregar cuidades") 
            print("3.- Buscar cuidad destino ,ediante el DNI ")
            print("4.- Cantidad de pasajeros que viajaron a una cuidad")
            print("5.- Buscar pais destino mediante DNI ")
            print("6.- Cantidad de pasajeros que viajan a un pais") 
            print("7.- Salir del programa")
            opcion=int(input("Accion a ejecutar:  "))
            if opcion==1:
                print("AGREGAR PASAJEROS ")
                pasajeros=agregarPasajeros(pasajeros)
            elif opcion==2:
                print("AGREFAR CIUDADES") 
                cuidades=agregarCiudades(cuidad) 
            elif opcion==3:
                dni=int(input("DNI"))    
                print("El pasajero viajara a ", buscarCiudad(pasajeros,dni))
            elif opcion==4:
                cuidad=input("Ciudad")
                print("Viajan ", CantidadPasajerosCiudad(pasajeros,cuidad), "pasajeros")
            elif opcion==5:
                dni=int(input("NDI: "))
                print("Viaja a ", buscarPaisDestino(pasajeros,cuidades,dni))
            elif opcion==6:
                pais=input("pais: ")
                print("Viajan ", CantidadPasajerosPais(pasajeros,cuidades, pais), "pasajeros ")
            elif opcion==7:
                break    
            
    elif opcion==3:
        
        # Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, 
        # # finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, 
        # # finalizando al ingresar “x”.
        # # - Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.<>
        # # - Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
        # # -Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
        from funciones import*
        primaria=set()
        secundaria=set()
        print("ALUMNOS DE PRIMARIA")
        primaria=cargarNombres(primaria)
        print("ALUMNOS DE SECUNDARIA")
        secundaria=cargarNombres(secundaria)
        print("NOMBRES DE TODOS LOS ALUMNOS:")
        for nombre in primaria|secundaria:
             print(nombre)
             print("NOMBRES COMUNES:")
        for nombre in primaria&secundaria:
                print(nombre)
                 
                print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
        for nombre in primaria-secundaria:
                print(nombre)
                
    elif opcion==4:
        
        # Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, 
         # la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). 
         # # Ejemplo:[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), 
         # # ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
         # # ("Jorge Russo", 15, 958, "Mirasol 218")]
         # # Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente 
         # # y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. 
         # # Notar que cada cliente puede haber hecho más de una compra en el mes, por lo que la función 
         # # # debe retornar una estructura que contenga cada domicilio una sola vez.
       def direcciones(ventas):
           domicilios=set()
           for venta in ventas:
               domicilios.add(venta[3])
           return domicilios
       
    elif opcion==5:
        
        # Escribir un programa que procese strings ingresados por el usuario. 
        # # La lectura finaliza cuando se hayan procesado 50 strings. 
        # # Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. 
        # # Ejemplo: "r":5, "%":3, "a":8, "9":1.
        # # ¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, 
        # # incluyendo el valor 0 para las letras que no aparecieron?   
        contadores={}
        for i in range(50):
            cadena=input("Cadena de caracteres: ")
        for caracter in cadena:
            if caracter not in contadores:
                contadores[caracter]=1
            else:
                contadores[caracter]+=1
                print("Frecuencia de cada carácter")
        for caracter, cantidad in contadores.items():
            print(caracter, ": ", cantidad)

        #Para contabilizar sólo letras (mayúsculas y minúsculas por separado):
        contadores={}
        alfabeto="abcdefghijklmnñopqrstuvwxyz"
        for letra in alfabeto+alfabeto.upper():
            contadores[letra]=0
            for i in range(50):
                cadena=input("Cadena de caracteres: ")
            for caracter in cadena:
                if caracter.lower() in alfabeto:
                    contadores[caracter]+=1
                    print("Frecuencia de cada letra")
            for caracter, cantidad in contadores.items():
                 print(caracter, ": ", cantidad)
                 
    elif opcion==6:
        
        # Crear un programa para gestionar datos de los socios de un club, permitiendo:
        # # -Cargar información de los socios en un diccionario para acceder por número de socio. 
        # # Los datos a almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). 
        # # El programa debe iniciar con los datos de los socios fundadores ya cargados:
        # # # Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
        # # Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
        # # Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
        # # -Informar cantidad de socios del club.
        # # -Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
        # # -Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, 
        # para indicar que en realidad ingresaron el 14/03/2018.
        # # -Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
        # # -Imprimir el listado de socios completo.
        socios_activos={1:["Amanda Núñez","17032009",True], 2:["Bárbara Molina","17032009",True], 3:["Lautaro Campos","17032009",True]}
        
        print("***Cargar socios")
        socios_activos=cargarSocios(socios_activos)      
        
        print("El club tiene", len(socios_activos), "socios")
        
        print("***Registrar pago de cuotas") 
        numero=int(input("Número de socio: "))
        socios_activos[numero][2]=True

        print("***Modificando fecha de ingreso...")
        socios_activos=modificarFecha(socios_activos, "13032018", "14032018")

        print("***Eliminar socio")
        nombre=input("Nombre y apellido: ")
        numero=numeroSocio(socios_activos, nombre)
        if numero in socios_activos:
          def socios_activos(numero):
           imprimirListado(socios_activos)
           
    elif opcion==7:
        
        lista=[1, 2, 3, 4]
        for elemento in lista:
            print(elemento)
            articulos={ 154:["jabon en polvo", "limpieza", True],
            248: ["talco", "cosmetica", False],
            199: ["cera para pisos","limpieza", True] }
        for clave, valor in articulos.items():
                print("Codigo: ", clave)
                print("Descripcion: ", valor[0])
                print("Rubro; ", valor[1])
                if valor[2]:
                   print("Hay stock")
                else:
                  print("Agotado")
                  print("-------------")
                  
    elif opcion==8:
        
        lista =[1, 2, 3, 4, 4, 6, 7, 7, 8, 0, 9, 9, 9]

        for i in range(len(lista)-1):
            if lista[i]==lista[i+1]:
                print(lista[i])
                
    elif opcion==9:
        
        def empleadoExiste(empleados, nombre):
         for datos in empleados.values():
            if datos[0]==nombre:
                return True
         return False
         
        empleados= {100: ["Jorge Millán", "Administracion"],
                    200:["Oriana López", "Gerencia"],
                    300:["Guadalupe Ríos", "RR.HH"],
                    400:["Lionel Campos", "Ventas"]}
        
        nombre = input("Nombre de empleados: ")
        if not empleadoExiste(empleados,nombre):
            print("El empleado no se encuentra en la nómina")
                       
    elif opcion==10:
        
        alumnos= {"121-5": 42752983,
                  "243-9":  39234110,
                  "113-8:": 44922182,
                  "324-1": 39110245 }
        
        legajo= input("Legajo a buscar: ")
        if legajo in alumnos.keys():
            print("El DNI es: ", alumnos[legajo])
            
    elif opcion==11:
        
        def cargarDatos(diccionario):
            dni = int(input("DNI: "))
            while dni != 0:
                nombre = input("Nombre:" )
                domicilio = input("Domicilio:" )
                telefono = int(input("Telefono: " ))
                diccionario[dni]=[nombre, domicilio, telefono]
                dni= int(input("DNI: "))
                return diccionario

        def imprimirDatos (diccionario):
            for clave, valor in diccionario.items():
                print ("-DNI:",clave, "-Nombre:", valor[0], "-Domicilio:", valor[1], "-Telefono:", valor[2])

        clientes= { 44299132:["Gastón Quinteros", "Los Tilios 412", 582119721],
          38110223:["Valeria Gimenez", "Almendros 192",59912834],
          27918006:["Diego Linares", "Las Fresias 881", 51288390] }
        clientes= cargarDatos(clientes)
        imprimirDatos(clientes)
        
    elif opcion==12:
        
        def cargarMercaderias(mercaderias):
            articulo=[]
            codigo= int(input("codigo: "))
            while codigo !=0:
                descripcion=input("Descripcion: ")
                articulo.append(descripcion)
                rubro=input("Rubro: ")
                articulo.append(rubro)
                mercaderias[codigo]=articulo
                codigo=int(input("codigo: "))
                return mercaderias

            productos={}
            productos=cargarMercaderias(productos)
            for codigo, datos in productos.items():
                print(codigo, "-Descripcion: ", datos[0], "-Rubro", datos[1])
