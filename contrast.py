import math
import numpy as np

def GetVariance(image, s=5):
    height, width, channel = image.shape
    var_image = np.zeros((height, width))
    pad_size = math.floor(s / 2.0)
    padimage_r = np.pad(image[:,:,0], (pad_size, pad_size), 'constant', constant_values=(np.inf, np.inf))
    padimage_g = np.pad(image[:,:,1], (pad_size, pad_size), 'constant', constant_values=(np.inf, np.inf))
    padimage_b = np.pad(image[:,:,2], (pad_size, pad_size), 'constant', constant_values=(np.inf, np.inf))
    padimage = np.zeros((height+pad_size*2,width+pad_size*2, 3))
    padimage[:,:,0] = padimage_r
    padimage[:,:,1] = padimage_g
    padimage[:,:,2] = padimage_b
    for i in xrange(height):
        for j in xrange(width):
            patch = padimage[i:i+s, j:j+s,:]
            center = np.ones((s,s,channel))*image[i,j,:]
            var = (patch - center) ** 2
            var = var[var <= 1]
            var_image[i,j] =  math.sqrt( np.sum(var) / var.shape )
    return var_image
            
def GetContrast(image, scale=10):
    var_image = GetVariance(image)
    JCon = np.zeros((5, 5))
    pad_size = np.floor(scale/2.0)
    padimage = var_image[(5-pad_size):(10+pad_size), (5-pad_size):(10+pad_size)]
    for i in xrange(5):
        for j in xrange(5):
            patch = padimage[i:(i+scale), j:(j+scale)]
            JCon[i,j] = np.max(patch)
    return JCon