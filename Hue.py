import cv2
import numpy as np

def GetHue(image):
    image = image[5:10,5:10,:]
    height, width, channel = image.shape
    image_si = image.copy();
    for i in xrange(height):
        for j in xrange(width):
            for k in xrange(channel):
                if (image_si[i,j,k] < 0.5):
                    image_si[i,j,k] = 1 - image_si[i,j,k]
    image = np.uint8(image * 255.0)
    image_si = np.uint8(image_si * 255.0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    image_si = cv2.cvtColor(image_si, cv2.COLOR_BGR2HLS)
    
    Hue = image[:,:,0]
    Hue_si = image_si[:,:,0]
    Hue = Hue / 180.0
    Hue_si = Hue_si / 180.0
    JHue = np.abs(Hue - Hue_si)
    return JHue