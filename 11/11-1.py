from PIL import Image
import numpy as np

img = Image.open(r"C:\Users\aumla\Downloads\MU.jpg")
img_array = np.array(img)

print("Dimensions:", img_array.shape)
print("Height:", img_array.shape[0])
print("Width:", img_array.shape[1])
if img_array.ndim == 3:
    print("Channels:", img_array.shape[2])
    print("Min Blue:", img_array[:, :, 2].min())
