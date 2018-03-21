import sys
from PIL import Image
import numpy as np

img=Image.open('westbrook.jpg')

width  = img.size[0]
height = img.size[1]

output_img = Image.new('RGB', img.size, (255, 255, 255))
input_array = np.array(img)

output_array = np.array(input_array/2,dtype=np.uint8)
#output_array = np.array(np.floor(input_array/2),dtype=np.uint8)

output_img = Image.fromarray(output_array)
output_img.save('q2.jpg', 'jpeg')