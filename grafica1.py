import numpy as np
import matplotlib.pyplot as plt

# ---- Datos de la Tabla 1 ---- con el plano inclinado de 8 grados
d = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])                     # distancia [m]
t_exp = np.array([1.022, 1.886, 2.268, 2.688, 2.952, 2.966])     # tiempo medido [s]
t_teo = np.array([0.85, 1.209, 1.481, 1.710, 1.912, 2.094])      # tiempo teórico [s]
a_teo = 1.368  

# ---- Aceleraciones experimentales ----
a_exp = 2 * d / t_exp**2
print("Aceleraciones experimentales:", np.round(a_exp, 3))
print(f"Promedio: {a_exp.mean():.3f} m/s²")
 
# Ajuste por mínimos cuadrados de d = ½·a·t² (parábola por el origen)
a_ajuste = 2 * np.sum(d * t_exp**2) / np.sum(t_exp**4)
print(f"Aceleración por ajuste: {a_ajuste:.3f} m/s²")
 
# ---- Gráfica ----
t = np.linspace(0, 3.2, 300)
 
fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(t, 0.5 * a_teo * t**2, color="tab:blue", label=f"Teórica (a = {a_teo} m/s²)")
ax.plot(t_teo, d, "s", color="tab:blue", markersize=6)
ax.plot(t_exp, d, "o", color="tab:red", markersize=7, label="Experimental (mediciones)")
ax.plot(t, 0.5 * a_ajuste * t**2, "--", color="tab:red",
        label=f"Ajuste experimental (a = {a_ajuste:.3f} m/s²)")
 
ax.set_title("Tabla 1 – Distancia vs. tiempo (MRUV)")
ax.set_xlabel("Tiempo [s]")
ax.set_ylabel("Distancia [m]")
ax.set_xlim(0, 3.2)
ax.set_ylim(0, 3.3)
ax.grid(True, alpha=0.4)
ax.legend()
 
plt.tight_layout()
plt.savefig("grafico_tabla1.png", dpi=200)
plt.show()