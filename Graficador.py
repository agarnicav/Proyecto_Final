import plotext  
import math

''' Se define la función graficadorRC:
La cual se encarga de graficar las tensiones en un circuito RC. Recibe como argumentos la amplitud A y A1, la frecuencia F, el ángulo de fase AG y AG1. 
Se utiliza la biblioteca plotext para generar los gráficos.'''

def graficadorRC(A,A1,F,AG,AG1):

    l = int(F)  # Se convierte la frecuencia F a un numero entero y se almacena en l
    x = range(0, l+1) # Se crea un rango de valores en el eje x que va desde 0 hasta l+1
    frames = 50 # Establece el número de fotogramas que se utilizarán para la animación. En este caso, se han definido 50 fotogramas.

    plotext.title("Tensiones Circuito RC") # Se esablece el título del gráfico "Tensiones Circuito RC" 
    plotext.clc()  # Borra la pantalla del gráfico anterior, si lo hay.
    
    
    ''' Se inicia un bucle que itera a través de los fotogramas, cada iteración del bucle representa un fotograma de la animación.'''
    for i in range(frames): 
        plotext.clt() # Borra el contenido de la terminal, eliminando cualquier texto o gráfico previamente mostrado 
        plotext.cld()  # Borra la información de datos relativa a la subgráfica activa

        ''' y Calcula los valores de la función seno con una amplitud A, un número de periodos F, una longitud l y un desplazamiento de fase (2 * i / frames)-math.radians(AG). 
        Estos valores representan la forma de onda de la tensión VR(t) en el circuito RC. '''
        y = plotext.sin(amplitude=A, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG))
        
        ''' y1 Calcula los valores de la función seno con una amplitud A1, un número de periodos F, una longitud l y un desplazamiento de fase (2 * i / frames)-math.radians(AG1). 
        Estos valores representan la forma de onda de la tensión VC(t) en el circuito RC'''
        y1 = plotext.sin(amplitude=A1, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG1))
        
        ''' plotext.plot Traza los puntos en el gráfico utilizando los valores de "x " y "y " 
        Se define el marcado con "dot" (punto), color (color que representar  el trazo de los puntos de la tensión). Y una etiqueta "VR(t),VC(t)" al trazado.'''
        plotext.plot(x, y, marker="dot", color="red",label="VR(t)")
        plotext.plot(x, y1, marker="dot", color="green",label="VC(t)")
        
        ''' plotext.sleep  Pausa la ejecución del programa durante 0.1 segundos para controlar la velocidad de la animación.'''
        plotext.sleep(0.1)
        plotext.show()
        
    ''' plotext.clear_plot(): Borra el gráfico después de que se completan todos los fotogramas de la animación.'''
    plotext.clear_plot() 
    

''' Se define la función graficadorRL:
La cual se encarga de graficar las tensiones en un circuito RL. Recibe como argumentos la amplitud A y A1, la frecuencia F, el ángulo de fase AG y AG1.'''
def graficadorRL(A,A1,F,AG,AG1):
    
    l = int(F)  # Se convierte la frecuencia F a un numero entero y se almacena en l
    x = range(0, l+1) # Se crea un rango de valores en el eje x que va desde 0 hasta l+1
    frames = 50 # Establece el número de fotogramas que se utilizarán para la animación. En este caso, se han definido 50 fotogramas.


    plotext.title("Tensiones Circuito RL") # Se esablece el título del gráfico "Tensiones Circuito RL" 
    plotext.clc() # Borra la pantalla del gráfico anterior, si lo hay, utilizando la función clc 
    
    ''' Se inicia un bucle que itera a través de los fotogramas, cada iteración del bucle representa un fotograma de la animación.'''
    for i in range(frames):
        
        plotext.clt() 
        plotext.cld() 

        ''' y Calcula los valores de la función seno con una amplitud A, un número de periodos F, una longitud l y un desplazamiento de fase (2 * i / frames)-math.radians(AG). 
        Estos valores representan la forma de onda de la tensión VR(t) en el circuito RL. '''
        y = plotext.sin(amplitude=A, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG))
        ''' y1 Calcula los valores de la función seno con una amplitud A1, un número de periodos F, una longitud l y un desplazamiento de fase (2 * i / frames)-math.radians(AG1). 
        Estos valores representan la forma de onda de la tensión VC(t) en el circuito RL'''
        y1 = plotext.sin(amplitude=A1, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG1))
        
        ''' plotext.plot Traza los puntos en el gráfico utilizando los valores de "x " y "y " 
        Se define el marcado con "dot" (punto), color (color que representar  el trazo de los puntos de la tensión). Y una etiqueta "VR(t),VL(t)" al trazado.'''
        plotext.plot(x, y, marker="dot", color="red",label="VR(t)")
        plotext.plot(x, y1, marker="dot", color="blue",label="VL(t)")
        
        ''' plotext.sleep  Pausa la ejecución del programa durante 0.1 segundos para controlar la velocidad de la animación.'''
        plotext.sleep(0.1)
        plotext.show()
        
    ''' plotext.clear_plot(): Borra el gráfico después de que se completan todos los fotogramas de la animación.'''
    plotext.clear_plot()
    
    
