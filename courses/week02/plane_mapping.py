import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('papancatur1.png')

h, w, _ = img.shape
print("Ukuran gambar:", w, "x", h)

# urutan: kiri-atas, kanan-atas, kanan-bawah, kiri-bawah
src_points = np.float32([
    [48, 4],    # kiri atas
    [284, 4],   # kanan atas
    [320, 200], # kanan bawah
    [5, 200]    # kiri bawah
])


# misal hasilnya ingin kita buat 400x400 piksel
dst_points = np.float32([
    [0, 0],
    [400, 0],
    [400, 400],
    [0, 400]
])


# --- 3. Hitung matriks homografi (H) ---
H, status = cv2.findHomography(src_points, dst_points)

print("Matriks Homografi (H):\n", H)

corrected = cv2.warpPerspective(img, H, (400, 400))

# --- 6. Tampilkan hasil ---
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Papan Asli (Miring)")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(corrected, cv2.COLOR_BGR2RGB))
plt.title("Hasil Koreksi Perspektif (Lurus)")
plt.show()