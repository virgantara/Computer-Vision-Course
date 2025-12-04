import numpy as np
import matplotlib.pyplot as plt

points = np.array([
    [0, 0],   # A
    [4, 0],   # B
    [4, 2],   # C
    [0, 2],   # D
    [0, 0]    # kembali ke A untuk menutup bentuk
])

points_homogen = np.hstack([points, np.ones((points.shape[0], 1))])

# matriks homografi
H = np.array([
    [1.0, 0.2, 2.0],
    [0.1, 1.0, 1.0],
    [0.001, 0.002, 1.0]
])


transformed_homogen = (H @ points_homogen.T).T

# normalisasi ke koordinat biasa (inhomogen)
transformed_points = transformed_homogen[:, :2] / transformed_homogen[:, 2, np.newaxis]

plt.figure(figsize=(6,6))
plt.plot(points[:,0], points[:,1], 'bo--', label='Asli')
plt.plot(transformed_points[:,0], transformed_points[:,1], 'ro--', label=f'Projective')

plt.gca().set_aspect('equal', adjustable='box')
plt.title("Transformasi Proyektif (Homografi / Perspektif)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()