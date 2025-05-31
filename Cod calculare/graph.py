import numpy as np
import matplotlib.pyplot as plt

# CONSTANTE
u = 1676       # viteza gazelor evacuate (m/s)
P = 5000       # payload (kg)
k = 5          # raport structural
v_target = 7840  # viteză orbitală dorită (m/s)

# FUNCȚIE: calculează viteza finală
def compute_velocity(m1, m2, m3):
    term1 = np.log((k*m1 + k*m2 + k*m3 + P) / (k*m2 + k*m3 + P))
    term2 = np.log((k*m2 + k*m3 + P) / (k*m3 + P))
    term3 = np.log((k*m3 + P) / P)
    return u * (term1 + term2 + term3)

# ---------------------
# GRAFIC 1: Viteză finală în funcție de m1 și m2 (cu m3 fix)
# ---------------------
m1_vals = np.linspace(100, 5000, 50)
m2_vals = np.linspace(100, 5000, 50)
m1_grid, m2_grid = np.meshgrid(m1_vals, m2_vals)
m3_fixed = 2000  # m3 fix pentru ca nu merge

v_grid = compute_velocity(m1_grid, m2_grid, m3_fixed)

plt.figure(figsize=(10, 6))
contour = plt.contourf(m1_grid, m2_grid, v_grid, levels=30, cmap='plasma')
plt.colorbar(contour, label='Viteza finală (m/s)')
plt.title('Viteza finală în funcție de m1 și m2 (m3 = 2000 kg)')
plt.xlabel('m1 (kg)')
plt.ylabel('m2 (kg)')
plt.grid(True)
plt.tight_layout()
plt.savefig("viteza_vs_m1_m2.png")
plt.show()

# ---------------------
# GRAFIC 2: Masa totală minimă în funcție de m3
# ---------------------
m3_vals = np.linspace(1000, 15000, 60)
m_total_vals = []

for m3 in m3_vals:
    best_diff = np.inf
    best_total_mass = np.nan
    for m1 in np.linspace(1000, 15000, 40):
        for m2 in np.linspace(1000, 15000, 40):
            v = compute_velocity(m1, m2, m3)
            total_mass = k * (m1 + m2 + m3) + P
            diff = abs(v - v_target)
            if diff < best_diff:
                best_diff = diff
                best_total_mass = total_mass
    m_total_vals.append(best_total_mass)

plt.figure(figsize=(10, 6))
plt.plot(m3_vals, m_total_vals, marker='o', color='green')
plt.title('Masa totală minimă în funcție de m3 (pentru viteză orbitală)')
plt.xlabel('m3 (kg)')
plt.ylabel('Masa totală (kg)')
plt.grid(True)
plt.tight_layout()
plt.savefig("masa_vs_m3.png")
plt.show()
