from typing import Match

opcion=0
def menu():
    opc= int(input("EJERCICIOS DEL VIDEO      \n " +
                   "28  AL 31                 \n " +
                   "MENU PRINCIPAL            \n " +  
                   "1.- EJERCICIO NUMERO #28.1:  \n " +
                   "2.- EJERCICIO NUMERO #28.2:  \n " +
                   "3.- EJERCICIO NUMERO #29.1:  \n " +
                   "4.- EJERCICIO NUMERO #29.2:  \n " +
                   "5.- EJERCICIO NUMERO #29.3:  \n " +
                   "6.- EJERCICIO NUMERO #30:    \n " +
                   "7.- EJERCICIO NUMERO #31:    \n " +                   
                    "ELIJA UNA OPCION: "))
    return opc 
while opcion !=6:
    opcion = menu ()
    if opcion==1 :
        # sin ejecutar el siguiente programa determine cual es la salida en
        # # pantalla si se ingresa los valores x=6, y=7
        def coordenadaz (x,y):
          x=x+10
          y=y+15
          return x+y
        # programa principal 
        x= int(input("coordenada eje x:  "))
        y= int(input("coordenada eje y:  "))
        for i in range(3):
          z=coordenadaz(x,y)
          x=x+1
          y=y+1
          print(x," . ",y )    
    elif opcion ==2:
        def maximo(a,b):
            if x>y:
                return x 
            else :
                return y 
        def minimo (a,b):
            if x<y :
                return x
            else:
                return y 
        #progra,a principal 
        x=int(input("Un numeri:    "))               
        y=int(input("Otro numero:  "))  
        print(maximo(x-3, minimo(x+2, y-5)))
    elif opcion==3:
        def DNIvalido (dni):
            cantidad=0
            while dni!=0:
                cantidad=cantidad+1
                dni=dni//10
            return cantidad==7 or cantidad==8
    elif opcion==4:
        def lenUltimaPalabra(cadena):
            longitud=len(cadena)
            if longitud==0:
                return 0
            cantidad=0
            for i in range(longitud):
                if cadena[i] !=" ":
                    cantidad=cantidad+1
                else:
                    if cadena[i]==" " and i<(longitud-1) and cadena [i+1]!= " ":
              
                     return cantidad   
    elif opcion==5:
        from funciones import*
        nombre=input("Nombre del socio:    ")
        while nombre!="":
            dni=int(input("DNI del socio:  "))
            while not (DNIvalido(dni)):
                print("Numero invalido")
                dni= int(input("DNI DEL SOCIO: "))
            identificador=obtenerIdentificador(nombre,dni)
            print("El identificador del socio es: ", identificador)
            nombre=input("Nombre del socio:  ")
    elif opcion==6:
        menus=0
        def menus():
            menu= int(input("MENU PRINCIPAL       \n " +  
                   "1.- EJERCICIO NUMERO #30.1:  \n " +
                   "2.- EJERCICIO NUMERO #30.2:  \n " +
                   "3.- EJERCICIO NUMERO #30.1:  \n " +
                    "ELIJA UNA OPCION: "))
            return menu
        while menu !=3:
            munus=menu() 
            if menus==1:
                def titulo(cadena):
                    nueva="  "
                    inicioPalabra=True 
                for caracter in cadena:
                    if not caracter.isalpha():
                        nueva =nueva+caracter
                        inicioPalabra=True
                    else:
                        if inicioPalabra:
                            nueva=nueva+caracter.upper( )
                            inicioPalabra=False
                        else:
                           nueva=nueva+caracter.lower()
            elif menus==2:
                def titulo(cadena):
                    titulo('esto es una frase')
                    'Esto Es Una Frase'
                    titulo('ESTO ES UNA FRASE')
                    'Esto Es Una Frase'   
                    titulo('palabra')
                    'palabra' 
                    titulo('esto es una frase')
                    'Esto Es Una Frase'
                    titulo('esto es una frase')
                    'Esto Es Una Frase'
                    titulo('esto es una frase')
                    'Esto Es Una Frase'
                    titulo('  ')
                    '  '
                    titulo('  ')
                    '  '
                    titulo('123')
                    '123'
                    titulo('1esto 2es 3una 4frase')
                    '-1Esto 2Es 3Una 4Frase' 
                    titulo('1esto 2es 3una 4frase')
                    'Esto1 Es2 Una3 Frase4'       
            elif menus==3:
                class Pruebas(tesdtcase):
                    def tests_titulo(self):
                        self.assertEqual(titulo('esto es una frase'), "Esto Es Una Frase", "Error al convertir cadena ,minuscula")
                        self.assertEqual(titulo('ESTO ES UNA FRASE'), 'Esto Es Una Frase', )
                        self.assertEqual(titulo('palabra'),'palabra')
                        self.assertEqual(titulo('esto es una frase'),'Esto Es Una Frase')
                        self.assertEqual(titulo('esto es una frase'),'Esto Es Una Frase') 
                        self.assertEqual(titulo('esto es una frase'),'Esto Es Una Frase')  
                        self.assertEqual(titulo('  '), '  ') 
                        self.assertEqual(titulo('  '), '  ')
                        self.assertEqual(titulo('123'),'123')
                        self.assertEqual(titulo('1esto 2es 3una 4frase'),'-1Esto 2Es 3Una 4Frase' )
                        self.assertEqual(titulo('1esto 2es 3una 4frase'),"Esto1 Es2 Una3 Frase4")
    elif opcion==7:
         menus=0
         def menus():
            menu= int(input("MENU PRINCIPAL       \n " +  
                   "1.- EJERCICIO NUMERO #31.1:  \n " +
                   "2.- EJERCICIO NUMERO #31.2:  \n " +
                   "3.- EJERCICIO NUMERO #31.1:  \n " +
                    "ELIJA UNA OPCION: "))
            return menu
         while menu !=3:
            munus=menu() 
            if menus==1:
                lista=0
                for i in range (len(lista)):
                    print(lista[i])
                    
            elif opcion==2:
                i=0
                while i<len(lista):
                    print(lista[i])
                    i+=1
            elif opcion==3:
                for elemento in lista:
                    print(elemento)
                    