from PIL import Image

images = [  "id1.jpg","id2.jpg"]

image_list = [Image.open(img).convert("RGB") for img in images]

image_list[0].save("identity.pdf", save_all=True, append_images=image_list[1:])



