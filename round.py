# http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/data/label_colors.txt
import numpy as np
import os
from PIL import Image

convertSet = {(64, 128, 64), (192, 0, 128), (0, 128, 192), (0, 128, 64), (128, 0, 0),
              (64, 0, 128), (64, 0, 192), (192, 128, 64), (192, 192, 128), (64, 64, 128),
              (128, 0, 192), (192, 0, 64), (128, 128, 64), (192, 0, 192), (128, 64, 64),
              (64, 192, 128), (64, 64, 0), (128, 64, 128), (128, 128, 192), (0, 0, 192),
              (192, 128, 128), (128, 128, 128), (64, 128, 192), (0, 0, 64), (0, 64, 64),
              (192, 64, 128), (128, 128, 0), (192, 128, 192), (64, 0, 64), (192, 192, 0),
              (0, 0, 0), (64, 192, 0)}

convertArr = np.array([[64, 128, 64], [192, 0, 128], [0, 128, 192], [0, 128, 64], [128, 0, 0],
              [64, 0, 128], [64, 0, 192], [192, 128, 64], [192, 192, 128], [64, 64, 128],
              [128, 0, 192], [192, 0, 64], [128, 128, 64], [192, 0, 192], [128, 64, 64],
              [64, 192, 128], [64, 64, 0], [128, 64, 128], [128, 128, 192], [0, 0, 192],
              [192, 128, 128], [128, 128, 128], [64, 128, 192], [0, 0, 64], [0, 64, 64],
              [192, 64, 128], [128, 128, 0], [192, 128, 192], [64, 0, 64], [192, 192, 0],
              [0, 0, 0], [64, 192, 0]])

def main():
  	counter = 0
	imagefoldername = 'first_fifty_fakes'
	savefoldername = 'fff_rounded'
	for filename in os.listdir(imagefoldername):
    	img = Image.open(imagefoldername + '/' +filename)
    	arr = np.array(img)
   	 	pixelwise_rounding(arr)
    	traverse_img(arr)
    	save(arr, savefoldername, counter)
        counter += 1


def traverse_img(arr):
    width, height = arr.shape[0], arr.shape[1]
    counter = 0
    for x in range(width):
        for y in range(height):
            r = arr[x][y][0]
            g = arr[x][y][1]
            b = arr[x][y][2]
            if (r, g, b) in convertSet:
                counter += 1
    print(counter / (width * height))

def pixelwise_rounding(arr):
    width, height = arr.shape[0], arr.shape[1]
    for x in range(width):
        for y in range(height):
            diffs = np.sum(np.absolute(convertArr - arr[x, y, :]), axis=1)
            idx = np.argmin(diffs)
            arr[x, y, :] = convertArr[idx, :]

def save(arr, savefoldername, counter):
    im = Image.fromarray(arr)
    im.save(savefoldername + '/rounded' + str(counter) + ".png")


if __name__ == "__main__":
    main()
