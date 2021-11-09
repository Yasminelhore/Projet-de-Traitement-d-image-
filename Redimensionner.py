from scipy import misc
import sys
from PIL import Image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


class redimensionner:
    def __init__(self, image):
        self.image = Image.open(image)
    def redi(self):
        imgF = self.image.resize((100 , 120))
        return imgF


"""
ImageFile = 'C:/Users/Omar ETTARGUY/PycharmProjects/traitement/Group/test.jpg'
c1 = redimensionner(ImageFile)
imgF = c1.redi()
plt.imshow(imgF)
plt.show()
"""