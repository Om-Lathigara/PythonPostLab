import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Replace with actual image paths
img1 = np.array(Image.open(r"C:\Users\aumla\Downloads\MU.jpg"))
img2 = np.array(Image.open(r"C:\Users\aumla\Downloads\MU.jpg"))
# plt.imshow(img1-img2)
# plt.show()

# newImage = Image.new("L", (200, 200), "white")
# newImage.show()

# from PIL import Image, ImageDraw
# width, height = 200, 200
# image = Image.new("RGB", (width, height), "white")
# draw = ImageDraw.Draw(image)
# draw.rectangle([0,0,width//2,height], fill="black")
# draw.rectangle([width//2,0,width,height], fill="white")
# image.show()
# image.save("checkerboard.png")

# from PIL import Image
# img = Image.open(r"C:\Users\aumla\Downloads\MU.jpg")
# resized_img = img.resize((100, 100))
# resized_img.show()

# from PIL import Image
# img = Image.open(r"C:\Users\aumla\Downloads\MU.jpg")
# resized_img = img.resize((1024, 800)) 


from PIL import Image, ImageChops
# img1 = Image.open(r"C:\Users\aumla\Downloads\MU.jpg".resize((300, 300)))
# img2 = Image.open(r"C:\Users\aumla\Downloads\MU.jpg".resize((300, 300)))
# added_image = ImageChops.add(img1, img2)
# added_image.show()

# subtracted_image = ImageChops.subtract(img1, img2)
# subtracted_image.show()
img1 = Image.open(r"C:\Users\aumla\Downloads\MU.jpg")

gray = img1.convert("L")
gray.show()

r,g,b= img1.split()

red_image = Image.merge("RGB", (r, Image.new('L', r.size), Image.new('L', r.size)))
green_image = Image.merge("RGB", (Image.new('L', g.size), g, Image.new('L', g.size)))
blue_image = Image.merge("RGB", (Image.new('L', b.size), Image.new('L', b.size), b))

red_image.show(title="Red Channel")
green_image.show(title="Green Channel")
blue_image.show(title="Blue Channel")

merged_image = Image.merge("RGB", (r, g, b))
merged_image.show(title="Merged Image")