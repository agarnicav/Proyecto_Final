from Circuitos import *
from Circuitos_solucionados import *
from Graficador import *
from colorama import init, Fore, Back, Style
import math


init()

def datosDeTension() -> dict:
    datosVoltajeAC = {}
    print(Fore.YELLOW+'INGRESE LOS DATOS DE LA FUENTE "V1"'+Fore.RESET)
    datos = {"Tensión":["la","Voltios"],"Frecuencia":["la","Herzios"],"Angulo":["el","grados"]}
    for i in datos:
        datosVoltajeAC[i] =  float(input('Ingrese {} {} en {}: '.format(datos[i][0], i, datos[i][1])))
    print("")
    return datosVoltajeAC

def datosDeResistencia() -> dict:
    datosResistencia = {}
    print(Fore.RED+'INGRESE LOS DATOS DE LA RESISTENCIA "R1"'+Fore.RESET)
    datosResistencia["Resistencia"] = float(input("Ingrese la resistividad en Ohmios: "))
    print("")
    return datosResistencia

def datosDeCondensador() -> dict:
    datosCondensador = {}
    print(Fore.GREEN+'INGRESE LOS DATOS DEL CONDENSADOR "C1"'+Fore.RESET)
    datosCondensador["Capacitancia"] = float(input("Ingrese la capacitancia en Micro Faradios: "))
    print("")
    return datosCondensador

def datosDeInductor() -> dict:
    datosInductor = {}
    print(Fore.BLUE+'INGRESE LOS DATOS DEL INDUCTOR "L1"'+Fore.RESET)
    datosInductor["Inductancia"] = float(input("Ingrese la inductancia en Henrios: "))
    print("")
    return datosInductor

def convertirFasores(datosCircuito:dict) -> dict:
    Xc = {}
    Xl = {}
    V = {"Tension":[datosCircuito["Tensión"],datosCircuito["Angulo"]]}
    R = {"Resistiva":[datosCircuito["Resistencia"],0]}
    for i in datosCircuito:
        if i == "Capacitancia":
            Xc = {"Capacitiva":[1/(2*math.pi*datosCircuito["Frecuencia"]*datosCircuito[i]*10**(-6)),-90]}
        elif i == "Inductancia":
            Xl = {"Inductiva":[2*math.pi*datosCircuito["Frecuencia"]*datosCircuito[i],90]}
    
    fasoresCircuito = dict(list(V.items())+list(R.items())+list(Xc.items())+list(Xl.items()))

    for i in fasoresCircuito: 
        if i == {}: fasoresCircuito.remove(i)
    
    return fasoresCircuito

def impedanciaEquivalente(fasores:dict,bandera:int) -> list: 
    if bandera == 1:
        magnitudZeq = math.sqrt(fasores["Resistiva"][0]**2 + fasores["Capacitiva"][0]**2)
        anguloZeq = math.degrees(math.atan(-fasores["Capacitiva"][0]/fasores["Resistiva"][0]))
    elif bandera == 2:
        magnitudZeq = math.sqrt(fasores["Resistiva"][0]**2 + fasores["Inductiva"][0]**2) 
        anguloZeq = math.degrees(math.atan(fasores["Inductiva"][0]/fasores["Resistiva"][0]))
    elif bandera == 3:
        magnitudZeq = math.sqrt(fasores["Resistiva"][0]**2 + (abs(fasores["Inductiva"][0] - fasores["Capacitiva"][0]))**2)
        anguloZeq = math.degrees(math.atan(abs(fasores["Inductiva"][0]-fasores["Capacitiva"][0])/fasores["Resistiva"][0]))
        if fasores["Capacitiva"] > fasores["Inductiva"]:
            anguloZeq *= -1
    
    Zeq = [magnitudZeq,anguloZeq]
    return Zeq

def leyDeOhm(impedancia:list,fasores:dict,banderas:int) -> dict:
    corrienteFasorial = {"Corriente":fasores["Tension"][0]/impedancia[0],"Angulo":fasores["Tension"][1]-impedancia[1]}
    tensionResistencia = {"TensionR":corrienteFasorial["Corriente"]*fasores["Resistiva"][0],"AnguloR":corrienteFasorial["Angulo"]+fasores["Resistiva"][1]}
    tensionCondensador = {}
    tensionInductor = {}
    if banderas == 1 or banderas == 3:
        tensionCondensador = {"TensionC":corrienteFasorial["Corriente"]*fasores["Capacitiva"][0],"AnguloC":corrienteFasorial["Angulo"]+fasores["Capacitiva"][1]}
    if banderas == 2 or banderas == 3:
        tensionInductor = {"TensionL":corrienteFasorial["Corriente"]*fasores["Inductiva"][0],"AnguloL":corrienteFasorial["Angulo"]+fasores["Inductiva"][1]}

    return corrienteFasorial,tensionResistencia,tensionCondensador,tensionInductor

