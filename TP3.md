\textbf{a)}

\textbf{Modelo DMP:} En estos modelos de búsqueda se asigna una distribución de probabilidades para los salarios que podría enfrentar un trabajador. El valor de estar empleado, $V_{E}$, es $w$ y en cada intervalo de tiempo $dt$ la utilidad es $w\cdot dt$. En ese intervalo también hay una tasa $b$ con la que el trabajo desaparece. Luego, con tasa de interés constante $r$, cada intervalo $dt$ se descuenta con el factor $\frac{1}{1+r \cdot dt}$. La utilidad es el salario sumado recursivamente a la misma utilidad instantánea de estar empleado $V_{E}$ ponderado por la tasa con la que se pierde el trabajo y le agregamos la utilidad de estar desempleado $V_{U}$; todo eso descontado et al. (2014, p.261):
$$
V_{E}=\frac{1}{1+r \cdot dt}\left[ w\cdot dt+\left( 1-b\cdot dt \right) V_{E} + \left( b \cdot dt \right)  V_{U}  \right] 
$$
Si multiplicamos ambos lados por $1+r\cdot dt$
$$
V_{E}\left( 1+r \cdot dt \right) =\left[ w\cdot dt+\left( 1-b\cdot dt \right) V_{E} + \left( b \cdot dt \right)  V_{U}  \right] 
$$$$
V_{E}+rV_{E} \cdot dt-\left( 1-b\cdot dt \right) V_{E} =w\cdot dt + \left( b \cdot dt \right)  V_{U}
$$
$$
V_{E}\left( r+b \right)dt =(w+ b V_{U})dt
$$
$$
rV_{E}=w+b(V_{U}-V_{E})
$$

Para los trabajadores tenemos entonces $rV_{E}=w-b(V_{E}-V_{U})$. Es el salario en todos los periodos, mitigados por la posibilidad de perderlos. $rV_{E}$ se puede interpretar como el flujo esperado de ingresos. Ese flujo esperado es igual al flujo de salario que recibe al estar empleado menos un ingreso promedio $b(V_{E}-V_{U})$ que incluye el posible cambios de estado del agente a estar desempleado.

De manera muy similar podemos plantear el valor de estar desempleado $V_{U}$ con la misma ecuación que $V_{E}$ pero usando $a$, la tasa con la que se encuentra empleo (se cambia de estado), en lugar de $b$. Nos queda $rV_{U}=a(V_{E}-V_{U})$ y se puede interpretar como la 'probabilidad' de tener un flujo de ingresos en el futuro.

Para las firmas, tienen que valorar tener un puesto de trabajo ocupado por un trabajador, $V_{F}$, o tenerlo sin ocupar, $V_{V}$. La lógica es similar al caso de los trabajadores. Esta es la función de valor de tener un puesto de trabajo ocupado:
$$
V_{F}=\frac{1}{1+r \cdot dt}\left[ (A-w-C)\cdot dt+\left( 1-b\cdot dt \right) V_{F} + \left( b \cdot dt \right)  V_{V}  \right] 
$$
Tenemos de nuevo $b$, la tasa exógena con la que se destruye el empleo, pero aparece de una manera inversa a como estaba antes en la función de valor del empleado. $A$ es la producción del trabajador empleado y $C$ es el costo fijo de tener un puesto de trabajo abierto, ocupado o sin ocupar. 

Sabemos que se puede simplificar esa expresión a $rV_{F}=(A-w-C)-b(V_{F}-V_{V})$, representado el valor de tener un puesto ocupado como simplemente el beneficio $A$ menos el costo del trabajador y del puesto también restando la posibilidad de que deje de existir ese empleo. El valor de tener el puesto vacante es $rV_{V}=(-C)+\alpha(V_{F}-V_{V})$. El costo de forma negativa y, sumando, la posibilidad de que se ocupe (representado por la tasa $\alpha$, con la que se ocupan los puestos vacantes)

