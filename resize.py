import os
import imageio
import numpy as np
import PIL
from PIL import ImageOps
from PIL import Image
import sys

"""
def resize_image(image, image_width = 128,image_height = 128):
    # Lee una imagen y la coloca en I
    I = imageio.imread(image)
    # En imageOps.fit necesito una imagen tipo PIL, paso de tipo imageio a array y luego a PIL
    I = np.asarray(I)
    I = PIL.Image.fromarray(I)
    # ImageOps.fit le hace un resize
    I = ImageOps.fit(I, [image_width,image_height])
    # Vuelve a convertirlo en un Numpy array
    I = np.array(I)
    imageio.imwrite("resize"+image, I)
    
    return
"""
def resize_image(image, image_width = 128,image_height = 128):
    imageFile = image
    im1 = Image.open(imageFile)
    # adjust width and height to your needs
    width = image_width
    height = image_height
    # use one of these filter options to resize the image
    im2 = im1.resize((width, height), Image.NEAREST)      # use nearest neighbour
    im3 = im1.resize((width, height), Image.BILINEAR)     # linear interpolation in a 2x2 environment
    im4 = im1.resize((width, height), Image.BICUBIC)      # cubic spline interpolation in a 4x4 environment
    im5 = im1.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
    ext = image[-4:]
    im2.save("1NEAREST" +image[:-5] + ext)
    im3.save("1BILINEAR" + image[:-5] +ext)
    im4.save("1BICUBIC" +image[:-5] + ext)
    im5.save("1ANTIALIAS" + image[:-5] +ext)
    
    return


resize_image(sys.argv[1],int(sys.argv[2]), int(sys.argv[3]))