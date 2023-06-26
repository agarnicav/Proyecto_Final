import plotext 
import math

def graficadorRC(A,A1,F,AG,AG1):
    l = int(F)
    x = range(0, l+1)
    frames = 50

    plotext.title("Tensiones Circuito RC")
    plotext.clc()

    for i in range(frames):
        plotext.clt() 
        plotext.cld() 

        y = plotext.sin(amplitude=A, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG))
        y1 = plotext.sin(amplitude=A1, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG1))
        plotext.plot(x, y, marker="dot", color="red",label="VR(t)")
        plotext.plot(x, y1, marker="dot", color="green",label="VC(t)")
        plotext.sleep(0.1)
        plotext.show()
    
    plotext.clear_plot()

def graficadorRL(A,A1,F,AG,AG1):
    l = int(F)
    x = range(0, l+1)
    frames = 50

    plotext.title("Tensiones Circuito RL")
    plotext.clc()

    for i in range(frames):
        plotext.clt() 
        plotext.cld() 

        y = plotext.sin(amplitude=A, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG))
        y1 = plotext.sin(amplitude=A1, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG1))
        plotext.plot(x, y, marker="dot", color="red",label="VR(t)")
        plotext.plot(x, y1, marker="dot", color="blue",label="VL(t)")
        plotext.sleep(0.1)
        plotext.show()
    
    plotext.clear_plot()

def graficadorRLC(A,A1,A2,F,AG,AG1,AG2):
    l = int(F)
    x = range(0, l+1)
    frames = 50

    plotext.title("Tensiones Circuito RLC")
    plotext.clc()

    for i in range(frames):
        plotext.clt() 
        plotext.cld() 

        y = plotext.sin(amplitude=A, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG))
        y1 = plotext.sin(amplitude=A1, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG1))
        y2 = plotext.sin(amplitude=A2, periods=F, length=l, phase=(2 * i  / frames)-math.radians(AG2))
        plotext.plot(x, y, marker="dot", color="red",label="VR(t)")
        plotext.plot(x, y1, marker="dot", color="blue",label="VL(t)")
        plotext.plot(x, y2, marker="dot", color="green",label="VC(t)")
        plotext.sleep(0.1)
        plotext.show()
    
    plotext.clear_plot()

def graficadorI(A, F, AG):
    l = int(F)
    x = range(0, l+1)
    frames = 50

    plotext.title("Corriente del Circuito")
    plotext.clc()

    for i in range(frames):
        plotext.clt() 
        plotext.cld() 

        y = plotext.sin(amplitude=A, periods=F, length=l, phase=(2 * i  / frames) + math.radians(AG))
        plotext.plot(x, y, marker="dot", color="magenta",label="I(t)")
        plotext.sleep(0.1)
        plotext.show()
    
    plotext.clear_plot()