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