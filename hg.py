import imageio.v3 as i
import numpy as np
import matplotlib.pyplot as plt

# Ganti dengan path gambar kamu
path = "C:\\Users\\muham\\OneDrive\\Desktop\\gs.jpg"

# Memuat gambar
ine = i.imread(path)

gray=ine[:,:,0]

rG_hist,bins = np.histogram(gray.flatten(),bins=256, range=[0,256])


rgnorm = rG_hist / rG_hist.sum()

plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title('Gambar Grayscale')


plt.subplot(2, 2, 2)
plt.plot(rG_hist, color='red')
plt.title('Histogram Gambar Grayscale')

plt.subplot(2, 2, 3)
plt.plot(rgnorm, color='red')
plt.title('Histogram Normalisasi Gambar Grayscale')

print(rG_hist)

plt.tight_layout()
plt.show()


for intensity in range(256):
    print(f'Intensitas {intensity}: {rG_hist[intensity]}')