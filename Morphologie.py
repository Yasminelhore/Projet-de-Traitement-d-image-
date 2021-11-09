
class Morphologie:

    def __init__(self,image):
        self.image = image

    def dilatation(self, H):
        imagecopy = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                s = 0;
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        s = s + self.image[k, l] * H[k - i + 1][l - j + 1]
                if (s == 0):
                    imagecopy[i][j] = 0
                else:
                    imagecopy[i][j] = 255
        return imagecopy

    def Erosion( self , H):
        imagecopy = self.image.copy()

        for i in range(0, self.image.shape[0]):
            for j in range(0, self.image.shape[1]):
                if (self.image[i][j] > 128):
                    self.image[i][j] = 255
                else:
                    self.image[i][j] = 0

        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                s = 0;
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        s = s + self.image[k, l] * H[k - i + 1][l - j + 1]
                if (s == 2295):
                    imagecopy[i][j] = 255
                else:
                    imagecopy[i][j] = 0
        return imagecopy

    def Ouverture(self, H):
        img = self.Erosion(self.image, H)
        image1 = self.dilatation(img, H)
        return image1

    def Fermeture(self, H):
        img = self.Erosion(self.image, H)
        image1 = self.dilatation(img, H)
        return image1
"""
img = cv2.imread('Morpho.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
m = Morphologie(gray)
H = [[1 ,1 , 1],[1, 1, 1],[1, 1, 1]]
image = m.Fermeture(H)
fig, axs = plt.subplots(2)
axs[0].imshow(gray,cmap='gray')
axs[1].imshow(image,cmap='gray')
show()"""