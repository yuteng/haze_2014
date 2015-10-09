import math
import numpy as np

def GetSaturation(image, scale=10):
    height, width, __ = image.shape
    JSat = np.zeros((height, width))
    for i in xrange(height):
        for j in xrange(width):
            JSat[i, j] = 1 - zero_dive(np.min(image[i,j,:]) , np.max(image[i,j,:]))
    pad_size = math.floor(scale/2.0)
    padimage = JSat[(5-pad_size):(10+pad_size), (5-pad_size):(10+pad_size)]
    JSat = np.zeros((5, 5))
    for i in xrange(5):
        for j in xrange(5):
            patch = padimage[i:(i+scale), j:(j+scale)]
            JSat[i,j] = np.max(patch)
    return JSat

def zero_dive(a,b):
    if(b != 0 ):
        return (a * 1.0)/b
    else:
        return 1
