from PIL import Image
import matplotlib.pyplot as plt

img = Image.open(r"C:\Users\aumla\Downloads\MU.jpg").convert("RGB")
r, g, b = img.split()

plt.imshow(img)
plt.show()

plt.imshow(r, cmap="Reds")
plt.show()

plt.imshow(g, cmap="Greens")
plt.show()

plt.imshow(b, cmap="Blues")
plt.show()
