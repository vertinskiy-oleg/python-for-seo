from PIL import Image


img_file = 'images/Green-Python-h.jpg'

im = Image.open(img_file)

old_w, old_h = im.size
new_size = (old_w//2, old_h//2)
new_img = im.resize(new_size)

new_img = new_img.rotate(3)
new_img = new_img.crop((40, 40, new_size[0]-40, new_size[1]-40))

new_img.show()

new_img.save(f'resized/new_resized_image.png')

breakpoint()
