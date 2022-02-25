import numpy as np
import cv2
import sklearn,skimage.measure
import pandas as pd 
from matplotlib import pyplot as plt
import os
import imageio
from skimage import img_as_ubyte
capture = cv2.VideoCapture('sample_video.mp4')
frameNr = 0
while (True):
    success, frame = capture.read()
    if success:
        cv2.imwrite(f'video/{frameNr}.jpg', frame)
        img=cv2.imread(f"video/{frameNr}.jpg")
        downsample = 2
        ds_array = img/255
        b = skimage.measure.block_reduce(ds_array[:, :, 0],(downsample, downsample),np.mean)
        g = skimage.measure.block_reduce(ds_array[:, :, 1],(downsample, downsample),np.mean)
        r = skimage.measure.block_reduce(ds_array[:, :, 2],(downsample, downsample),np.mean)
        ds_array = np.stack((r, g, b), axis=-1)
        imageio.imwrite(f"down/{frameNr}.jpg", img_as_ubyte(ds_array))
    else:
        break
    frameNr = frameNr+1
capture.release()





import numpy as np
import skvideo.io
   
out_video =  np.empty([330, 180, 320, 3], dtype = np.uint8)
out_video =  out_video.astype(np.uint8)
  
for i in range(0,330):
  img = cv2.imread(f"down/{i}.jpg")
  out_video[i] = img

skvideo.io.vwrite("video.mp4", out_video)