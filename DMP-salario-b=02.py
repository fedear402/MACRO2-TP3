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

# Funcion busca E de equilibrio
def E_eq(A):
    E = np.linspace(0, 99.99, num=100000)
    V = ( (b * E) / (K * (L_barra - E) )**beta )**(1/gamma)
    alpha = (b*E) / V
    a = (b*E) / (L_barra - E)
    Vv = (-C + ( alpha / (a + alpha + 2*b + 2*r)  ) * A)/r
    E_equilibrio = None
    for i, e in zip(r*Vv, E):
        if abs(i) <= 0.001:
            E_equilibrio = e
            break
    return E_equilibrio

##################################################
# SALARIOS con A low
##################################################
A_l = 1.5

# variable independiente w
w = np.linspace(0, 1.5, num=10000)

E_equilibrio_l = E_eq(A_l)

# Evaluamos en el equilibrio
V = ( (b * E_equilibrio_l) / (K * (L_barra - E_equilibrio_l) )**beta )**(1/gamma)
alpha = (b*E_equilibrio_l) / V
a = (b*E_equilibrio_l) / (L_barra - E_equilibrio_l)
w_l_eq = round(((a+b+r)*A_l)/(a+alpha+2*b+2*r), 3)

# var dependiente
VEVU_l = w/(a+b+r)
VFVV_l = (A_l-w)/(alpha+b+r)

# ploteamos
fig, ax = plt.subplots()
ax.plot(w, VEVU_l, color='red', linewidth=2, linestyle="--", label=r"$V_{E}-V_{U}, A_{\text{low}}$") 
ax.plot(w, VFVV_l, color='blue', linewidth=2, linestyle="--", label=r"$V_{F}-V_{V}, A_{\text{low}}$") 



##################################################
# SALARIOS con A high
##################################################
A_h = 2

# Buscamos E de equilibrio
E_equilibrio_h = E_eq(A_h)

# Evaluamos en el equilibrio
V = ( (b * E_equilibrio_h) / (K * (L_barra - E_equilibrio_h) )**beta )**(1/gamma)
alpha = (b*E_equilibrio_h) / V
a = (b*E_equilibrio_h) / (L_barra - E_equilibrio_h)
w_h_eq = round(((a+b+r)*A_h)/(a+alpha+2*b+2*r), 3)

VEVU_h = w/(a+b+r)
VFVV_h = (A_h-w)/(alpha+b+r)


ax.plot(w, VEVU_h, color='red', linewidth=2, label=r"$V_{E}-V_{U}, A_{\text{high}}$") 
ax.plot(w, VFVV_h, color='blue', linewidth=2, label=r"$V_{F}-V_{V}, A_{\text{high}}$") 


# labels
plt.legend(loc='upper left')
ax.set_title(f"Salario en equilibrio - modelo DMP - b = {b}")
ax.set_ylabel('Beneficios')
ax.set_xlabel('Salarios')



ax.axvline(x=w_h_eq, color='black', linestyle=':', ymin=0, 
           ymax=(w_h_eq - ax.get_ylim()[0]) / (ax.get_ylim()[1] - ax.get_ylim()[0]) - 0.02) 

ax.axvline(x=w_l_eq, color='black', linestyle=':', ymin=0, 
           ymax=(w_l_eq - ax.get_ylim()[0]) / (ax.get_ylim()[1] - ax.get_ylim()[0]) + 0.05) 


# agrega label en el tick de w de equilibrio
t = sorted( list(ax.get_xticks()) + [w_h_eq, w_l_eq] )
del t[0]
del t[-1]
del t[3]
del t[-5]
print(t)
labels = [round(i, 2) for i in t]
plt.xticks(ticks=t, labels = labels, fontsize=10)
plt.ylim([0, 2])
fig.savefig("DMP-salario-b=02.png")
plt.show()