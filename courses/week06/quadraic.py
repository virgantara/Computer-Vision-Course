import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_error_surface(M, title):
    u = np.linspace(-5, 5, 20)
    v = np.linspace(-5, 5, 20)
    U, V = np.meshgrid(u, v)

    E = M[0,0]*U**2 + 2*M[0,1]*U*V + M[1,1]*V**2

    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(U, V, E, cmap='viridis', edgecolor='none')
    ax.set_title(title)
    ax.set_xlabel('u')
    ax.set_ylabel('v')
    ax.set_zlabel('E(u,v)')
    plt.tight_layout()
    plt.show()

M_flat = np.array([[1, 0],
                   [0, 1]])

plot_error_surface(M_flat, "Flat Region (λ1 ≈ λ2 ≈ small)")

M_edge = np.array([[10, 0],
                   [0, 0.5]])

plot_error_surface(M_edge, "Edge (λ1 >> λ2)")

M_corner = np.array([[10, 0],
                     [0, 10]])

plot_error_surface(M_corner, "Corner (λ1 ≈ λ2 >> 0)")

