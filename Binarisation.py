import cv2
import numpy as np

class Binarisation:
    def __init__(self,image):
        self.image = image

    def Seuillage(self,s):
         imageX = self.image.copy()
         for i in range(1,imageX.shape[0]):
            for j in range(1,imageX.shape[1]):
                if imageX[i,j] < s:
                    imageX[i, j] = 0
                else:
                    imageX[i, j] = 255
         return imageX

    def Otsu(self):
        pixel_number = self.image.shape[0] * self.image.shape[1]
        mean_weigth = 1.0 / pixel_number
        his, bins = np.histogram(self.image, np.arange(0, 257))
        final_thresh = -1
        final_value = -1
        intensity_arr = np.arange(256)
        for t in bins[1:-1]:  # This goes from 1 to 254 uint8 range (Pretty sure wont be those values)
            pcb = np.sum(his[:t])
            pcf = np.sum(his[t:])
            Wb = pcb * mean_weigth
            Wf = pcf * mean_weigth

            mub = np.sum(intensity_arr[:t] * his[:t]) / float(pcb)
            muf = np.sum(intensity_arr[t:] * his[t:]) / float(pcf)
            # print mub, muf
            value = Wb * Wf * (mub - muf) ** 2

            if value > final_value:
                final_thresh = t
                final_value = value
        final_img = self.image.copy()
        print(final_thresh)
        final_img[self.image > final_thresh] = 255
        final_img[self.image < final_thresh] = 0
        return final_img