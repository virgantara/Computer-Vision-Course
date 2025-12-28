import numpy as np

np.random.seed(0)

N = 50

# Contoh Flat

Ix_flat = np.random.normal(0, 0.2, N)
Iy_flat = np.random.normal(0, 0.2, N)


grad_flat = np.column_stack((Ix_flat, Iy_flat))

# print("Flat region (Ix, Iy) sample:")
# print(grad_flat[:5])


# Contoh Edge
Ix_edge = np.random.normal(5, 0.5, N)   
Iy_edge = np.random.normal(0, 0.2, N)

grad_edge = np.column_stack((Ix_edge, Iy_edge))

# print("\nEdge region (Ix, Iy) sample:")
# print(grad_edge[:5])

# Contoh Corner
Ix_corner = np.random.normal(5, 0.5, N)
Iy_corner = np.random.normal(5, 0.5, N)

grad_corner = np.column_stack((Ix_corner, Iy_corner))

# print("\nCorner region (Ix, Iy) sample:")
# print(grad_corner[:5])


def center_data(G):
    return G - G.mean(axis=0)


def compute_M(Ix, Iy, center=True, average=False):
    """
    Compute structure tensor / gradient covariance matrix M from Ix and Iy.

    center  : if True, subtract mean from Ix and Iy (remove DC offset)
    average : if True, return average (divide by N). If False, return sum as in slide.
    """
    Ix = np.asarray(Ix, dtype=float).ravel()
    Iy = np.asarray(Iy, dtype=float).ravel()

    if center:
        Ix = Ix - Ix.mean()
        Iy = Iy - Iy.mean()

    # Build M
    M = np.array([
        [np.sum(Ix * Ix), np.sum(Ix * Iy)],
        [np.sum(Ix * Iy), np.sum(Iy * Iy)]
    ])

    if average:
        N = Ix.size
        M = M / N

    return M

def eig_info(M):
    # eigh  untuk matriks simetris: eigenvalue terurut naik
    w, V = np.linalg.eigh(M)
    # urutkan dari besar ke kecil agar enak dibaca
    idx = np.argsort(w)[::-1]
    w = w[idx]
    V = V[:, idx]
    return w, V

# def classify_by_eigenvalues(l1, l2, t_flat=1.0, t_corner=10.0):
#     """
#     Aturan sederhana berbasis skala.
#     - flat   : l1 < t_flat dan l2 < t_flat
#     - edge   : l1 >= t_corner dan l2 < t_flat (atau sebaliknya)
#     - corner : l1 >= t_corner dan l2 >= t_corner
#     Catatan: threshold tergantung normalisasi & data (ini demo).
#     """
#     if l1 < t_flat and l2 < t_flat:
#         return "FLAT"
#     if (l1 >= t_corner and l2 < t_flat) or (l2 >= t_corner and l1 < t_flat):
#         return "EDGE"
#     if l1 >= t_corner and l2 >= t_corner:
#         return "CORNER"
#     return "INTERMEDIATE"


# grad_flat_c   = center_data(grad_flat)
# grad_edge_c   = center_data(grad_edge)
# grad_corner_c = center_data(grad_corner)
M_flat   = compute_M(Ix_flat, Iy_flat, center=True, average=True)
M_edge   = compute_M(Ix_edge, Iy_edge, center=True, average=True)
M_corner = compute_M(Ix_corner, Iy_corner, center=True, average=True)

def harris_response(M, k=0.04):
    return np.linalg.det(M) - k * (np.trace(M) ** 2)

Rs = []
for M in [M_flat, M_edge, M_corner]:
    Rs.append(harris_response(M))

Rs = np.array(Rs)
print("All R:", Rs)

# threshold relatif
t = 0.5 * np.max(Rs)

for name, R in zip(["flat","edge","corner"], Rs):
    cls = "CORNER" if R > t else "NOT CORNER"
    print(name, R, " ~ ", cls)
