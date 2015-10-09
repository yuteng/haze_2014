import math
import numpy as np

def DarkChannel(image, scale=10):
    JDark = np.zeros((5, 5))
    pad_size = math.floor(scale/2.0)
    padimage = image[(5-pad_size):(10+pad_size), (5-pad_size):(10+pad_size), :]
    for i in xrange(5):
        for j in xrange(5):
            patch = padimage[i:(i+scale), j:(j+scale), :]
            JDark[i,j] = np.min(patch)
    return JDark