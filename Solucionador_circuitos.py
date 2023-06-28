from Circuitos import *
from Circuitos_solucionados import *
from Graficador import *
from colorama import init, Fore, Back, Style
import math


init() # Inicialización del módulo colorama


''' Se define la función para solicitar los datos de la Tensión '''

def datosDeTension() -> dict:  
    datosVoltajeAC = {}   # Se define el diccionario datosVoltajeAC  que alamacena los datos Tensión,Frecuencia y Ángulo
    print(Fore.YELLOW+'INGRESE LOS DATOS DE LA FUENTE "V1"'+Fore.RESET) # Se imprime el mensaje que le pide al usuario ingresar el valor que tendrá la fuente V1
    datos = {"Tensión":["la","Voltios"],"Frecuencia":["la","Herzios"],"Angulo":["el","grados"]} 
    '''Se define otro diccionario llamado datos que contiene la información para solicitar los datos al usuario. Cada clave del diccionario representa un tipo de dato (Tensión, Frecuencia, Ángulo), y los valores asociados son listas con información adicional sobre cómo solicitar los datos al usuario.'''
    
    ''' Se inicia un bucle for que recorre las claves del diccionario datos en el cual en cada iteración se pide al usuario ingresar los valores corresponedientes al tipo de dato '''
    for i in datos:   
        datosVoltajeAC[i] =  float(input('Ingrese {} {} en {}: '.format(datos[i][0], i, datos[i][1])))  # El valor ingresado se asigna al diccionario utilizando la clave correspondiente.
    print("")
    return datosVoltajeAC   # Se retorna el diccionario datosVoltacAC  que contendrá los datos ingresados


'''Se define la función para solicitar los datos de la resistencia  '''
def datosDeResistencia() -> dict:  
    datosResistencia = {}  # Se crea un diccionario vacío el cual alamacena el valor de la resistencia
    print(Fore.RED+'INGRESE LOS DATOS DE LA RESISTENCIA "R1"'+Fore.RESET)   # Se imprime un mensaje que indica ingresar los datos del resistencia "R1".
    datosResistencia["Resistencia"] = float(input("Ingrese la resistividad en Ohmios: "))   # El valor asignado a la resistencia  en Ohmios se asigna al diccionario datosResistencia con la clave "Resistencia".
    print("")
    return datosResistencia  # Se retorna el diccionario que contendrá el valor de la resistencia 


'''Se define la función para solicitar los datos de condensador   '''
def datosDeCondensador() -> dict:
    datosCondensador = {}  # Se crea un diccionario vacío el cual alamacena los datos del condensador 
    print(Fore.GREEN+'INGRESE LOS DATOS DEL CONDENSADOR "C1"'+Fore.RESET)  # Se imprime un mensaje que indica ingresar los datos del condensador "C1".
    datosCondensador["Capacitancia"] = float(input("Ingrese la capacitancia en Micro Faradios: ")) #  El valor ingresado en Micro Faradios  se asigna al diccionario datosCondensador con la clave "Capacitancia".
    print("")
    return datosCondensador # Se retorna el diccionario que contendrá los datos del condensador 


''' Se define la función para solicitar los datos del inductor  '''
def datosDeInductor() -> dict: 
    datosInductor = {} # Se crea un diccionario el cual almacenara los datos del inductor
    print(Fore.BLUE+'INGRESE LOS DATOS DEL INDUCTOR "L1"'+Fore.RESET)  # Se imprime un mensaje que indica ingresar los datos del inductor "L1".
    datosInductor["Inductancia"] = float(input("Ingrese la inductancia en Henrios: ")) # El valor ingresado en hernios  se asigna al diccionario datosInductor con la clave "Inductancia".
    print("")
    return datosInductor # Se retorna el diccionario que contendrá los datos del inductor



''' Se define la función convertirFasores() toma un diccionario datosCircuito que contiene los datos de un circuito (la tensión, resistencia, capacitancia, inductancia)  y realiza la conversión a fasores.'''

