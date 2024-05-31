import numpy as np
import matplotlib.pyplot as plt



# Variables conocidas
beta = 0.5
gamma = 1 - beta
K = 1
r = 0.04
b = 0.2
C = 1
L_barra = 100




# variable independiente E
E = np.linspace(0, 99.99, num=100000)


##################################################################################################
####################  A low ######################################################################
##################################################################################################
A_l = 1.5


# Otras variables que se definen en equilibrio en funcion de E
V = ( (b * E) / (K * (L_barra - E) )**beta )**(1/gamma)
alpha = (b*E) / V
a = (b*E) / (L_barra - E)

Vv = (-C + ( alpha / (a + alpha + 2*b + 2*r)  ) * A_l)/r

fig, ax = plt.subplots()
ax.plot(E, r*Vv, color='green', linewidth=2) 


# empleo de equilibrio con A low
E_equilibrio_l = None
for i, e in zip(r*Vv, E):
    if abs(i) <= 0.0001:
        E_equilibrio_l = round(e,1)
        break
    
# linea en el E de equilibrio con A low
ax.axvline(x=E_equilibrio_l, color='red', linestyle='dashed', 
           ymin=0, ymax=(0 - ax.get_ylim()[0]) / (ax.get_ylim()[1] - ax.get_ylim()[0]) - 0.15) 
           # el - 0.15 está hecho a ojo (es el limte superior contra la linea del 0)

# agrega label en el tick de E de equilibrio
t = sorted( list(ax.get_xticks()) + [E_equilibrio_l] )
del t[0]
del t[-1]
t.remove(float(80))
labels = [i if i != float(100) else r"$\bar{L}$" for i in t]
plt.xticks(ticks=t, labels=labels)



##################################################################################################
####################  A high #####################################################################
##################################################################################################
A_h = 2

# variables endógenas
V = ( (b * E) / (K * (L_barra - E) )**beta )**(1/gamma)
alpha = (b*E) / V
a = (b*E) / (L_barra - E)

# variable dependiente
Vv = (-C + ( alpha / (a + alpha + 2*b + 2*r)  ) * A_h)/r

# plot
ax.plot(E, r*Vv, color='red', linewidth=2) 

# empleo de equilibrio con A high
E_equilibrio_h = None
for i, e in zip(r*Vv, E):
    if abs(i) <= 0.0001:
        E_equilibrio_h = round(e,1)
        break

# linea en el del E de equilibrio con A high
ax.axvline(x=E_equilibrio_h, color='red', linestyle='dashed', ymin=0, 
           ymax=(0 - ax.get_ylim()[0]) / (ax.get_ylim()[1] - ax.get_ylim()[0]))

# lineas
linest = ":"
ax.axhline(0, color='black', linestyle="-")
ax.axhline(-C, color='black', linestyle=linest)
ax.axvline(100, color='black', linestyle=linest)

# labels
fig.suptitle(None)
ax.set_title(f"Empleo en equilibrio - modelo DMP - b={b}")
ax.set_ylabel(r"$rV_{V}$")
ax.set_xlabel("Empleo")

# anota el max y min de ambos graficos
plt.yticks([-C, 0, A_l-C, A_h-C], ["-C", 0, r"$A_{low}$-C", r"$A_{high}$-C"])

# agrega label del valor de E_equilibrio_h
t = sorted( list(ax.get_xticks()) + [E_equilibrio_h] )
labels = [i if i != float(100) else r"$\bar{L}$" for i in t]
plt.xticks(ticks=t, labels=labels)

# Acomoda el label de los E de equilibrio para que se lean
# for label, value in zip(ax.get_xticklabels(), t):
#     if value == E_equilibrio_l:
#         label.set_horizontalalignment('right')
#         label.set_fontsize(10)



fig.savefig("DMP-empleo-equilibrio-b=02.png")
plt.show()