''' Se define la función graficadorRLC:
La cual se encarga de graficar las tensiones en un circuito RLC. Recibe como argumentos la amplitud A, A1 y A2, la frecuencia F, el ángulo de fase AG AG1y AG2.'''    
def graficadorRLC(A,A1,A2,F,AG,AG1,AG2):
    
    l = int(F)  # Se convierte la frecuencia F a un numero entero y se almacena en l
    x = range(0, l+1) # Se crea un rango de valores en el eje x que va desde 0 hasta l+1
    frames = 50 # Establece el número de fotogramas que se utilizarán para la animación. En este caso, se han definido 50 fotogramas.


    plotext.title("Tensiones Circuito RLC") # Se esablece el título del gráfico "Tensiones Circuito RLC" 
    plotext.clc() # Borra la pantalla del gráfico anterior, si lo hay, utilizando la función clc 
    
    ''' Se inicia un bucle que itera a través de los fotogramas, cada iteración del bucle representa un fotograma de la animación.'''
    for i in range(frames):
        plotext.clt() 
        plotext.cld() 
        
        ''' y Calcula los valores de la función seno con una amplitud A, un número de periodos F, una longitud l y un desplazamiento de fase (2 * i / frames)-math.radians(AG). 
        Estos valores representan la forma de onda de la tensión VR(t) en el circuito RLC. '''
        y = plotext.sin(amplitude=A, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG))
        
        '''y1 Calcula los valores de la función seno con una amplitud A1, un número de periodos F, una longitud l y un desplazamiento de fase (2 * i / frames)-math.radians(AG1).
        Estos valores representan la forma de onda de la tensión VL(t) en el circuito RLC.'''
        y1 = plotext.sin(amplitude=A1, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG1))
        
        ''' y2 Calcula los valores de la función seno con una amplitud A2, un número de periodos F, una longitud l y un desplazamiento de fase (2 * i / frames)-math.radians(AG2). 
        Estos valores representan la forma de onda de la tensión VC(t) en el circuito RLC.'''
        y2 = plotext.sin(amplitude=A2, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG2))
        
        ''' plotext.plot Traza los puntos en el gráfico utilizando los valores de "x " y "y " 
        Se define el marcado con "dot" (punto), color (color que representar  el trazo de los puntos de la tensión). Y una etiqueta "VR(t),VL(t), VC(t)" al trazado. '''
        plotext.plot(x, y, marker="dot", color="red",label="VR(t)")
        plotext.plot(x, y1, marker="dot", color="blue",label="VL(t)")
        plotext.plot(x, y2, marker="dot", color="green",label="VC(t)")
        
        ''' plotext.sleep  Pausa la ejecución del programa durante 0.1 segundos para controlar la velocidad de la animación.'''
        plotext.sleep(0.1)
        plotext.show()
        
    ''' plotext.clear_plot(): Borra el gráfico después de que se completan todos los fotogramas de la animación.'''
    plotext.clear_plot()

''' Se define la función graficadorI:
Se encarga de graficar la corriente en un circuito.'''  
def graficadorI(A, F, AG):
    l = int(F)  # Se convierte la frecuencia F a un numero entero y se almacena en l
    x = range(0, l+1) # Se crea un rango de valores en el eje x que va desde 0 hasta l+1
    frames = 50 # Establece el número de fotogramas que se utilizarán para la animación. En este caso, se han definido 50 fotogramas.

    plotext.title("Corriente del Circuito") #  Se establece el título del gráfico como "Corriente del Circuito"
    plotext.clc()  #  Borra la pantalla del gráfico anterior, si lo hay.

    ''' Se inicia un bucle que itera a través de los fotogramas, cada iteración del bucle representa un fotograma de la animación. '''
    for i in range(frames):
        plotext.clt() 
        plotext.cld() 
        
        ''' y:  Calcula los valores de la función seno con una amplitud A, un número de periodos F, una longitud l y un desplazamiento de fase (2 * i / frames) + math.radians(AG).
        Estos valores representan la forma de onda de la corriente I(t) en el circuito.'''
        y = plotext.sin(amplitude=A, periods=F, length=l, phase=(2 * i  / frames) + math.radians(AG))
        
        ''' plotext.plot Traza los puntos en el gráfico utilizando los valores de "x " y "y " 
        Se define el marcado con "dot" (punto), color (Magenta que representar  el trazo de los puntos de la tensión). Y una etiqueta "I(t)" al trazado.'''
        plotext.plot(x, y, marker="dot", color="magenta",label="I(t)")
        
        ''' plotext.sleep  Pausa la ejecución del programa durante 0.1 segundos para controlar la velocidad de la animación.'''
        plotext.sleep(0.1)
        plotext.show()
        
    ''' plotext.clear_plot(): Borra el gráfico después de que se completan todos los fotogramas de la animación.'''
    plotext.clear_plot()