def convertirFasores(datosCircuito:dict) -> dict:  
    
    ''' se crean  dos diccionarios vacios el diccionario Xc almacenara el valor de los fasores del capacitor, el diccionario Xl almacenara los fasores del inductor'''
    Xc = {} 
    Xl = {} 
    V = {"Tension":[datosCircuito["Tensión"],datosCircuito["Angulo"]]}  # Se crea un diccionario que contiene  el fasor correspondiente a la tensión del circuito. El fasor de tensión se construye utilizando los valores de Tensión y Angulo del diccionario datosCircuito.
    R = {"Resistiva":[datosCircuito["Resistencia"],0]} #  Se crea un diccionario R que contiene el fasor correspondiente a la resistencia del circuito. El fasor de resistencia se construye utilizando el valor de Resistencia del diccionario datosCircuito y se establece la componente imaginaria en 0.
   
    ''' Se recorre el diccionario datosCircuito para buscar las claves "Capacitancia" e "Inductancia". 
    Si se encuentra la clave "Capacitancia", se calcula el fasor de la capacitancia utilizando la fórmula 1 / (2 * pi * frecuencia * capacitancia * 10^(-6)) y se establece la componente imaginaria en -90 (correspondiente a "j"). 
    Si se encuentra la clave "Inductancia", se calcula el fasor de la inductancia utilizando la fórmula 2 * pi * frecuencia * inductancia y se establece la componente imaginaria en 90.  ''' 
    
    for i in datosCircuito:  
        if i == "Capacitancia": 
            Xc = {"Capacitiva":[1/(2*math.pi*datosCircuito["Frecuencia"]*datosCircuito[i]*10**(-6)),-90]} 
        elif i == "Inductancia":
            Xl = {"Inductiva":[2*math.pi*datosCircuito["Frecuencia"]*datosCircuito[i],90]}   
    
    fasoresCircuito = dict(list(V.items())+list(R.items())+list(Xc.items())+list(Xl.items())) #  Se crea un diccionario fasoresCircuito que combina todos los diccionarios que almacenan los fasores calculados anteriormente.
    
    ''' Se recorre el diccionario fasoresCircuito y se eliminan aquellos fasores que tengan un valor de diccionario vacío {}.''' 
    for i in fasoresCircuito: 
        if i == {}: fasoresCircuito.remove(i)
    
    return fasoresCircuito # Se retorna el diccionario fasoresCircuito que contiene los fasores correspondientes a los componentes del circuito.


''' Se define la función Impedancia equivalente la cual toma dos argumentos: fasores (diccionario que contiene los fasores de los componentes del circuito) y bandera, que es un entero que indica el caso de circuitos que se desea realizar.'''
def impedanciaEquivalente(fasores:dict,bandera:int) -> list: 
    if bandera == 1:   # Si la bandera es igual a 1 (circuito RC), se realiza una combinación de resistencia y capacitancia.
        magnitudZeq = math.sqrt(fasores["Resistiva"][0]**2 + fasores["Capacitiva"][0]**2) # Se calcula la magnitud de la impedancia equivalente utilizando la fórmula de la hipotenusa, se forma un triagulo rectángulo formado por las componentes real e imaginaria de los fasores de resistencia y capacitancia. 
        anguloZeq = math.degrees(math.atan(-fasores["Capacitiva"][0]/fasores["Resistiva"][0])) # El ángulo de la impedancia equivalente se calcula utilizando la función math.atan() para obtener el ángulo resultante del cociente entre las componentes imaginaria y real de los fasores de capacitancia y resistencia.
    elif bandera == 2:  # Si la bandera es igual a 2 (circuito RL), se realiza una combinación de resistencia e inductancia.
        magnitudZeq = math.sqrt(fasores["Resistiva"][0]**2 + fasores["Inductiva"][0]**2)  # Se calcula la magnitud de la impedancia equivalente utilizando la fórmula de la hipotenusa, se forma un triagulo rectángulo formado por las componentes real e imaginaria de los fasores de resistencia e inductancia. 
        anguloZeq = math.degrees(math.atan(fasores["Inductiva"][0]/fasores["Resistiva"][0]))  # El ángulo de la impedancia equivalente se calcula utilizando la función math.atan() para obtener el ángulo resultante del cociente entre las componentes imaginaria y real de los fasores de inductancia y resistencia.
    elif bandera == 3: # Si la bandera es igual a 3 (circuito RLC), se realiza una combinación de resistencia e inductancia.
        magnitudZeq = math.sqrt(fasores["Resistiva"][0]**2 + (abs(fasores["Inductiva"][0] - fasores["Capacitiva"][0]))**2) # Se calcula la magnitud de la impedancia equivalente utilizando la fórmula de la hipotenusa, se forma un triángulo rectángulo formado por las componentes real e imaginaria de los fasores de resistencia, inductancia y capacitancia. 
        anguloZeq = math.degrees(math.atan(abs(fasores["Inductiva"][0]-fasores["Capacitiva"][0])/fasores["Resistiva"][0])) # El ángulo se calcula utilizando la función math.atan(), usando el valor absoluto de la diferencia entre la componente imaginaria de los fasores de inductancia y capacitancia dividido por la componente real de la resistencia. 
        
        ''' Si la capacitancia es mayor que la inductancia, se multiplica el ángulo resultante por -1. '''
        if fasores["Capacitiva"] > fasores["Inductiva"]:
            anguloZeq *= -1
    
    Zeq = [magnitudZeq,anguloZeq]  # Se crea una lista Zeq que contiene la magnitud y el ángulo de la impedancia equivalente.
    return Zeq  # Se retorna la lista Zeq, que representa la impedancia equivalente del circuito.


