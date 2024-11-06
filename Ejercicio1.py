import streamlit as st
import pulp
import matplotlib.pyplot as plt
import numpy as np

st.title("Ejercicio 8.1 - Método de Dakin's Branch and Bound holi ")

# Definir el problema de maximización
prob = pulp.LpProblem("Maximizar_P", pulp.LpMaximize)

# Definir variables
x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')
x3 = pulp.LpVariable('x3', lowBound=0, cat='Integer')

# Función objetivo
prob += 4 * x1 + 3 * x2 + 3 * x3

# Restricciones
prob += 4 * x1 + 2 * x2 + x3 <= 10
prob += 3 * x1 + 4 * x2 + 2 * x3 <= 14
prob += 2 * x1 + x2 + 3 * x3 <= 7

# Resolver el problema
prob.solve()

# Mostrar la solución en Streamlit
st.write("Estado:", pulp.LpStatus[prob.status])
st.write("x1 =", x1.varValue)
st.write("x2 =", x2.varValue)
st.write("x3 =", x3.varValue)
st.write("Valor óptimo (P) =", pulp.value(prob.objective))

# Gráfica de la región factible
x_vals = np.linspace(0, 5, 400)
y_vals1 = (10 - 4 * x_vals) / 2
y_vals2 = (14 - 3 * x_vals) / 4
y_vals3 = (7 - 2 * x_vals) / 1

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals1, label="4x1 + 2x2 + x3 ≤ 10")
plt.plot(x_vals, y_vals2, label="3x1 + 4x2 + 2x3 ≤ 14")
plt.plot(x_vals, y_vals3, label="2x1 + x2 + 3x3 ≤ 7")
plt.xlim((0, 5))
plt.ylim((0, 5))
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.title('Región factible')
plt.fill_between(x_vals, np.minimum(np.minimum(y_vals1, y_vals2), y_vals3), alpha=0.3)
st.pyplot(plt)
