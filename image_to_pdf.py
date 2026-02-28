from PIL import Image

images = [  "img1.jpeg"]

image_list = [Image.open(img).convert("RGB") for img in images]

image_list[0].save("Bonafide.pdf", save_all=True, append_images=image_list[1:])
