import math
import cv2
from matplotlib.pyplot import *

class Filtrage:
    def __init__(self,image):
        self.image = image

    def Moyenneur(self, taille):
        imagefiltrage= self.image.copy()
        x = int((taille - 1 )/2)
        for i in range(x, self.image.shape[0] - x):
            for j in range(x, self.image.shape[1] - x):
                s=0
                for n in range(-x, x):
                    for m in range(-x, x):
                        s += self.image[i+n,j+m]/(taille*taille)
                imagefiltrage[i,j] = s
                s=0
        return imagefiltrage

    def Median(self, taille):
        imagefiltrage = self.image.copy()
        x = int((taille - 1) / 2)
        for i in range(x, self.image.shape[0] - x):
            for j in range(x, self.image.shape[1] - x):
                liste = []
                if imagefiltrage[i, j] == 0 or imagefiltrage[i, j] == 255:
                    for n in range(-x, x):
                        for m in range(-x, x):
                            liste.append(imagefiltrage[i + n, j + m])
                    liste.sort()
                    imagefiltrage[i, j] = liste[x + 1]
                    while len(liste) > 0: liste.pop()
        return imagefiltrage

    def h(self,x,y,v):
        x =(1/(2*math.pi*math.pow(v,2)))*(math.exp(-(math.pow(x,2)+math.pow(y,2))/(2*math.pow(v,2))))
        return x

    def Gaussien(self,v):
        imagefiltrage = self.image.copy()
        x = 1
        for i in range(x, self.image.shape[0] - x):
            for j in range(x, self.image.shape[1] - x):
                s=0
                for a in range(-x, x):
                    for b in range(-x, x):
                        s = s + self.h(a, b, v)*self.image[i+a, j+b]
                imagefiltrage[i, j] = s
                s=0
        return imagefiltrage