''' Se define función leyDeOhm la cual toma tres argumentos: impedancia (lista que contiene la magnitud y el ángulo de la impedancia del circuito), fasores ( diccionario que contiene los fasores de los componentes del circuito) y banderas.'''
def leyDeOhm(impedancia:list,fasores:dict,banderas:int) -> dict:
    corrienteFasorial = {"Corriente":fasores["Tension"][0]/impedancia[0],"Angulo":fasores["Tension"][1]-impedancia[1]}    # Se calcula la corriente fasorial dividiendo la amplitud de la tensión entre la amplitud de la impedancia, y se restan el ángulo de la impedancia con el ángulo de la tensión. El resultado se almacena en el diccionario corrienteFasorial. 
    tensionResistencia = {"TensionR":corrienteFasorial["Corriente"]*fasores["Resistiva"][0],"AnguloR":corrienteFasorial["Angulo"]+fasores["Resistiva"][1]}  # Se calcula la tensión en la resistencia multiplicando la corriente fasorial por la amplitud de la resistencia, y se suman el ángulo de la corriente fasorial con el ángulo de la resistencia. El resultado se almacena en el diccionario tensionResistencia.
    tensionCondensador = {}
    tensionInductor = {}
    if banderas == 1 or banderas == 3:  # Si la bandera es igual a 1 o 3, indica que en el circuito hay un condensador  
        tensionCondensador = {"TensionC":corrienteFasorial["Corriente"]*fasores["Capacitiva"][0],"AnguloC":corrienteFasorial["Angulo"]+fasores["Capacitiva"][1]} # Se calcula la tensión en el condensador multiplicando la corriente fasorial por la amplitud del condensador, y se suma el ángulo de la corriente fasorial al ángulo del condensador. El resultado se almacena en el diccionario tensionCondensador. 
    if banderas == 2 or banderas == 3: # Si la bandera es igual a 2 o 3, indica que en el circuito hay un inductor
        tensionInductor = {"TensionL":corrienteFasorial["Corriente"]*fasores["Inductiva"][0],"AnguloL":corrienteFasorial["Angulo"]+fasores["Inductiva"][1]} # Se calcula la tension del inductor multiplicando la corriente fasorial por la amplitud del inductor, y se suma el ángulo de la corriente fasorial al ángulo del inductor. EL resultado se almacena en el diccionario tensionInductor.

    return corrienteFasorial,tensionResistencia,tensionCondensador,tensionInductor   # se devuelven 4 diccionarios que contienen la magnitud y el ángulo de la corriente fasorial, la tensión en la resistencia, la tensión en el condensador (si está presente) y la tensión en el inductor (si está presente).

