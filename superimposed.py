import numpy as np
import matplotlib.pyplot as plt

# Variables conocidas
beta = 0.5
gamma = 1 - beta
K = 1
r = 0.04
C = 1
L_barra = 100

# Funcion busca E de equilibrio
def E_eq(A, b):
    E = np.linspace(0, 99.99, num=100000)
    V = ((b * E) / (K * (L_barra - E))**beta)**(1/gamma)
    alpha = (b*E) / V
    a = (b*E) / (L_barra - E)
    Vv = (-C + (alpha / (a + alpha + 2*b + 2*r)) * A) / r
    E_equilibrio = None
    for i, e in zip(r*Vv, E):
        if abs(i) <= 0.001:
            E_equilibrio = e
            break
    return E_equilibrio

# Plotting function
def plot_graph(b, color, transparency):
    A_l = 1.5
    w = np.linspace(0, 1.5, num=10000)
    E_equilibrio_l = E_eq(A_l, b)
    V = ((b * E_equilibrio_l) / (K * (L_barra - E_equilibrio_l))**beta)**(1/gamma)
    alpha = (b*E_equilibrio_l) / V
    a = (b*E_equilibrio_l) / (L_barra - E_equilibrio_l)
    VEVU_l = w/(a+b+r)
    VFVV_l = (A_l-w)/(alpha+b+r)

    A_h = 2
    E_equilibrio_h = E_eq(A_h, b)
    V = ((b * E_equilibrio_h) / (K * (L_barra - E_equilibrio_h))**beta)**(1/gamma)
    alpha = (b*E_equilibrio_h) / V
    a = (b*E_equilibrio_h) / (L_barra - E_equilibrio_h)
    VEVU_h = w/(a+b+r)
    VFVV_h = (A_h-w)/(alpha+b+r)

    plt.plot(w, VEVU_l, color="red", linewidth=2, linestyle="--", alpha=transparency, label=r"$V_{E}-V_{U}, A_{low}$" if b == 0.1 else "") 
    plt.plot(w, VFVV_l, color="blue", linewidth=2, linestyle="--", alpha=transparency, label=r"$V_{F}-V_{V}, A_{low}$" if b == 0.1 else "") 
    plt.plot(w, VEVU_h, color="red", linewidth=2, alpha=transparency, label=r"$V_{E}-V_{U}, A_{high}$" if b == 0.1 else "") 
    plt.plot(w, VFVV_h, color="blue", linewidth=2, alpha=transparency, label=r"$V_{F}-V_{V}, A_{high}$" if b == 0.1 else "")

# Create a figure
plt.figure(figsize=(10, 6))

# Plot both sets of data
plot_graph(0.1, 'red', 1)   # b = 0.1 without transparency
plot_graph(0.2, 'blue', 0.3)  # b = 0.2 with 50% transparency



plt.title("Salario en equilibrio - modelo DMP con distintos b")
plt.xlabel("Salarios")
plt.ylabel("Beneficios")
plt.legend()
plt.grid(True)
plt.savefig("super.png")
plt.show()
