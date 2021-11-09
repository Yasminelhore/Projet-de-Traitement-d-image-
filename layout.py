# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from operation import *
from filtrage import *
from contour import *

from Binarisation import *
from Morphologie import *
from segmentation import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 693)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ImageOrigine = QtWidgets.QLabel(self.centralwidget)
        self.ImageOrigine.setGeometry(QtCore.QRect(20, 60, 481, 461))
        self.ImageOrigine.setText("")
        self.ImageOrigine.setObjectName("ImageOrigine")
        self.ImageFinale = QtWidgets.QLabel(self.centralwidget)
        self.ImageFinale.setGeometry(QtCore.QRect(550, 60, 481, 461))
        self.ImageFinale.setText("")
        self.ImageFinale.setObjectName("ImageFinale")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(480, 600, 101, 31))
        self.reset.setObjectName("reset")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuOperation = QtWidgets.QMenu(self.menubar)
        self.menuOperation.setObjectName("menuOperation")
        self.menuZoom = QtWidgets.QMenu(self.menuOperation)
        self.menuZoom.setObjectName("menuZoom")
        self.menuRedimentionnenemt = QtWidgets.QMenu(self.menuOperation)
        self.menuRedimentionnenemt.setObjectName("menuRedimentionnenemt")
        self.menuRotation = QtWidgets.QMenu(self.menuOperation)
        self.menuRotation.setObjectName("menuRotation")
        self.menuFiltrage = QtWidgets.QMenu(self.menubar)
        self.menuFiltrage.setObjectName("menuFiltrage")
        self.menuMoyanneur = QtWidgets.QMenu(self.menuFiltrage)
        self.menuMoyanneur.setObjectName("menuMoyanneur")
        self.menuMedian = QtWidgets.QMenu(self.menuFiltrage)
        self.menuMedian.setObjectName("menuMedian")
        self.menuGaussien = QtWidgets.QMenu(self.menuFiltrage)
        self.menuGaussien.setObjectName("menuGaussien")
        self.menuExtraction_contour = QtWidgets.QMenu(self.menubar)
        self.menuExtraction_contour.setObjectName("menuExtraction_contour")
        self.menuMorph_Math = QtWidgets.QMenu(self.menubar)
        self.menuMorph_Math.setObjectName("menuMorph_Math")
        self.menuSegmentation = QtWidgets.QMenu(self.menubar)
        self.menuSegmentation.setObjectName("menuSegmentation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionEnregistrer = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.actionGradiant = QtWidgets.QAction(MainWindow)
        self.actionGradiant.setObjectName("actionGradiant")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionRobert = QtWidgets.QAction(MainWindow)
        self.actionRobert.setObjectName("actionRobert")
        self.actionLaplacien = QtWidgets.QAction(MainWindow)
        self.actionLaplacien.setObjectName("actionLaplacien")
        self.actionErosion = QtWidgets.QAction(MainWindow)
        self.actionErosion.setObjectName("actionErosion")
        self.actionDilatation = QtWidgets.QAction(MainWindow)
        self.actionDilatation.setObjectName("actionDilatation")
        self.actionOuverture = QtWidgets.QAction(MainWindow)
        self.actionOuverture.setObjectName("actionOuverture")
        self.actionFermeture = QtWidgets.QAction(MainWindow)
        self.actionFermeture.setObjectName("actionFermeture")
        self.actionCroissance_de_r_gions = QtWidgets.QAction(MainWindow)
        self.actionCroissance_de_r_gions.setObjectName("actionCroissance_de_r_gions")
        self.actionPartition_de_regions = QtWidgets.QAction(MainWindow)
        self.actionPartition_de_regions.setObjectName("actionPartition_de_regions")
        self.actionM_thode_des_k_means = QtWidgets.QAction(MainWindow)
        self.actionM_thode_des_k_means.setObjectName("actionM_thode_des_k_means")
        self.zoomx2 = QtWidgets.QAction(MainWindow)
        self.zoomx2.setObjectName("zoomx2")
        self.zoomx4 = QtWidgets.QAction(MainWindow)
        self.zoomx4.setObjectName("zoomx4")
        self.actionNegatif = QtWidgets.QAction(MainWindow)
        self.actionNegatif.setObjectName("actionNegatif")
        self.redimentx2 = QtWidgets.QAction(MainWindow)
        self.redimentx2.setObjectName("redimentx2")
        self.redimentx4 = QtWidgets.QAction(MainWindow)
        self.redimentx4.setObjectName("redimentx4")
        self.action90 = QtWidgets.QAction(MainWindow)
        self.action90.setObjectName("action90")
        self.action180 = QtWidgets.QAction(MainWindow)
        self.action180.setObjectName("action180")
        self.moyenneur3x3 = QtWidgets.QAction(MainWindow)
        self.moyenneur3x3.setObjectName("moyenneur3x3")
        self.moyenneur5x5 = QtWidgets.QAction(MainWindow)
        self.moyenneur5x5.setObjectName("moyenneur5x5")
        self.median3x3 = QtWidgets.QAction(MainWindow)
        self.median3x3.setObjectName("median3x3")
        self.median5x5 = QtWidgets.QAction(MainWindow)
        self.median5x5.setObjectName("median5x5")
        self.gausien3x3 = QtWidgets.QAction(MainWindow)
        self.gausien3x3.setObjectName("gausien3x3")
        self.gausien5x5 = QtWidgets.QAction(MainWindow)
        self.gausien5x5.setObjectName("gausien5x5")
        self.actionhistogramme = QtWidgets.QAction(MainWindow)
        self.actionhistogramme.setObjectName("actionhistogramme")
        self.actionEgalization = QtWidgets.QAction(MainWindow)
        self.actionEgalization.setObjectName("actionEgalization")
        self.actionEtirement = QtWidgets.QAction(MainWindow)
        self.actionEtirement.setObjectName("actionEtirement")
        self.actionbinarisation_local = QtWidgets.QAction(MainWindow)
        self.actionbinarisation_local.setObjectName("actionbinarisation_local")
        self.actionbinarisation_global = QtWidgets.QAction(MainWindow)
        self.actionbinarisation_global.setObjectName("actionbinarisation_global")
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionEnregistrer)
        self.menuZoom.addAction(self.zoomx2)
        self.menuZoom.addAction(self.zoomx4)
        self.menuRedimentionnenemt.addAction(self.redimentx2)
        self.menuRedimentionnenemt.addAction(self.redimentx4)
        self.menuRotation.addAction(self.action90)
        self.menuRotation.addAction(self.action180)
        self.menuOperation.addAction(self.menuRotation.menuAction())
        self.menuOperation.addAction(self.menuZoom.menuAction())
        self.menuOperation.addAction(self.actionNegatif)
        self.menuOperation.addAction(self.menuRedimentionnenemt.menuAction())
        self.menuOperation.addSeparator()
        self.menuOperation.addAction(self.actionhistogramme)
        self.menuOperation.addAction(self.actionEgalization)
        self.menuOperation.addAction(self.actionEtirement)
        self.menuOperation.addSeparator()
        self.menuOperation.addAction(self.actionbinarisation_local)
        self.menuOperation.addAction(self.actionbinarisation_global)
        self.menuMoyanneur.addAction(self.moyenneur3x3)
        self.menuMoyanneur.addAction(self.moyenneur5x5)
        self.menuMedian.addAction(self.median3x3)
        self.menuMedian.addAction(self.median5x5)
        self.menuGaussien.addAction(self.gausien3x3)
        self.menuGaussien.addAction(self.gausien5x5)
        self.menuFiltrage.addAction(self.menuGaussien.menuAction())
        self.menuFiltrage.addAction(self.menuMoyanneur.menuAction())
        self.menuFiltrage.addAction(self.menuMedian.menuAction())
        self.menuExtraction_contour.addAction(self.actionGradiant)
        self.menuExtraction_contour.addAction(self.actionSobel)
        self.menuExtraction_contour.addAction(self.actionRobert)
        self.menuExtraction_contour.addAction(self.actionLaplacien)
        self.menuMorph_Math.addAction(self.actionErosion)
        self.menuMorph_Math.addAction(self.actionDilatation)
        self.menuMorph_Math.addAction(self.actionOuverture)
        self.menuMorph_Math.addAction(self.actionFermeture)
        self.menuSegmentation.addAction(self.actionCroissance_de_r_gions)
        self.menuSegmentation.addAction(self.actionPartition_de_regions)
        self.menuSegmentation.addAction(self.actionM_thode_des_k_means)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuOperation.menuAction())
        self.menubar.addAction(self.menuFiltrage.menuAction())
        self.menubar.addAction(self.menuExtraction_contour.menuAction())
        self.menubar.addAction(self.menuMorph_Math.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "L\'image originale"))
        self.label_2.setText(_translate("MainWindow", "L\'image resultat"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuOperation.setTitle(_translate("MainWindow", "Operation"))
        self.menuZoom.setTitle(_translate("MainWindow", "Zoom"))
        self.menuRedimentionnenemt.setTitle(_translate("MainWindow", "Redimentionnenemt"))
        self.menuRotation.setTitle(_translate("MainWindow", "Rotation"))
        self.menuFiltrage.setTitle(_translate("MainWindow", "Filtrage"))
        self.menuMoyanneur.setTitle(_translate("MainWindow", "Moyanneur"))
        self.menuMedian.setTitle(_translate("MainWindow", "Median"))
        self.menuGaussien.setTitle(_translate("MainWindow", "Gaussien"))
        self.menuExtraction_contour.setTitle(_translate("MainWindow", "Extraction contour"))
        self.menuMorph_Math.setTitle(_translate("MainWindow", "Morph Math"))
        self.menuSegmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.actionOuvrir.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionEnregistrer.setText(_translate("MainWindow", "Enregistrer"))
        self.actionEnregistrer.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionGradiant.setText(_translate("MainWindow", "Gradient"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionRobert.setText(_translate("MainWindow", "Robert"))
        self.actionLaplacien.setText(_translate("MainWindow", "Laplacien"))
        self.actionErosion.setText(_translate("MainWindow", "Erosion"))
        self.actionDilatation.setText(_translate("MainWindow", "Dilatation"))
        self.actionOuverture.setText(_translate("MainWindow", "Ouverture"))
        self.actionFermeture.setText(_translate("MainWindow", "Fermeture"))
        self.actionCroissance_de_r_gions.setText(_translate("MainWindow", "Croissance de régions"))
        self.actionPartition_de_regions.setText(_translate("MainWindow", "Partition de regions"))
        self.actionM_thode_des_k_means.setText(_translate("MainWindow", "Méthode des k-means"))
        self.zoomx2.setText(_translate("MainWindow", "x2"))
        self.zoomx4.setText(_translate("MainWindow", "x4"))
        self.actionNegatif.setText(_translate("MainWindow", "Negatif"))
        self.redimentx2.setText(_translate("MainWindow", "x2"))
        self.redimentx4.setText(_translate("MainWindow", "x3"))
        self.action90.setText(_translate("MainWindow", "90°"))
        self.action180.setText(_translate("MainWindow", "180°"))
        self.moyenneur3x3.setText(_translate("MainWindow", "3x3"))
        self.moyenneur5x5.setText(_translate("MainWindow", "5x5"))
        self.median3x3.setText(_translate("MainWindow", "3x3"))
        self.median5x5.setText(_translate("MainWindow", "5x5"))
        self.gausien3x3.setText(_translate("MainWindow", "s = 0.1"))
        self.gausien5x5.setText(_translate("MainWindow", "s = 0.8"))
        self.actionhistogramme.setText(_translate("MainWindow", "histogramme"))
        self.actionEgalization.setText(_translate("MainWindow", "Egalization"))
        self.actionEtirement.setText(_translate("MainWindow", "Etirement"))
        self.actionbinarisation_local.setText(_translate("MainWindow", "binarisation local"))
        self.actionbinarisation_global.setText(_translate("MainWindow", "binarisation global"))
        self.actionOuvrir.triggered.connect(self.openFile)
        self.action90.triggered.connect(self.rotate90)
        self.action180.triggered.connect(self.rotate180)
        self.actionNegatif.triggered.connect(self.negatif)
        self.moyenneur3x3.triggered.connect(self.Moyenneur5)
        self.moyenneur5x5.triggered.connect(self.Moyenneur7)
        self.gausien3x3.triggered.connect(self.gaussian5)
        self.gausien5x5.triggered.connect(self.gaussian7)
        self.median3x3.triggered.connect(self.median3)
        self.median5x5.triggered.connect(self.median5)
        self.actionGradiant.triggered.connect(self.grad)
        self.actionRobert.triggered.connect(self.Robert)
        self.actionSobel.triggered.connect(self.Sobel)
        self.actionLaplacien.triggered.connect(self.laplacien)
        self.actionErosion.triggered.connect(self.Erosion)
        self.actionDilatation.triggered.connect(self.dilatation)
        self.actionOuverture.triggered.connect(self.ouverture)
        self.actionFermeture.triggered.connect(self.fermeture)
        self.actionbinarisation_global.triggered.connect(self.BinarisationOtsu)
        self.actionbinarisation_local.triggered.connect(self.BinarisationLocal)
        self.actionM_thode_des_k_means.triggered.connect(self.kmeans)
        self.actionPartition_de_regions.triggered.connect(self.partRegion)

    def openFile(self):
        nom_fichier = QFileDialog.getOpenFileName()
        self.path = nom_fichier[0]
        pathx = self.path
        pixmap = QtGui.QPixmap(pathx)
        pixmap4 = pixmap.scaled(481, 461)

        self.ImageOrigine.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageOrigine.adjustSize()

    def rotate90(self):
        image = cv2.imread(self.path)
        o = Operation(image)
        img = o.rotate_image(90)
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : rotation 90")
        self.label_2.adjustSize()

    def rotate180(self):
        imag = cv2.imread(self.path)
        o = Operation(imag)
        img = o.rotate_image(180)
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : rotation 180")
        self.label_2.adjustSize()

    def negatif(self):
        image = cv2.imread(self.path)
        img = 255 - image
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : negative")
        self.label_2.adjustSize()

    def Moyenneur5(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Moyenneur(5)
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : f.moyenneur 5x5")
        self.label_2.adjustSize()

    def Moyenneur7(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Moyenneur(7)
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : f.moyenneur 7x7")
        self.label_2.adjustSize()

    def gaussian5(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Gaussien(0.1)
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : f.Gaussien 5x5")
        self.label_2.adjustSize()

    def gaussian7(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Gaussien(0.8)
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : f.Gaussien 7x7")
        self.label_2.adjustSize()

    def median3(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            f = Filtrage(image)
            img = f.Median(5)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            f = Filtrage(image)
            img = f.Median(5)
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : f.Median 3x3")
        self.label_2.adjustSize()

    def median5(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            f = Filtrage(image)
            img = f.Median(5)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            f = Filtrage(image)
            img = f.Median(5)
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : f.Median 5x5")
        self.label_2.adjustSize()
    def grad(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.grad(20)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.grad(20)
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)

        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : grad")
        self.label_2.adjustSize()

    def Robert(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Robert(20)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.Robert(20)
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)

        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : Robert")
        self.label_2.adjustSize()

    def Sobel(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Sobel(50)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.Sobel(50)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)

        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : Sobel")
        self.label_2.adjustSize()

    def laplacien(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Laplacien(20)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.Laplacien(20)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : laplacien")
        self.label_2.adjustSize()

    def Erosion(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.Erosion(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.Erosion(h)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_2.setText("L\'image resultat : Erosion")
        self.label_2.adjustSize()

    def dilatation(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.dilatation(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.dilatation(h)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_2.setText("L\'image resultat : Dilatation")
        self.label_2.adjustSize()

    def ouverture(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.Erosion(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.dilatation(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.Erosion(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.dilatation(h)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_2.setText("L\'image resultat : Ouverture")
        self.label_2.adjustSize()

    def fermeture(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.dilatation(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.Erosion(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.dilatation(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.Erosion(h)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_2.setText("L\'image resultat : Ouverture")
        self.label_2.adjustSize()
    def BinarisationOtsu(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            b = Binarisation(image)
            print('hello')
            img = b.Otsu()
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            b = Binarisation(image)
            img = b.Otsu()
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat :Otsu")
        self.label_2.adjustSize()
    def BinarisationLocal(self):
        image = cv2.imread(self.path)
        imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        f = Binarisation(imag)
        img =f.Seuillage(128)
        imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat :local")
        self.label_2.adjustSize()
    def kmeans(self):
        image = cv2.imread(self.path)
        imag = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, byteValue = imag.shape
        s = Segmentation(imag)
        img = s.k_means()
        imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : k_means")
        self.label_2.adjustSize()
    def partRegion(self):
        image = cv2.imread(self.path)
        imag = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, byteValue = imag.shape
        s = Segmentation(imag)
        img = s.partition_regions()
        imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("L\'image resultat : partition region")
        self.label_2.adjustSize()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