''' Se define la función principal if __name__ == "__main__":  
Se definen variables booleanas (bandera, bandera1, bandera2) y una variable entera (opcion) con valores iniciales. 
Estas variables se utilizan para controlar los bucles y las opciones del menú.

'''
if __name__ == "__main__":  
    bandera : bool = True
    bandera2 : bool = True
    opcion : int = 0
 
    while bandera or opcion != 4:    # Se crea un bucle principal que se ejecuta mientras bandera sea verdadera o hasta que la opción seleccionada sea 4 (SALIR).
        bandera = False 
        bandera1 : bool = True 

        while bandera1 or opcion not in [1,2,3,4]: 
            bandera1 = False  # bandera1 se establece en falso para evitar que se ejecute el bucle interno.
            '''Se muestra un menú con las opciones de circuito disponibles'''
            print(Fore.RED+'####################################################\n#'+Fore.YELLOW+' ELIJA LA OPCIÓN DE CIRCUITO QUE DESEA SOLUCIONAR '+Fore.RED+'#\n####################################################'+Fore.RESET)
            opcion = int(input("1. CIRCUITO RC \n2. CIRCUITO RL \n3. CIRCUITO RLC \n4. SALIR \n"))   # Al ingresar un numero entero que representa la opcion elegida, se almacena en la variable opcion.

            if opcion not in [1,2,3,4]: #  Si la opción no coincide con las opciones 1,2,30 4 , se muestra un mensaje de error (" la opxión digitada no es valida")
                print("\nLa opción digitada no es válida\n")
            
        ''' Si la opción no es válida, la bandera1 permanece en falso y el bucle se repite, volviendo a mostrar el menú y solicitando al usuario que ingrese una opción válida.'''



        ''' Se utiliza la declaración match para evaluar el valor de la opcion que se obtiene al elegir una opción del menú principal.  '''
        match opcion:
            
            # Si la opcion elegida es igual a 1, se ejecuta el codigo del primer caso RC.  
            case 1:  
                bandera = True  # Se establece la variable bandera en verdadero
                opcion1 = 0     # se inicializan las variables opcion1 en 0
                print(RC) # Se imprime el ejemplo de circuiro RC
                
                 
                # Se solicitan los datos para el circuito RC, utilizando las funciones establecidas anteriormente 
                V1 = datosDeTension() 
                R1 = datosDeResistencia() 
                C1 = datosDeCondensador()
                datosCircuito = dict(list(V1.items()) + list(R1.items()) + list(C1.items())) # Los datos ingresados se guardan y se combinan en el diccionario datosCircuito.
                fasores = convertirFasores(datosCircuito)  # Se llama a la función ConvertirFasores y se le a de argumentos el diccionario datos circuitos
                impedancia = impedanciaEquivalente(fasores,1) # Se llama a la función impedanciaEquivalente y se le asignan los argumentos Fasores y 1 que hace refetencia a la bandera
                A, Tr, Tc, Tl = leyDeOhm(impedancia,fasores,1) # Se llama a la función leyDeOhm y se le asiganan los argumenos Impendacia, Fasores y 1, La función leyDeOhm devuelve cuatro valores: A, Tr, Tc y Tl.
                
                ''' Se utilizan estos valores A, Tr, Tc, Tl para crear representaciones en cadena de caracteres de las corrientes y tensiones en función del tiempo, Los valores se redondean a 2 decimales antes de ser insertados en las cadenas mediante el método format.'''
                I = "I(t) = {}*10^-3 sin({} t + {}°)".format(round(A["Corriente"]*10**3,2),V1["Frecuencia"],round(A["Angulo"],2))
                V = "V(t) = {} sin({} t + {}°)".format(round(V1["Tensión"],2),V1["Frecuencia"],round(V1["Angulo"],2))
                VR = "VR(t) = {} sin({} t + {}°)".format(round(Tr["TensionR"],2),V1["Frecuencia"],round(Tr["AnguloR"],2))
                VC = "VC(t) = {} sin({} t + {}°)".format(round(Tc["TensionC"],2),V1["Frecuencia"],round(Tc["AnguloC"],2))
                
                   
                '''  Se generan las representaciones en cadena de caracteres para la corriente y las tensiones en función del tiempo (I, V, VR, VC).
                
            Se ejecuta un bucle while que se repetirá mientras la bandera sea verdadera o la  opcion1 no sea igual a 4.
            Este bucle se utiliza para mostrar el menú de opciones y ejecutar el código correspondiente a la opción seleccionada. '''
                while bandera or opcion1 != 4:
                    bandera = False
                    bandera2 = True
                    
                    ''' Dentro del bucle, se muestra el menú de opciones y en la cual se solicita elegir una opción. 
                    El valor ingresado se convierte a entero y se almacena en la variable opcion1. '''
                    while bandera2 or opcion1 not in [1,2,3,4]:
                        bandera2 = False
                        print(Fore.LIGHTMAGENTA_EX+'======================================\n='+Fore.GREEN+' ELIJA LA OPCIÓN QUE DESEA IMPRIMIR '+Fore.LIGHTMAGENTA_EX+'=\n======================================'+Fore.RESET)
                        opcion1 = int(input("1. CIRCUITO SOLUCIONADO \n2. GRÁFICO DE LA CORRIENTE \n3. GRÁFICO DE LAS TENSIONES \n4. SALIR \n"))
                    
                        if opcion1 not in [1,2,3,4]:
                            print("\nLa opción digitada no es válida\n")
                            
                    
                    ''' Se utiliza match para evaluar el valor de opcion1 y ejecutar el código correspondiente a cada caso:'''
                    match opcion1:
                        # Si opcion1 es igual a 1, se llama a la función circuitoRC pasando como argumentos las representaciones en cadena de caracteres de las variables V, VR, VC, I, R1 y C1.
                        case 1:
                            circuitoRC(V,VR,VC,I,R1["Resistencia"],C1["Capacitancia"])  # Se muestra el circuito con los valores ingresados y la solucíon 
                    
                        # Si opcion1 es igual a 2, se llama a la función graficadorI pasando como argumentos la corriente máxima, la frecuencia y el ángulo de la corriente.
                        case 2:
                            graficadorI(round(A["Corriente"]*10**3,2),V1["Frecuencia"],round(A["Angulo"],2)) # Se muestra el Grafico de corriente 
                    
                        # Si opcion1 es igual a 3, se llama a la función graficadorRC pasando como argumentos las tensiones en el resistor y el condensador, la frecuencia, y los ángulos correspondientes.
                        case 3:
                            graficadorRC(round(Tr["TensionR"],2),round(Tc["TensionC"],2),V1["Frecuencia"],round(Tr["AnguloR"],2),round(Tc["AnguloC"],2)) # Se muestra el grafico de tensiones 
                    
                
                        # Si opcion1 es igual a 4, no se ejecuta ninguna acción adicional 
                        case 4:
                            print() # Se imprime una línea en blanco.
                
                print("")
                
            
            # Si la opcion elegida es igual a 2, se ejecuta el codigo del segundo caso RL.  
            case 2:
            
                bandera = True # Se establece la variable bandera en verdadero
                opcion2 = 0  # se inicializan las variables opcion2 en 0
                print(RL) # Se imprime el ejemplo de circuiro RL
                
                
                # Se solicitan los datos para el circuito RL, utilizando las funciones establecidas anteriormente 
                V1 = datosDeTension()
                R1 = datosDeResistencia()
                L1 = datosDeInductor()
                datosCircuito = dict(list(V1.items()) + list(R1.items()) + list(L1.items())) # Los datos ingresados se guardan y se combinan en el diccionario datosCircuito.
                fasores = convertirFasores(datosCircuito) # Se llama a la función ConvertirFasores y se le a de argumentos el diccionario datos circuitos
                impedancia = impedanciaEquivalente(fasores,2) # Se llama a la función impedanciaEquivalente y se le asignan los argumentos Fasores y 2  que hace refetencia a la bandera
                A, Tr, Tc, Tl = leyDeOhm(impedancia,fasores,2) # Se llama a la función leyDeOhm y se le asiganan los argumenos Impendacia, Fasores y 2, La función leyDeOhm devuelve cuatro valores: A, Tr, Tc y Tl.
                
                ''' Se utilizan estos valores A, Tr, Tc, Tl para crear representaciones en cadena de caracteres de las corrientes y tensiones en función del tiempo, Los valores se redondean a 2 decimales antes de ser insertados en las cadenas mediante el método format.'''
                I = "I(t) = {}*10^-3 sin({} t + {}°)".format(round(A["Corriente"]*10**3,2),V1["Frecuencia"],round(A["Angulo"],2))
                V = "V(t) = {} sin({} t + {}°)".format(round(V1["Tensión"],2),V1["Frecuencia"],round(V1["Angulo"],2))
                VR = "VR(t) = {} sin({} t + {}°)".format(round(Tr["TensionR"],2),V1["Frecuencia"],round(Tr["AnguloR"],2))
                VL = "VL(t) = {} sin({} t + {}°)".format(round(Tl["TensionL"],2),V1["Frecuencia"],round(Tl["AnguloL"],2))
                
                '''  Se generan las representaciones en cadena de caracteres para la corriente y las tensiones en función del tiempo (I, V, VR, VL).
                
            Se ejecuta un bucle while que se repetirá mientras la bandera sea verdadera o la  opcion2 no sea igual a 4.
            Este bucle se utiliza para mostrar el menú de opciones y ejecutar el código correspondiente a la opción seleccionada. '''
                
                while bandera or opcion2 != 4:
                    bandera = False
                    bandera2 = True
                    
                    ''' Dentro del bucle, se muestra el menú de opciones y en la cual se solicita elegir una opción. 
                    El valor ingresado se convierte a entero y se almacena en la variable opcion2. '''
                    while bandera2 or opcion2 not in [1,2,3,4]:
                        bandera2 = False
                        print(Fore.LIGHTMAGENTA_EX+'======================================\n='+Fore.GREEN+' ELIJA LA OPCIÓN QUE DESEA IMPRIMIR '+Fore.LIGHTMAGENTA_EX+'=\n======================================'+Fore.RESET)
                        opcion2 = int(input("1. CIRCUITO SOLUCIONADO \n2. GRÁFICO DE LA CORRIENTE \n3. GRÁFICO DE LAS TENSIONES \n4. SALIR \n"))
                        
                        if opcion2 not in [1,2,3,4]:
                            print("\nLa opción digitada no es válida\n")
                            
                    ''' Se utiliza match para evaluar el valor de opcion2 y ejecutar el código correspondiente a cada caso:'''
                    match opcion2:
                        
                        # Si opcion2 es igual a 1, se llama a la función circuitoRL pasando como argumentos las representaciones en cadena de caracteres de las variables V, VR, VL, I, R1 y L1.
                        case 1:
                            circuitoRL(V,VR,VL,I,R1["Resistencia"],L1["Inductancia"])
                            
                        # Si opcion2 es igual a 2, se llama a la función graficadorI pasando como argumentos la corriente máxima, la frecuencia y el ángulo de la corriente.
                        case 2:
                            graficadorI(round(A["Corriente"]*10**3,2),V1["Frecuencia"],round(A["Angulo"],2))  # Se muestra el grafico de corriente
                        
                        # Si opcion2 es igual a 3, se llama a la función graficadorRC pasando como argumentos las tensiones en el resistor y el inductor, la frecuencia, y los ángulos correspondientes.
                        case 3:
                            graficadorRL(round(Tr["TensionR"],2),round(Tl["TensionL"],2),V1["Frecuencia"],round(Tr["AnguloR"],2),round(Tl["AnguloL"],2)) # Se muestra el grafico de tensiones 
                            
                        # Si opcion1 es igual a 4, no se ejecuta ninguna acción adicional 
                        case 4:
                            print() # Se imprime una línea en blanco.
                        

                print("")
                
            # Si la opcion elegida es igual a 3, se ejecuta el codigo del tercer caso RLC.  
            case 3:
                bandera = True
                opcion3 = 0  # se inicializan las variables opcion3 en 0
                print(RLC) # Se imprime el ejemplo de circuiro RLC
                
                # Se solicitan los datos para el circuito RLC, utilizando las funciones establecidas anteriormente 
                V1 = datosDeTension()
                R1 = datosDeResistencia()
                L1 = datosDeInductor()
                C1 = datosDeCondensador()
                
            
                ''' Se utilizan estos valores A, Tr, Tc, Tl para crear representaciones en cadena de caracteres de las corrientes y tensiones en función del tiempo, Los valores se redondean a 2 decimales antes de ser insertados en las cadenas mediante el método format.'''
                datosCircuito = dict(list(V1.items()) + list(R1.items()) + list(L1.items()) + list(C1.items()))  # Los datos ingresados se guardan y se combinan en el diccionario datosCircuito.
                fasores = convertirFasores(datosCircuito)  # Se llama a la función ConvertirFasores y se le a de argumentos el diccionario datos circuitos
                impedancia = impedanciaEquivalente(fasores,3) # Se llama a la función impedanciaEquivalente y se le asignan los argumentos Fasores y 3 que hace refetencia a la bandera
                A, Tr, Tc, Tl = leyDeOhm(impedancia,fasores,3) # Se llama a la función leyDeOhm y se le asiganan los argumenos Impendacia, Fasores y 3, La función leyDeOhm devuelve cuatro valores: A, Tr, Tc y Tl.
                
                
                ''' Se utilizan estos valores A, Tr, Tc, Tl para crear representaciones en una cadena de caracteres de las corrientes y tensiones en función del tiempo, utilizando los valores obtenidos anteriormente. Los valores se formatean y se redondean qa 2 decimales para que sean legibles.'''
                I = "I(t) = {}*10^-3 sin({} t + {}°)".format(round(A["Corriente"]*10**3,2),V1["Frecuencia"],round(A["Angulo"],2))
                V = "V(t) = {} sin({} t + {}°)".format(round(V1["Tensión"],2),V1["Frecuencia"],round(V1["Angulo"],2))
                
                # VR, VL y VC Crean cadenas de caracteres representando las tensiones en la resistencia, inductor y condensador respectivamente, utilizando los valores obtenidos anteriormente.
                VR = "VR(t) = {} sin({} t + {}°)".format(round(Tr["TensionR"],2),V1["Frecuencia"],round(Tr["AnguloR"],2))
                VL = "VL(t) = {} sin({} t + {}°)".format(round(Tl["TensionL"],2),V1["Frecuencia"],round(Tl["AnguloL"],2))
                VC = "VC(t) = {} sin({} t + {}°)".format(round(Tc["TensionC"],2),V1["Frecuencia"],round(Tc["AnguloC"],2)) 
                
                
                '''  Se generan las representaciones en cadena de caracteres para la corriente y las tensiones en función del tiempo (I, V, VR, VL,VC).
                
            Se ejecuta un bucle while que se repetirá mientras la bandera sea verdadera o la  opcion3 no sea igual a 4.
            Este bucle se utiliza para mostrar el menú de opciones y ejecutar el código correspondiente a la opción seleccionada. '''
                
                while bandera or opcion3 != 4:
                    bandera = False
                    bandera2 = True
                    
                    ''' Dentro del bucle, se muestra el menú de opciones y en la cual se solicita elegir una opción. 
                    El valor ingresado se convierte a entero y se almacena en la variable opcion3. '''
                    while bandera2 or opcion3 not in [1,2,3,4]:
                        bandera2 = False
                        print(Fore.LIGHTMAGENTA_EX+'======================================\n='+Fore.GREEN+' ELIJA LA OPCIÓN QUE DESEA IMPRIMIR '+Fore.LIGHTMAGENTA_EX+'=\n======================================'+Fore.RESET)
                        opcion3 = int(input("1. CIRCUITO SOLUCIONADO \n2. GRÁFICO DE LA CORRIENTE \n3. GRÁFICO DE LAS TENSIONES \n4. SALIR \n"))
             
                        if opcion3 not in [1,2,3,4]:
                            print("\nLa opción digitada no es válida\n")
                            
                    ''' Se utiliza match para evaluar el valor de opcion3 y ejecutar el código correspondiente a cada caso:'''
                    match opcion3:
                        # Si opcion3 es igual a 1, se llama a la función circuitoRLC pasando como argumentos las representaciones en cadena de caracteres de las variables V, VR, VL, I, R1, L1 y C1.
                        case 1:
                            circuitoRLC(V,VR,VL,VC,I,R1["Resistencia"],L1["Inductancia"],C1["Capacitancia"]) 
                            
                        # Si opcion3 es igual a 2, se llama a la función graficadorI pasando como argumentos la corriente máxima, la frecuencia y el ángulo de la corriente.
                        case 2:
                            graficadorI(round(A["Corriente"]*10**3,2),V1["Frecuencia"],round(A["Angulo"],2)) # Se muestra el grafico de corriente
                        
                        # Si opcion3 es igual a 3, se llama a la función graficadorRLC pasando como argumentos las tensiones en el resistor,el inductor y el capacior, la frecuencia, y los ángulos correspondientes.
                        case 3:
                            graficadorRLC(round(Tr["TensionR"],2),round(Tl["TensionL"],2),round(Tc["TensionC"],2),V1["Frecuencia"],round(Tr["AnguloR"],2),round(Tl["AnguloL"],2),round(Tc["AnguloC"],2)) # Se muestra el grafico de tensiones 
                        
                        
                        # Si opcion3 es igual a 4, no se ejecuta ninguna acción adicional 
                        case 4:
                            print() # Se imprime una línea en blanco.
                       
                print("")
            
            # Si la opcion elegida es igual a 4, se ejecuta el codigo del 4 caso en el cual se ejecuta un mensaje de despedida y se finaliza el programa
            case 4:
                print("\nMuchas gracias")
