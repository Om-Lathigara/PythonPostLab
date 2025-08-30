from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(r"C:\Users\aumla\Downloads\MU.jpg").convert("RGB")
r, g, b = img.split()
r_np, g_np, b_np = np.array(r), np.array(g), np.array(b)

plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1); plt.imshow(img); plt.title("Original"); plt.axis("off")
plt.subplot(2, 2, 2); plt.imshow(r_np, cmap="Reds"); plt.title("Red"); plt.axis("off")
plt.subplot(2, 2, 3); plt.imshow(g_np, cmap="Greens"); plt.title("Green"); plt.axis("off")
plt.subplot(2, 2, 4); plt.imshow(b_np, cmap="Blues"); plt.title("Blue"); plt.axis("off")
plt.show()