\textbf{Modelo Shapiro-Stiglitz:}
Este modelo plantea funciones de valor diferentes solo para el trabajador que decide, además del salario que acepta o no, un nivel de esfuerzo, $e$, que le resta utilidad y es función creciente del salario. En la versión simple del modelo, el nivel de esfuerzo es discreto y puede no esforzarse: $e=0$ o esforzarse $e=\bar{e}$. Además, se asume que la tasa de retorno de la economía $r$ es igual a la tasa de descuento intertemporal del agente, $\rho$. Las funciones de valor son las siguientes:

Estando empleado y esforzándose gana $\rho V_{E}=(w-\bar{e})+b(V_{U}-V_{E})$. Donde $(V_{U}-V_{E})$ es la ganancia al perder el trabajo. El valor de estar empleado debería ser mayor al de estar desempleado por lo que el valor de esforzarse es el salario menos el esfuerzo menos el prospecto de quedarse sin trabajo.

El valor de trabajar y no esforzarse es $\rho V_{S}=w+(b+q)(V_{U}-V_{S})$. Representa el salario y el valor promedio al cambiar de estado, pero ahora con una probabilidad más alta de cambiar de estado ya que pierde el trabajo no solo con tasa $b$ de la naturaleza de la economía sino que también con tasa $q$ con la que atrapan a trabajadores no esforzándose.

Por último el valor de estar desempleado es $\rho V_{U}=a(V_{E}-V_{U})$ y es proporcional a la tasa de encontrar trabajo y recibir el flujo de ingresos de empleo en el futuro como en el modelo DMP.
\\

\textbf{b)} Este es el resultado de la negociación de un contrato según Nash con poder de negociación igual entre las partes. El problema de negociación que se plantea es el de repartir un excedente total $S$. La idea es que el excedente total van a ser los retornos de ambos si deciden negociar (entrar en un contrato de trabajo). Para el trabajador esto es $V_{E}-V_{U}$ porque gana $V_{E}$ si acceden a un contrato y $V_{U}$ es lo que ganaría si no. Similarmente para la firma su retorno por estar en una relación contractual es es $V_{F}-V_{V}$. (Cahuc et al., 2014, p.592)

El poder de negociación de cada uno entra en consideración en tanto el retorno que recibe cada agente cuando acceden a al contrato es una proporción del excedente total $S$:

$$
V_{E}-V_{U}=\gamma S \ \ \ \ \ \ \ V_{F}-V_{V}=(1-\gamma)S
$$

donde $\gamma$ es el poder de negociación del trabajador. Igual poder de negociación implica $\gamma=0.5$. Es obvio entonces que ambos retornos deben ser iguales si el poder de negociación es el mismo. $0.5S=V_{E}-V_{U}=V_{F}-V_{V}$.
\\

\textbf{c)} Esta condición es una condición de la libre entrada de empresas en el mercado. Con libre entrada el costo promedio de tener un puesto vacante abierto para la firma es igual a la ganancia esperada de que ese trabajo se ocupe. Es decir, con libre entrada al mercado, ninguna firma se beneficia si no llena los puestos que tiene abiertos.
\\

\textbf{d)} En el modelo de Shapiro Stiglitz los empleados se esfuerzan sólo si $V_{E}\geq V_{S}$, el valor actual de esforzarse tiene que ser mayor que el de no hacerlo. Las firmas controlan la variable salario que define esas funciones de valor, y quisieran pagar el mínimo salario necesario para que se esfuerzan. Como son funciones crecientes en salario, hay un salario que deja al valor de esforzarse igual al valor de no hacerlo y pagar más que eso no es eficiente para la firma. El salario que paga cuando $V_{E}= V_{S}$ es el mínimo necesario para que esforzarse sea una mejor respuesta del trabajador.

----
2


---
BIBLIOGRAFIA

Cahuc, Pierre & Carcillo, Stéphane & Zylberberg, André, 2014."Labor Economics, second edition," MIT Press Books, The MIT Press, edition 2, volume 1, number 0262027704, December.

Campante, F., Sturzenegger, F. and Velasco, A. 2021. Advanced Macroeconomics: An Easy Guide. Ch. 16. ‘Unemployment’, pp. 243–258. London: LSE Press. DOI: https://doi.org/10.31389/lsepress.ame.p License: CC-BY-NC 4.0.