import numpy as np
import matplotlib.pyplot as plt

# ---------------------
# CONSTANTE
# ---------------------
u = 1676       # viteza gazelor evacuate (m/s)
P = 5000       # payload (kg)
k = 5          # raport structural (total/m combustibil)
v_target = 7840  # viteza finală dorită (m/s)

# ---------------------
# FUNCȚIE: Calculează viteza finală
# ---------------------
def compute_velocity(m1, m2, m3):
    term1 = np.log((k*m1 + k*m2 + k*m3 + P) / (k*m2 + k*m3 + P))
    term2 = np.log((k*m2 + k*m3 + P) / (k*m3 + P))
    term3 = np.log((k*m3 + P) / P)
    return u * (term1 + term2 + term3)

# ---------------------
# GRAFIC 1: Viteza finală în funcție de m1 și m2 (m3 fix)
# ---------------------
m1_vals = np.linspace(100, 5000, 50)
m2_vals = np.linspace(100, 5000, 50)
m1_grid, m2_grid = np.meshgrid(m1_vals, m2_vals)
m3_fixed = 2000  # m3 fixat pentru vizualizare

v_grid = compute_velocity(m1_grid, m2_grid, m3_fixed)

plt.figure(figsize=(10, 6))
contour = plt.contourf(m1_grid, m2_grid, v_grid, levels=30, cmap='plasma')
plt.colorbar(contour, label='Viteza finală (m/s)')
plt.title('Viteza finală în funcție de m1 și m2 (m3 = 2000 kg)')
plt.xlabel('m1 (kg)')
plt.ylabel('m2 (kg)')
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------
# GRAFIC 2: Masa totală minimă în funcție de m3 (pentru v_target)
# ---------------------
m3_vals = np.linspace(500, 5000, 50)
m_total_vals = []

for m3 in m3_vals:
    min_mass = np.inf
    found = False
    for m1 in np.linspace(500, 5000, 30):
        for m2 in np.linspace(500, 5000, 30):
            v = compute_velocity(m1, m2, m3)
            if abs(v - v_target) < 100:  # toleranță de 100 m/s
                total_mass = k * (m1 + m2 + m3) + P
                if total_mass < min_mass:
                    min_mass = total_mass
                    found = True
    m_total_vals.append(min_mass if found else np.nan)

plt.figure(figsize=(10, 6))
plt.plot(m3_vals, m_total_vals, marker='o')
plt.title('Masa totală necesară în funcție de m3 (pentru viteză orbitală)')
plt.xlabel('m3 (kg)')
plt.ylabel('Masa totală (kg)')
plt.grid(True)
plt.tight_layout()
plt.show()
