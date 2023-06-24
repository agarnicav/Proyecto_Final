<center>

# Proyecto Final
## Grupo Attack On Coding

</center>

![Logo](https://i.postimg.cc/c47bzvy0/Atack-on-Codding-edited.jpg)

## Integrantes
- Dilan Mateo Torres Muñoz
- Lisa Maria Forjan Despaigne
- Ana Maria Garnica Vargas


## Circuitos

Un circuito es una colección de componentes reales, fuentes de poder y fuentes de señales, todas conectadas de modo que la corriente pueda fluir en un círculo completo. La corriente eléctrica es un movimiento de electrones, por lo tanto, cualquier circuito debe permitir el paso de los electrones por los elementos que lo componen.

### Componentes de un circuito eléctrico
![Componentes](https://github.com/agarnicav/Proyecto_Final/assets/124607325/e1de8778-b427-481d-b903-fb95b4c83952)

- Fuente de alimentación: Suministra la energía eléctrica al circuito. Puede ser una batería, un generador o una fuente de alimentación de corriente alterna.
- Resistencia: Restringe el flujo de corriente en el circuito. Las resistencias se utilizan para controlar la cantidad de corriente que fluye en un circuito y para limitar la caída de voltaje. Se miden en Ohms.
- Capacitor: Almacena y libera carga eléctrica. Está compuesto por dos placas conductoras separadas por un material dieléctrico. Los capacitores se utilizan para almacenar energía, filtrar señales, acoplar circuitos, entre otros.
- Inductor: Almacena energía en forma de campo magnético. Está formado por una bobina de alambre conductor. Los inductores se utilizan para almacenar energía, filtrar señales y controlar cambios en la corriente.
- Interruptores: Permiten abrir o cerrar el flujo de corriente en un circuito. Pueden ser interruptores manuales o electrónicos controlados.


 ## Cicuitos RC RL Y RLC

 ## Circuitos RC

Los circuitos RC son  circuitos computos por Resistencias (R) y un Capacitos (C), Conectados en serie o en paralelo. Estos circuitos almacenan voltajes para dejarlos en milifacciones en segundos.

 **Circuitos RC en Serie y paralero**

- **En un circuito RC en serie**: el resistor y el capacitor se conectan uno tras otro, compartiendo la misma corriente. Las rresistencias limita el flujo de corriente en el circuito, mientras que el capacitor almacena y libera carga eléctrica a medida que la corriente fluye a través de él. El capacitor se carga y descarga a través del resistor.

- **En un circuito RC en paralelo**:  el resistor y el capacitor se conectan de forma paralela a la fuente de alimentación. Esto significa que la corriente se divide entre el resistor y el capacitor. El resistor proporciona una ruta para la corriente constante, mientras que el capacitor se carga y descarga independientemente a través de su propia trayectoria.


### Formulas


**Impedancia**
Para calcular la impedancia en un circuito RC:

Impedancia del resistor (R): Z_R = R
Impedancia del capacitor (C): Z_C = 1 / (2 * π * f * C)
Impedancia total del circuito (Z_eq): Z_eq = sqrt(Z_R^2 + Z_C^2)
Para calcular la impedancia en un circuito RL:

R es la resistencia en ohmios, C es la capacitancia en microfaradios, L es la inductancia en henrios, f es la frecuencia en hercios, ω es la frecuencia angular en radianes por segundo (ω = 2 * π * f), j es la unidad imaginaria (√(-1)).


**Resistencias total:**

R_total = R + (1/Cs)
En un circuito RC en serie, la resistencia total (R_total) es simplemente la suma de la resistencia (R) y la resistencia del capacitor (1/Cs), expresada como la 

**Corriente total:**

I(t) = (V / R) * (1 - e^(-t/τ))
 Donde V es el voltaje aplicado, R es la resistencia y τ es la constante de tiempo. El tiempo (t) es el tiempo transcurrido desde el inicio de la carga.
 

## Circuitos RL

Un circuito RL es un circuito eléctrico que contiene una combinación de una bobina (L) y una resistencia (R). En un circuito RL, la bobina (inductor) almacena energía en forma de campo magnético cuando fluye corriente a través de ella. 

Cuando se aplica un voltaje al circuito RL, la corriente no aumenta instantáneamente debido a la inductancia de la bobina. La inductancia resiste los cambios rápidos en la corriente, lo que resulta en una respuesta transitoria más lenta.

- **Circuito RL en serie** :
En un circuito RL en serie, el inductor (L) y la resistencia (R) se conectan uno tras otro, de modo que la corriente fluye a través de ambos componentes en serie. En esta configuración, la corriente es la misma en todos los elementos del circuito, pero la tensión se divide entre el inductor y la resistencia. La inductancia afecta el comportamiento de la corriente y la respuesta transitoria del circuito. La resistencia, por su parte, limita el flujo de corriente y disipa energía en forma de calor.

- **Circuito RL en paralelo :**
En un circuito RL en paralelo, el inductor (L) y la resistencia (R) se conectan en paralelo a la fuente de alimentación. En esta configuración, la tensión es la misma en ambos elementos, pero la corriente se divide entre el inductor y la resistencia. El inductor proporciona una ruta para la corriente alterna, mientras que la resistencia limita el flujo de corriente y disipa energía. En un circuito RL en paralelo, la inductancia afecta la impedancia total del circuito y la fase de la corriente en relación con la tensión aplicada.


### Formulas

Para calcular la impedancia en un circuito RL:
- **Impedancia (Z):**

La impedancia combina tanto la resistencia como la reactancia inductiva y representa la oposición total al flujo de corriente en el circuito RL.

- Impedancia del resistor (R): Z_R = R
- Impedancia del inductor (L): Z_L = j * ω * L
- Impedancia total del circuito (Z_eq): Z_eq = sqrt(Z_R^2 + Z_L^2)

Z es la impedancia total del circuito., R es la resistencia en ohmios.w L es la reactancia inductiva en ohmios, que se calcula multiplicando la frecuencia angular (ω) por la inductancia (L):


- **Corriente total (I_total):**

I_total = V / Z

- **Corriente en la resistencia (I_R):**

I_R = V / R

## Circuito RLC
Los circuitos RLC son circuitos eléctricos que contienen una combinación de elementos resistivos (R), inductivos (L) y capacitivos (C). Estos circuitos son de particular interés debido a su comportamiento resonante y su capacidad para filtrar frecuencias específicas. El componente resistivo (R) representa la resistencia eléctrica y se utiliza para limitar el flujo de corriente en el circuito. La resistencia disipa la energía eléctrica en forma de calor. El componente inductivo (L) representa la inductancia y se crea mediante la presencia de una bobina de alambre conductor. La inductancia almacena energía en forma de campo magnético cuando fluye corriente a través de ella. El componente capacitivo (C) representa la capacitancia y se crea mediante la presencia de un capacitor, que consta de dos placas conductoras separadas por un material dieléctrico. El capacitor almacena energía en forma de campo eléctrico cuando se carga.

Cuando se combinan estos tres componentes en un circuito, se pueden observar fenómenos interesantes, como la resonancia y el filtrado de frecuencias. Los circuitos RLC pueden tener diferentes configuraciones, como circuitos RLC en serie, circuitos RLC en paralelo o circuitos RLC resonantes.

- **Circuito RLC en serie:**
En un circuito RLC en serie, los componentes (resistencia, inductancia y capacitancia) están conectados en serie uno tras otro. La corriente es la misma en todos los componentes del circuito.
La impedancia total del circuito RLC en serie se calcula sumando las impedancias de cada componente en serie: Z_eq = R + jωL + 1/(jωC), donde ω es la frecuencia angular en radianes por segundo.

- **Circuito RLC en paralelo:**
En un circuito RLC en paralelo, los componentes (resistencia, inductancia y capacitancia) están conectados en paralelo uno junto al otro.
El voltaje es el mismo en todos los componentes del circuito.
La impedancia total del circuito RLC en paralelo se calcula sumando las admitancias de cada componente en paralelo y luego tomando el inverso: 1/Z_eq = 1/R + 1/(jωL) + jωC.

### Formulas

- **Impedancia** 
Impedancia total (Z_eq) del circuito RLC en función de R, L y C:
(Z_eq): Z_eq = sqrt(Z_R^2 + (Z_L - Z_C)^2))

Para calcular la impedancia en un circuito RLC:

Impedancia del resistor (R): Z_R = R
Impedancia del inductor (L): Z_L = j * ω * L
Impedancia del capacitor (C): Z_C = 1 / (j * ω * C)

donde ω es la frecuencia angular en radianes por segundo, ω = 2 * π * f, y f es la frecuencia en hercios.

- **Corriente en el circuito (I)**   en función de la tensión de la fuente (V) y la impedancia (Z_eq):
I = V / Z_eq

- **Tensión en el circuit:**  (V_R, V_L, V_C) en función de la corriente (I) y la impedancia (Z_eq):

Tensión en el resistor (V_R): V_R = I * R
Tensión en el inductor (V_L): V_L = I * (ω * L)
Tensión en el capacitor (V_C): V_C = I * (1 / (ω * C))
Potencia en el circuito (P) en función de la corriente (I) y la tensión en el resistor (V_R):
P = V_R * I = (I * R) * I = I^2 * R




# Procedimiento del Proyecto 

1. Se crean y presentan circuitos de muestra para que los usuarios puedan comprender los tipos de circuitos que el programa maneja. Estos circuitos ilustran visualmente la configuración y la conexión de los componentes en cada tipo de circuito.
   
![Circuitos 1](https://github.com/agarnicav/Proyecto_Final/assets/124607325/5d6d9cb0-a1cb-457c-98ed-87256eaeebb2)

![Circuitos 2](https://github.com/agarnicav/Proyecto_Final/assets/124607325/9c192147-f29f-4e5e-8124-d33a9895220a)


2. Se definene funciones para poder alamcenar, procesar y hallar los valores del circuito elegido.

- Función datosDeTension() la cual solicita al usuario los datos de voltaje de la fuente de corriente alterna (AC) y devuelve un diccionario con esos datos.
  ![Datostension](https://github.com/agarnicav/Proyecto_Final/assets/124607325/db72c783-5017-4efc-874d-01039c566b6f)

- Función datosDeResistencia() que solicita al usuario la resistencia en ohmios y devuelve un diccionario con ese dato.
![Datosresistencias](https://github.com/agarnicav/Proyecto_Final/assets/124607325/8ed72228-8caa-4e05-905c-b6bf01fdb793)

- Función datosDeCondensador() que solicita al usuario la capacitancia en microfaradios y devuelve un diccionario con ese dato.
![DatosCondensador](https://github.com/agarnicav/Proyecto_Final/assets/124607325/8a22db63-7b80-4edd-a1b1-f0a6037c0881)

- Función datosDeInductor() que solicita al usuario la inductancia en henrios y devuelve un diccionario con ese dato.
![Datos inductor](https://github.com/agarnicav/Proyecto_Final/assets/124607325/aa91550f-6b6e-4615-bf7a-464e23306698)

- Función convertirFasores() que toma un diccionario de datos del circuito y convierte los valores de voltaje, resistencia, capacitancia e inductancia en fasores (representación compleja). Devuelve un diccionario con los fasores correspondientes.
![Convertir fasores](https://github.com/agarnicav/Proyecto_Final/assets/124607325/b70c2928-9e8c-42c1-8363-f9723f5a1f3c)

- Función impedanciaEquivalente() que toma los fasores y una bandera como entrada y calcula la impedancia equivalente del circuito. Dependiendo del valor de la bandera, realiza diferentes cálculos y devuelve una lista con la magnitud y el ángulo de la impedancia equivalente.
![Impedanciaequivalente](https://github.com/agarnicav/Proyecto_Final/assets/124607325/5d5e3b07-11c7-415a-9788-1864ed58d860)

Función leyDeOhm() que toma la impedancia, los fasores y una bandera como entrada. Utiliza la ley de Ohm para calcular la corriente y las tensiones en el circuito. Devuelve un diccionario con los resultados.
![Ley de ohm](https://github.com/agarnicav/Proyecto_Final/assets/124607325/3dcacc2d-ab20-4062-a180-06ab1c231b0e)



