import numpy as np
import matplotlib.pyplot as plt

points = np.array([
    [0, 0],   # A
    [4, 0],   # B
    [4, 2],   # C
    [0, 2],   # D
    [0, 0]    # kembali ke A untuk menutup bentuk
])

theta_deg = 30
theta = np.radians(theta_deg)

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

t = np.array([3, 2])

rotated_points = points @ R.T
transformed_points = rotated_points + t

plt.figure(figsize=(6,6))
plt.plot(points[:,0], points[:,1], 'bo--', label='Asli')
plt.plot(transformed_points[:,0], transformed_points[:,1], 'ro--', label=f'Rotasi {theta_deg}°')

plt.gca().set_aspect('equal', adjustable='box')
plt.title("Transformasi Rotasi Persegi Panjang")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()