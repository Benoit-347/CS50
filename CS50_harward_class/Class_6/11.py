#playing with files that are formats other than txt and csv: binary is the primary format
import sys
from PIL import Image
list1 = []
for i in sys.argv[1:]:
    list1.append(Image.open(i))

list1[0].save("costumes.gif", save_all = True, append_images = [list1[1]], duration = 1000, loop = 0) 
# <thumbnail>.save(<file_name>, save_all #to_save_all_frames = <True/False>, append_images = [<list of all frames loaded>], duration = <duration of each frame>, loop = <no. of times to loop> # if argument is zero -> no. = infinite loop)