if __name__ == "__main__":
    bandera : bool = True
    bandera2 : bool = True
    opcion : int = 0

    while bandera or opcion != 4:
        bandera = False
        bandera1 : bool = True 

        while bandera1 or opcion not in [1,2,3,4]:
            bandera1 = False
            print(Fore.RED+'####################################################\n#'+Fore.YELLOW+' ELIJA LA OPCIÓN DE CIRCUITO QUE DESEA SOLUCIONAR '+Fore.RED+'#\n####################################################'+Fore.RESET)
            opcion = int(input("1. CIRCUITO RC \n2. CIRCUITO RL \n3. CIRCUITO RLC \n4. SALIR \n"))

            if opcion not in [1,2,3,4]:
                print("\nLa opción digitada no es válida\n")

        match opcion:

            case 1:
                bandera = True
                opcion1 = 0
                print(RC)
                V1 = datosDeTension()
                R1 = datosDeResistencia()
                C1 = datosDeCondensador()
                datosCircuito = dict(list(V1.items()) + list(R1.items()) + list(C1.items()))
                fasores = convertirFasores(datosCircuito)
                impedancia = impedanciaEquivalente(fasores,1)
                A, Tr, Tc, Tl = leyDeOhm(impedancia,fasores,1)
                I = "I(t) = {}*10^-3 sin({} t + {}°)".format(round(A["Corriente"]*10**3,2),V1["Frecuencia"],round(A["Angulo"],2))
                V = "V(t) = {} sin({} t + {}°)".format(round(V1["Tensión"],2),V1["Frecuencia"],round(V1["Angulo"],2))
                VR = "VR(t) = {} sin({} t + {}°)".format(round(Tr["TensionR"],2),V1["Frecuencia"],round(Tr["AnguloR"],2))
                VC = "VC(t) = {} sin({} t + {}°)".format(round(Tc["TensionC"],2),V1["Frecuencia"],round(Tc["AnguloC"],2))

                while bandera or opcion1 != 4:
                    bandera = False
                    bandera2 = True
                    
                    while bandera2 or opcion1 not in [1,2,3,4]:
                        bandera2 = False
                        print(Fore.LIGHTMAGENTA_EX+'======================================\n='+Fore.GREEN+' ELIJA LA OPCIÓN QUE DESEA IMPRIMIR '+Fore.LIGHTMAGENTA_EX+'=\n======================================'+Fore.RESET)
                        opcion1 = int(input("1. CIRCUITO SOLUCIONADO \n2. GRÁFICO DE LA CORRIENTE \n3. GRÁFICO DE LAS TENSIONES \n4. SALIR \n"))
                    
                        if opcion1 not in [1,2,3,4]:
                            print("\nLa opción digitada no es válida\n")
                    
                    match opcion1:
                    
                        case 1:
                            circuitoRC(V,VR,VC,I,R1["Resistencia"],C1["Capacitancia"])
                    
                        case 2:
                            graficadorI(round(A["Corriente"]*10**3,2),V1["Frecuencia"],round(A["Angulo"],2))
                    
                        case 3:
                            graficadorRC(round(Tr["TensionR"],2),round(Tc["TensionC"],2),V1["Frecuencia"],round(Tr["AnguloR"],2),round(Tc["AnguloC"],2))
                    
                        case 4:
                            print()
                
                print("")
            
            case 2:
                bandera = True
                opcion2 = 0
                print(RL)
                V1 = datosDeTension()
                R1 = datosDeResistencia()
                L1 = datosDeInductor()
                datosCircuito = dict(list(V1.items()) + list(R1.items()) + list(L1.items()))
                fasores = convertirFasores(datosCircuito)
                impedancia = impedanciaEquivalente(fasores,2)
                A, Tr, Tc, Tl = leyDeOhm(impedancia,fasores,2)
                I = "I(t) = {}*10^-3 sin({} t + {}°)".format(round(A["Corriente"]*10**3,2),V1["Frecuencia"],round(A["Angulo"],2))
                V = "V(t) = {} sin({} t + {}°)".format(round(V1["Tensión"],2),V1["Frecuencia"],round(V1["Angulo"],2))
                VR = "VR(t) = {} sin({} t + {}°)".format(round(Tr["TensionR"],2),V1["Frecuencia"],round(Tr["AnguloR"],2))
                VL = "VL(t) = {} sin({} t + {}°)".format(round(Tl["TensionL"],2),V1["Frecuencia"],round(Tl["AnguloL"],2))
                
                while bandera or opcion2 != 4:
                    bandera = False
                    bandera2 = True

                    while bandera2 or opcion2 not in [1,2,3,4]:
                        bandera2 = False
                        print(Fore.LIGHTMAGENTA_EX+'======================================\n='+Fore.GREEN+' ELIJA LA OPCIÓN QUE DESEA IMPRIMIR '+Fore.LIGHTMAGENTA_EX+'=\n======================================'+Fore.RESET)
                        opcion2 = int(input("1. CIRCUITO SOLUCIONADO \n2. GRÁFICO DE LA CORRIENTE \n3. GRÁFICO DE LAS TENSIONES \n4. SALIR \n"))
                        
                        if opcion2 not in [1,2,3,4]:
                            print("\nLa opción digitada no es válida\n")

                    match opcion2:
                        
                        case 1:
                            circuitoRL(V,VR,VL,I,R1["Resistencia"],L1["Inductancia"])
                        
                        case 2:
                            graficadorI(round(A["Corriente"]*10**3,2),V1["Frecuencia"],round(A["Angulo"],2))
                        
                        case 3:
                            graficadorRL(round(Tr["TensionR"],2),round(Tl["TensionL"],2),V1["Frecuencia"],round(Tr["AnguloR"],2),round(Tl["AnguloL"],2))
                        
                        case 4:
                            print()

                print("")
            
            case 3:
                bandera = True
                opcion3 = 0
                print(RLC)
                V1 = datosDeTension()
                R1 = datosDeResistencia()
                L1 = datosDeInductor()
                C1 = datosDeCondensador()
                datosCircuito = dict(list(V1.items()) + list(R1.items()) + list(L1.items()) + list(C1.items()))
                fasores = convertirFasores(datosCircuito)
                impedancia = impedanciaEquivalente(fasores,3)
                A, Tr, Tc, Tl = leyDeOhm(impedancia,fasores,3)
                I = "I(t) = {}*10^-3 sin({} t + {}°)".format(round(A["Corriente"]*10**3,2),V1["Frecuencia"],round(A["Angulo"],2))
                V = "V(t) = {} sin({} t + {}°)".format(round(V1["Tensión"],2),V1["Frecuencia"],round(V1["Angulo"],2))
                VR = "VR(t) = {} sin({} t + {}°)".format(round(Tr["TensionR"],2),V1["Frecuencia"],round(Tr["AnguloR"],2))
                VL = "VL(t) = {} sin({} t + {}°)".format(round(Tl["TensionL"],2),V1["Frecuencia"],round(Tl["AnguloL"],2))
                VC = "VC(t) = {} sin({} t + {}°)".format(round(Tc["TensionC"],2),V1["Frecuencia"],round(Tc["AnguloC"],2))
                
                while bandera or opcion3 != 4:
                    bandera = False
                    bandera2 = True
                    
                    while bandera2 or opcion3 not in [1,2,3,4]:
                        bandera2 = False
                        print(Fore.LIGHTMAGENTA_EX+'======================================\n='+Fore.GREEN+' ELIJA LA OPCIÓN QUE DESEA IMPRIMIR '+Fore.LIGHTMAGENTA_EX+'=\n======================================'+Fore.RESET)
                        opcion3 = int(input("1. CIRCUITO SOLUCIONADO \n2. GRÁFICO DE LA CORRIENTE \n3. GRÁFICO DE LAS TENSIONES \n4. SALIR \n"))
                        
                        if opcion3 not in [1,2,3,4]:
                            print("\nLa opción digitada no es válida\n")
                            
                    match opcion3:
                        
                        case 1:
                            circuitoRLC(V,VR,VL,VC,I,R1["Resistencia"],L1["Inductancia"],C1["Capacitancia"])
                        
                        case 2:
                            graficadorI(round(A["Corriente"]*10**3,2),V1["Frecuencia"],round(A["Angulo"],2))
                        
                        case 3:
                            graficadorRLC(round(Tr["TensionR"],2),round(Tl["TensionL"],2),round(Tc["TensionC"],2),V1["Frecuencia"],round(Tr["AnguloR"],2),round(Tl["AnguloL"],2),round(Tc["AnguloC"],2))
                        
                        case 4:
                            print()

                print("")
            
            case 4:
                print("\nMuchas gracias")