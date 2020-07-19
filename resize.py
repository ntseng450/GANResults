from PIL import Image
import os, sys

path = "../SPADE/datasets/CamVid/LabeledApproved_full/"
dirs = os.listdir( path )

def resize():
    i = 0
    for item in dirs:
        if os.path.isfile(path+item):
            i = i+1
            im = Image.open(path+item).convert("RGB")
            f, e = os.path.splitext(path+item)
            imResize = im.resize((256,256), Image.ANTIALIAS)
            imResize.save('resizedData/mask' + str(i) + '.jpg', 'JPEG', quality=90)

resize()
