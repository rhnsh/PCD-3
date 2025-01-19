import imageio.v3 as i
import numpy as np
image_path = "C:\\Users\\muham\\OneDrive\\Desktop\\bd.jpg"
my_image = i.imread(image_path)

print (my_image.shape[0])
if (len(my_image.shape)<3):
    print("Gambar input harus RGB ")
    exit()
r = my_image[:,:,0]
g = my_image[:,:,1]
b = my_image[:,:,2]

grayscale = 0.2989 * r + 0.5870 * g + 0.1140 * b
grayscale_image = np.stack((grayscale,)*3, axis=-1).astype(np.uint8)
i.imwrite("C:\\Users\\muham\\OneDrive\\Desktop\\gs.jpg", grayscale_image)