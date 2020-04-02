from PIL import Image
from PIL.ImageOps import mirror

img_file_1, img_file_2 = ['images/generic-fire.jpg', 'images/Large_bonfire.jpg']


def open_and_mirror(img):
    im = Image.open(img)
    return mirror(im)


def combine_h(im1, im2):
    combined = Image.new('RGB', (im1.width + im2.width, min(im1.height, im2.height)))
    combined.paste(im1, (0, 0))
    combined.paste(im2, (im1.width, 0))
    return combined


result = combine_h(open_and_mirror(img_file_1), open_and_mirror(img_file_2))
result.save('processed-images/new_processed_image.png')
