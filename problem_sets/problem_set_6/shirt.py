import sys
from PIL import Image, ImageOps

# checking file name and argv number
if len(sys.argv) != 3:
    sys.exit(1)

#read file names
file_input = sys.argv[1]
file_output = sys.argv[2]

#check if input filename is valid
list_1 = file_input.split('.')
ext = list_1[len(list_1)-1]
if ext not in ["jpeg", "jpg","png"]:
    sys.exit(1)


#check if output filename is same as input
list_1 = file_output.split('.')
ext2 = list_1[len(list_1)-1]
if ext != ext2:
    sys.exit(1)


# creating the new image with the shirt
image_object = Image.open(file_input)
shirt_obg = Image.open("shirt.png")

shirt_size = shirt_obg.size
image_object = ImageOps.fit(image_object, shirt_size)
image_object.paste(shirt_obg, shirt_obg)

image_object.save(file_output)
