import numpy as np
import cv2
import sklearn,skimage.measure
import pandas as pd 
from matplotlib import pyplot as plt
import os

def showImage(img):
    plt.imshow(img)
    plt.show()

img_array=cv2.imread('sample.jpg')
showImage(img_array)
downsample = 2
# first, change to 0-1
ds_array = img_array/255
r = skimage.measure.block_reduce(ds_array[:, :, 0],(downsample, downsample),np.mean)
g = skimage.measure.block_reduce(ds_array[:, :, 1],(downsample, downsample),np.mean)
b = skimage.measure.block_reduce(ds_array[:, :, 2],(downsample, downsample),np.mean)
ds_array = np.stack((r, g, b), axis=-1)
showImage(ds_array)
cv2.imwrite('output.jpg', ds_array)



import numpy as np
import cv2
import sklearn,skimage.measure
import pandas as pd 
from matplotlib import pyplot as plt
import os
import imageio

def showImage(img):
    plt.imshow(img)
    plt.show()

img_array=cv2.imread('sample.jpg')
# showImage(img_array)
downsample = 2
# first, change to 0-1
ds_array = img_array/255
b = skimage.measure.block_reduce(ds_array[:, :, 0],(downsample, downsample),np.mean)
g = skimage.measure.block_reduce(ds_array[:, :, 1],(downsample, downsample),np.mean)
r = skimage.measure.block_reduce(ds_array[:, :, 2],(downsample, downsample),np.mean)
ds_array = np.stack((r, g, b), axis=-1)
showImage(ds_array)
imageio.imwrite('output.jpg', ds_array)