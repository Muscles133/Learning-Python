import sys
import csv
from PIL import Image




in_file = "before1.jpg" #sys.argv[1]
out_file = "after1.jpg" #sys.argv[2]


with Image.open(in_file) as im:
    #(width, height) = (im.width//2, im.height//2)
    target_size = (600, 600)
    img_resized = im.resize((im.width // 2, im.height // 2))

     # Calculate dimensions for cropping
    width, height = img_resized.size
    left = 0
    top = (height - target_size[1]) // 2
    right = target_size[0]
    bottom = top + target_size[1]

    # Crop the image
    img_cropped = img_resized.crop((left, top, right, bottom))
    


img_cropped.save(out_file, format='JPEG')
