
<span style="color:purple">## Proyecto Final</span>

## Circuitos

Un circuito es una colección de componentes reales, fuentes de poder y fuentes de señales, todas conectadas de modo que la corriente pueda fluir en un círculo completo.La corriente eléctrica es un movimiento de electrones, por lo tanto, cualquier circuito debe permitir el paso de los electrones por los elementos que lo componen.

### Componentes de un circuito electrico 
![image](https://github.com/agarnicav/Proyecto_Final/assets/124607325/e1de8778-b427-481d-b903-fb95b4c83952)


Fuente de alimentación: Suministra la energía eléctrica al circuito. Puede ser una batería, un generador o una fuente de alimentación de corriente alterna.

**Resistencia**: Restringe el flujo de corriente en el circuito. Las resistencias se utilizan para controlar la cantidad de corriente que fluye en un circuito y para limitar la caída de voltaje. Se miden en Ohms 

**Capacitor:** Almacena y libera carga eléctrica. Está compuesto por dos placas conductoras separadas por un material dieléctrico. Los capacitores se utilizan para almacenar energía, filtrar señales, acoplar circuitos, entre otros.

**Inductor:** Almacena energía en forma de campo magnético. Está formado por una bobina de alambre conductor. Los inductores se utilizan para almacenar energía, filtrar señales y controlar cambios en la corriente.

**Interruptores:** Permiten abrir o cerrar el flujo de corriente en un circuito. Pueden ser interruptores manuales o electrónicos controlados.

 ## Cicuitos RC RL Y RLC

 ### Circuitos RC

Los circuitos RC son  circuitos computos por Resistencias (R) y un Capacitos (C), Conectados en serie o en paralelo. Estos circuitos almacenan voltajes para dejarlos en milifacciones en segundos.

 **Circuitos RC en Serie y paralero**

**En un circuito RC en serie**: el resistor y el capacitor se conectan uno tras otro, compartiendo la misma corriente. Las rresistencias limita el flujo de corriente en el circuito, mientras que el capacitor almacena y libera carga eléctrica a medida que la corriente fluye a través de él. El capacitor se carga y descarga a través del resistor.

**En un circuito RC en paralelo**:  el resistor y el capacitor se conectan de forma paralela a la fuente de alimentación. Esto significa que la corriente se divide entre el resistor y el capacitor. El resistor proporciona una ruta para la corriente constante, mientras que el capacitor se carga y descarga independientemente a través de su propia trayectoria.


**Formulas**

**Circuito RC en serie**

Resistencias total: 

R_total = R + (1/Cs)
En un circuito RC en serie, la resistencia total (R_total) es simplemente la suma de la resistencia (R) y la resistencia del capacitor (1/Cs), expresada como la 

Corriente total: 

I(t) = (V / R) * (1 - e^(-t/τ))
 Donde V es el voltaje aplicado, R es la resistencia y τ es la constante de tiempo. El tiempo (t) es el tiempo transcurrido desde el inicio de la carga.
 

### Circuitos RL

Un circuito RL es un circuito eléctrico que contiene una combinación de una bobina (L) y una resistencia (R). En un circuito RL, la bobina (inductor) almacena energía en forma de campo magnético cuando fluye corriente a través de ella. 

Cuando se aplica un voltaje al circuito RL, la corriente no aumenta instantáneamente debido a la inductancia de la bobina. La inductancia resiste los cambios rápidos en la corriente, lo que resulta en una respuesta transitoria más lenta.

**Circuito RL en serie** :
En un circuito RL en serie, el inductor (L) y la resistencia (R) se conectan uno tras otro, de modo que la corriente fluye a través de ambos componentes en serie. En esta configuración, la corriente es la misma en todos los elementos del circuito, pero la tensión se divide entre el inductor y la resistencia. La inductancia afecta el comportamiento de la corriente y la respuesta transitoria del circuito. La resistencia, por su parte, limita el flujo de corriente y disipa energía en forma de calor.

**Circuito RL en paralelo :**
En un circuito RL en paralelo, el inductor (L) y la resistencia (R) se conectan en paralelo a la fuente de alimentación. En esta configuración, la tensión es la misma en ambos elementos, pero la corriente se divide entre el inductor y la resistencia. El inductor proporciona una ruta para la corriente alterna, mientras que la resistencia limita el flujo de corriente y disipa energía. En un circuito RL en paralelo, la inductancia afecta la impedancia total del circuito y la fase de la corriente en relación con la tensión aplicada.


**Formulas**

**Formulas circuitos RL en serie**

Constante de tiempo (τ):

τ = L / R

Corriente máxima (I_max):

 I_max = V / R 

V es el voltaje aplicado en voltios, R es la resistencia en ohmios.

Corriente en un tiempo dado (I):

I(t) = I_max * (1 - e^(-t/τ))

I_max es la corriente máxima, t es el tiempo en segundos, τ es la constante de tiempo calculada anteriormente.

**Formulas circuitos RL paralelo**

En un circuito RL en paralelo, se utiliza la impedancia en lugar de la resistencia. Aquí tienes algunas fórmulas relevantes para hallar datos en un circuito RL en paralelo:

Impedancia (Z):

La impedancia combina tanto la resistencia como la reactancia inductiva y representa la oposición total al flujo de corriente en el circuito RL en paralelo.
La impedancia en un circuito RL en paralelo se calcula utilizando la fórmula:

1/Z = 1/R + 1/jωL
Z es la impedancia en ohmios, R es la resistencia en ohmios, j es la unidad imaginaria (√(-1)), ω es la frecuencia angular en radianes por segundo, L es la inductancia en henrios.


Corriente total (I_total):

I_total = V / Z

Corriente en la resistencia (I_R):

I_R = V / R

