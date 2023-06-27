![cPRUECTO](https://github.com/agarnicav/Proyecto_Final/assets/124607325/267f2848-0435-4d36-8d88-ebade2782990)


##                                                                 Integrantes
- **Dilan Mateo Torres Muñoz**
- **Lisa Maria Forjan Despaigne**
- **Ana Maria Garnica Vargas**

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
![Circuitos](https://github.com/agarnicav/Proyecto_Final/assets/124607325/bf8f8ae9-6e39-4976-a351-a7822f800af2)



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Un circuito es un conjunto de componentes eléctricos que permite el flujo de corriente eléctrica a través de una trayectoria cerrada. La corriente eléctrica consiste en el movimiento de electrones, por lo tanto, cualquier circuito debe permitir el paso de los electrones a través de los elementos que lo componen.

### Componentes de un circuito eléctrico

![Componentes](https://github.com/agarnicav/Proyecto_Final/assets/124607325/e1de8778-b427-481d-b903-fb95b4c83952)

- **Fuente de alimentación:** Suministra la energía eléctrica al circuito. Puede ser una batería, un generador o una fuente de alimentación de corriente alterna.
- **Resistencia:** Restringe el flujo de corriente en el circuito. Las resistencias se utilizan para controlar la cantidad de corriente que fluye en un circuito y para limitar la caída de voltaje. Se miden en Ohms.
- **Capacitor:** Almacena y libera carga eléctrica. Está compuesto por dos placas conductoras separadas por un material dieléctrico. Los capacitores se utilizan para almacenar energía, filtrar señales, acoplar circuitos, entre otras aplicaciones.
- **Inductor:** Almacena energía en forma de campo magnético. Está formado por una bobina de alambre conductor. Los inductores se utilizan para almacenar energía, filtrar señales y controlar cambios en la corriente.
- **Interruptores:** Permiten abrir o cerrar el flujo de corriente en un circuito. Pueden ser interruptores manuales o electrónicos controlados.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
![Circuitos rc rl rlc](https://github.com/agarnicav/Proyecto_Final/assets/124607325/ff8d718a-7b8c-4cd3-ba61-642204c22504)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

**Corriente fasorial:**

    I = V / Z
    Donde V es la amplitud de la tensión y Z es la amplitud de la impedancia.

**Tensión en la resistencia:**

    VR = I * R
    Donde I es la corriente fasorial y R es la resistencia.

**Tensión en el condensador:** 

    VC = I * Xc
    Donde I es la corriente fasorial y Xc es la reactancia capacitiva.


## Circuitos RL

Un circuito RL es un circuito eléctrico que contiene una combinación de una bobina (L) y una resistencia (R). En un circuito RL, la bobina (inductor) almacena energía en forma de campo magnético cuando fluye corriente a través de ella. Cuando se aplica un voltaje al circuito RL, la corriente no aumenta instantáneamente debido a la inductancia de la bobina. La inductancia resiste los cambios rápidos en la corriente, lo que resulta en una respuesta transitoria más lenta.

- **Circuito RL en serie** :
El inductor (L) y la resistencia (R) se conectan uno tras otro, de modo que la corriente fluye a través de ambos componentes en serie. En esta configuración, la corriente es la misma en todos los elementos del circuito, pero la tensión se divide entre el inductor y la resistencia. La inductancia afecta el comportamiento de la corriente y la respuesta transitoria del circuito. La resistencia, por su parte, limita el flujo de corriente y disipa energía en forma de calor.

- **Circuito RL en paralelo :**
En un circuito RL en paralelo, el inductor (L) y la resistencia (R) se conectan en paralelo a la fuente de alimentación. En esta configuración, la tensión es la misma en ambos elementos, pero la corriente se divide entre el inductor y la resistencia. El inductor proporciona una ruta para la corriente alterna, mientras que la resistencia limita el flujo de corriente y disipa energía. En un circuito RL en paralelo, la inductancia afecta la impedancia total del circuito y la fase de la corriente en relación con la tensión aplicada.


### Formulas

**Impedancia (Z):**
Para calcular la impedancia en un circuito RL:

    Impedancia del resistor: 
    (R): ZR = R

    Impedancia del inductor 
    (L): XL = ωL
    Donde XL es la reactancia inductiva, ω es la frecuencia angular del circuito (2πf), L es la inductancia del inductor.
    Finalmente, la impedancia equivalente (Zeq) para el circuito RL se calcula sumando la impedancia del resistor y la impedancia del inductor:

    Impedancia equivalente (Zeq): Zeq = R + jXL
    Donde j es la unidad imaginaria (√-1).

    Impedancia total del circuito (Z_eq): Z_eq = sqrt(Z_R^2 + Z_L^2)

    Z es la impedancia total del circuito., R es la resistencia en ohmios.w L es la reactancia inductiva en ohmios, que se calcula multiplicando la frecuencia angular (ω) por la inductancia (L):

**Corriente fasorial:**

    I = V / Z
    Donde V es la amplitud de la tensión y Z es la amplitud de la impedancia.
    
**Tensión en la resistencia:**

    VR = I * R
    Donde I es la corriente fasorial y R es la resistencia.
    
**Tensión en el inductor:** 

    VL = I * Xl
    Donde I es la corriente fasorial y Xl es la reactancia inductiva.

    
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


**Corriente fasorial:**

    I = V / Z
    Donde V es la amplitud de la tensión y Z es la amplitud de la impedancia.
    
**Tensión en la resistencia:**
   
    VR = I * R
    Donde I es la corriente fasorial y R es la resistencia.
    
**Tensión en el condensador:**

    VC = I * Xc
    Donde I es la corriente fasorial y Xc es la reactancia capacitiva.

**Tensión en el inductor:**

    VL = I * Xl
    Donde I es la corriente fasorial y Xl es la reactancia inductiva.




-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
![Procedimiento proyecto](https://github.com/agarnicav/Proyecto_Final/assets/124607325/ba1a4634-4d3a-4c2e-898b-2d928ece2cec)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Para el desarrollo del proyecto final se crean 4 archivos correspondientes, encargados de solucionar y graficar el circuito y opciones elegidas 

### PRIMER ARCHIVO Circuitos 
Se utiliza la biblioteca colorama para imprimir texto en colores en la consola, se crean y presentan tres circuitos de muestra (RC,RL, RLC), para que los usuarios puedan comprender los tipos de circuitos que el programa maneja. Estos circuitos ilustran visualmente la configuración y la conexión de los componentes en cada tipo de circuito.

![Circuitos 1](https://github.com/agarnicav/Proyecto_Final/assets/124607325/62c9e7bc-da98-4874-bb31-0a6ed6fbd0d7)
![Circuitos 2](https://github.com/agarnicav/Proyecto_Final/assets/124607325/6e13cba0-e8a7-4c25-958f-fcf0c24e2e2d)


### SEGUNDO ARCHIVO circuitos soluncionados 
Se crean y representan los diagramas de los circuitos RC,RL,RCL, se toman como argumentos los valores correspondientes al circuito, como el voltaje (V), voltaje en la resistencia (VR), voltaje en el inductor (VL) y  voltaje en el capacitor (VC),  y la corriente (I), resistencia (R), capacitancia (C), inductancia (L)
![circuitos solucionados 1](https://github.com/agarnicav/Proyecto_Final/assets/124607325/7fbbcdfe-56fe-4c2a-a9d1-a7e5f2d11515)
![circuitos solucionados 2](https://github.com/agarnicav/Proyecto_Final/assets/124607325/fea53e19-9537-46c9-a1d3-b5cedd3d50db)
![circuitos solucionados 3](https://github.com/agarnicav/Proyecto_Final/assets/124607325/9e21a428-d1ff-4ba9-b5d7-9afbb4d42c77)

### TERCERARCHIVO Graficador 

### CUARTO ARCHIVO Solucionador de circuitos 

1. Se definene funciones para poder alamcenar, procesar y hallar los valores del circuito elegido.

- Función datosDeTension() Se define la función para solicitar los datos de la Tension y almacenarlos por medio de un  diccionario 
![Datostension](https://github.com/agarnicav/Proyecto_Final/assets/124607325/a9ecb140-6cdd-48ef-9926-0181a67babaa)

- Función datosDeResistencia() Se define la función que solicita los datos de la resistencia en ohmios y devuelve un diccionario con este dato
![Datosresistencias](https://github.com/agarnicav/Proyecto_Final/assets/124607325/fad0b6e1-c9c1-414b-8902-374d3e6eb48b)

- Función datosDeCondensador()  Se define la función que solicita los datos de la capacitancia en microfaradios y devuelve un diccionario con ese dato.
![DatosCondensador](https://github.com/agarnicav/Proyecto_Final/assets/124607325/dc90a607-011b-4e43-b297-549c5b2e7981)

- Función datosDeInductor() Se define la función que solicita los datos de la inductancia en henrios y devuelve un diccionario con ese dato.
![Datos inductor](https://github.com/agarnicav/Proyecto_Final/assets/124607325/6c8325f5-a8bc-476c-a49b-987aeef4b1f6)


- Función convertirFasores() Se define la función que toma un diccionario de datos del circuito y convierte los valores de voltaje, resistencia, capacitancia e inductancia en fasores. Devuelve un diccionario con los fasores correspondientes.
![Convertir fasores](https://github.com/agarnicav/Proyecto_Final/assets/124607325/d168686d-fc8c-4405-9406-0d5b4f32b2ef)


- Función impedanciaEquivalente() Se define la función que toma los fasores y una bandera como entrada y calcula la impedancia equivalente del circuito. Dependiendo del valor de la bandera, realiza diferentes cálculos y devuelve una lista con la magnitud y el ángulo de la impedancia equivalente.
![Impedanciaequivalente](https://github.com/agarnicav/Proyecto_Final/assets/124607325/9993ad90-5e3c-4ab5-bf25-00ae880adada)

- Función leyDeOhm() Se define la función que toma la impedancia, los fasores y una bandera como entrada. Utiliza la ley de Ohm para calcular la corriente y las tensiones en el circuito. Se devuelven 4 diccionarios que contienen la magnitud y el ángulo de la corriente fasorial, la tensión en la resistencia, la tensión en el condensador (si está presente) y la tensión en el inductor (si está presente).
![Ley de ohm](https://github.com/agarnicav/Proyecto_Final/assets/124607325/3dcacc2d-ab20-4062-a180-06ab1c231b0e)


3. En el bloque if __name__ == "__main__":, se ejecuta el código. El programa utiliza un bucle while para mostrar el menú y permitir al usuario seleccionar la opción del circuito que desea resolver. Si la opción ingresada no corresponde a las que se muestran el buvle se repite hasta que la opción y bandera sea verdadera.
   
![BLOQUE IF](https://github.com/agarnicav/Proyecto_Final/assets/124607325/43cc406b-82e8-47db-8442-be0c854e8f55)

4. Dependiendo de la opción seleccionada, se llaman a las funciones correspondientes para recopilar los datos del circuito, convertirlos en fasores, calcular la impedancia equivalente y aplicar la ley de Ohm para obtener la corriente y las tensiones en el circuito.
 
![March opcion case 1](https://github.com/agarnicav/Proyecto_Final/assets/124607325/64d314bb-b362-4460-9762-79e1c302f7a5)
 
 **Caso 1:** Se imprime el ejemplo de circuiro RC  y se solicitan los datos de tensión, resistencia y capacitancia utilizando las funciones datosDeTension(), datosDeResistencia() y datosDeCondensador(), respectivamente. Luego, se combinan estos datos en un diccionario datosCircuito, se convierten a fasores, se calcula la impedancia equivalente, se aplican las leyes de Ohm y se generan las expresiones para las corrientes y tensiones del circuito. Posteriormente se muestra otro submenú al usuario para que elija qué desea imprimir el circuito RC solucionado o las graficas de corriente y tensión . Dependiendo de la opción seleccionada, se ejecuta el código correspondiente.

![Case2](https://github.com/agarnicav/Proyecto_Final/assets/124607325/eb022311-3c7e-4671-b4fe-1cd05bf8ee41)

**Caso 2:**  Se imprime el ejemplo de circuiro RL y se solicitan los datos de tensión, resistencia e inductancia utilizando las funciones datosDeTension(), datosDeResistencia() y datosDeInductor(), respectivamente. Luego, se combinan estos datos en un diccionario datosCircuito, se convierten a fasores, se calcula la impedancia equivalente, se aplican las leyes de Ohm y se generan las expresiones para las corrientes y tensiones del circuito. Posteriormente se muestra otro submenú al usuario para que elija qué desea imprimir el circuito RL solucionado o las graficas de corriente y tensión . Dependiendo de la opción seleccionada, se ejecuta el código correspondiente.


![Case 3 y ](https://github.com/agarnicav/Proyecto_Final/assets/124607325/ffc90347-115b-45a5-82eb-6e268ab096a8)


**Caso 3:**   Se imprime el ejemplo de circuiro RLC  y se solicitan los datos de voltaje (V1), resistencia (R1), inductor (L1) y condensador (C1). utilizando las funciones datosDeTension(), datosDeResistencia(), datosDeCondensador() y datosDeInductor(), respectivamente. Luego, se combinan estos datos en un diccionario datosCircuito, se convierten a fasores, se calcula la impedancia equivalente, se aplican las leyes de Ohm y se generan las expresiones para las corrientes y tensiones del circuito. Posteriormente se muestra otro submenú al usuario para que elija qué desea imprimir el circuito RLC solucionado o las graficas de corriente y tensión . Dependiendo de la opción seleccionada, se ejecuta el código correspondiente.

**Caso 4:**  Se muestra un mensaje de agradecimiento y el programa finaliza.


