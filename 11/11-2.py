from PIL import Image, ImageOps

img = Image.open(r"C:\Users\aumla\Downloads\MU.jpg")
padded = ImageOps.expand(img, border=(100, 50, 100, 50), fill='black')
padded.show()
