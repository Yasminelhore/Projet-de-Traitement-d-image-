from numpy import *
import cv2
from matplotlib.pyplot import *
import matplotlib.pyplot as plt

class Contours:

    def __init__(self,image):
        self.image = image

    def grad(self,seuil):
        imageX = self.image.copy()
        imageY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageX[i, j] = self.image[i, j+1] -self.image[i, j]
                imageY[i, j] = self.image[i+1,j] -self.image[i, j]
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = sqrt(imageX[i, j] ** 2 + imageY[i, j] ** 2)
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def Robert(self,seuil):
        imageX = self.image.copy()
        imageY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageX[i, j] = self.image[i, j] - self.image[i - 1, j - 1]
                imageY[i, j] = self.image[i, j] - self.image[i + 1, j + 1]
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = sqrt(imageX[i, j] ** 2 + imageY[i, j] ** 2)
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def Sobel(self,seuil):
        imageX = self.image.copy()
        imageY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageY[i, j] = -self.image[i-1, j-1] -2*self.image[i, j-1] -self.image[i+1, j-1] \
                               + self.image[i - 1, j + 1] +2*self.image[i, j + 1] +self.image[i + 1, j + 1]
                imageX[i, j] = self.image[i-1, j-1] + 2*self.image[i-1, j] +self.image[i - 1, j + 1]\
                                -self.image[i+1, j-1] - 2*self.image[i+1, j] - self.image[i + 1, j + 1]
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = sqrt(imageX[i, j] ** 2 + imageY[i, j] ** 2)
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def Laplacien(self,seuil):
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = -4*self.image[i, j] +self.image[i-1, j] +self.image[i+1, j] \
                               + self.image[i , j - 1] +self.image[i, j + 1]
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY
