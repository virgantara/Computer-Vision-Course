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

A = np.array([
    [1.2, 0.3, 2], # baris pertama: (skala + shear + translasi x)
    [0.2, 1.1, 1]  # baris pertama: (skala + shear + translasi y)
])

affine_trf = A @ points_homogen.T
transformed_points = affine_trf.T


plt.figure(figsize=(6,6))
plt.plot(points[:,0], points[:,1], 'bo--', label='Asli')
plt.plot(transformed_points[:,0], transformed_points[:,1], 'ro--', label=f'Affine')

plt.gca().set_aspect('equal', adjustable='box')
plt.title("Transformasi Affine Persegi Panjang")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()