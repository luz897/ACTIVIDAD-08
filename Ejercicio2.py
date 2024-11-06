import streamlit as st
import pulp
import matplotlib.pyplot as plt
import numpy as np

st.title("Ejercicio 8.3 - Método de Cortes de Gomory")

# Definir el problema de minimización
prob = pulp.LpProblem("Minimizar_C", pulp.LpMinimize)

# Definir variables
x = pulp.LpVariable('x', lowBound=0, cat='Integer')
y = pulp.LpVariable('y', lowBound=0, cat='Integer')

# Función objetivo
prob += x - y

# Restricciones
prob += 3 * x + 4 * y <= 6
prob += x - y <= 1

# Resolver el problema
prob.solve()

# Mostrar la solución en Streamlit
st.write("Estado:", pulp.LpStatus[prob.status])
st.write("x =", x.varValue)
st.write("y =", y.varValue)
st.write("Valor óptimo (C) =", pulp.value(prob.objective))

# Gráfica de la región factible
x_vals = np.linspace(0, 3, 400)
y_vals1 = (6 - 3 * x_vals) / 4
y_vals2 = x_vals - 1

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals1, label="3x + 4y ≤ 6")
plt.plot(x_vals, y_vals2, label="x - y ≤ 1")
plt.xlim((0, 3))
plt.ylim((0, 3))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Región factible')
plt.fill_between(x_vals, np.minimum(y_vals1, y_vals2), alpha=0.3)
st.pyplot(plt)
