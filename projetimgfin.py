# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projetimg1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit
from PyQt5.QtGui import QPixmap
import cv2
from cv2 import *
from matplotlib.pyplot import *
import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
from matplotlib import pyplot as plt
from filtrage import *
from contour import *
from Morphologie import *
import math

class Ui_MainWindow(object):
    path = 'hello';

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 781)
        MainWindow.setStyleSheet("background-color: rgb(148, 42, 21 );")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 0, 481, 61))
        self.label.setStyleSheet("\n"
"font: 75 15pt \"Fixedsys\";\n"
"font: 81 20pt \"Rockwell Extra Bold\";\n"
"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label.setObjectName("label")
        self.ouvrir_image = QtWidgets.QPushButton(self.centralwidget)
        self.ouvrir_image.setGeometry(QtCore.QRect(490, 80, 101, 21))
        self.ouvrir_image.setStyleSheet("background-color: rgb(209, 111, 91);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.ouvrir_image.setObjectName("ouvrir_image")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(530, 130, 20, 401))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 130, 121, 31))
        self.label_2.setStyleSheet("font: 8pt \"Oswald\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 130, 71, 31))
        self.label_3.setStyleSheet("font: 8pt \"Oswald\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 560, 81, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Sans Serif\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 610, 131, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Sans Serif\";")
        self.label_5.setObjectName("label_5")
        self.image_negative = QtWidgets.QPushButton(self.centralwidget)
        self.image_negative.setGeometry(QtCore.QRect(20, 520, 101, 21))
        self.image_negative.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.image_negative.setObjectName("image_negative")
        self.rotationtxt = QtWidgets.QTextEdit(self.centralwidget)
        self.rotationtxt.setGeometry(QtCore.QRect(190, 560, 104, 31))
        self.rotationtxt.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"background-color: rgb(255, 255, 255);")
        self.rotationtxt.setObjectName("rotationtxt")
        self.tailleprtxt = QtWidgets.QTextEdit(self.centralwidget)
        self.tailleprtxt.setGeometry(QtCore.QRect(190, 610, 104, 31))
        self.tailleprtxt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tailleprtxt.setObjectName("tailleprtxt")
        self.image_rotation = QtWidgets.QPushButton(self.centralwidget)
        self.image_rotation.setGeometry(QtCore.QRect(310, 560, 151, 31))
        self.image_rotation.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.image_rotation.setObjectName("image_rotation")
        self.image_redimenssionerpr = QtWidgets.QPushButton(self.centralwidget)
        self.image_redimenssionerpr.setGeometry(QtCore.QRect(310, 610, 151, 31))
        self.image_redimenssionerpr.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.image_redimenssionerpr.setObjectName("image_redimenssionerpr")
        self.afficher_image = QtWidgets.QLabel(self.centralwidget)
        self.afficher_image.setGeometry(QtCore.QRect(110, 200, 311, 241))
        self.afficher_image.setText("")
        self.afficher_image.setObjectName("afficher_image")
        self.resultat_image = QtWidgets.QLabel(self.centralwidget)
        self.resultat_image.setGeometry(QtCore.QRect(640, 200, 311, 241))
        self.resultat_image.setText("")
        self.resultat_image.setObjectName("resultat_image")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 670, 81, 31))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Sans Serif\";")
        self.label_6.setObjectName("label_6")
        self.largeur = QtWidgets.QTextEdit(self.centralwidget)
        self.largeur.setGeometry(QtCore.QRect(190, 670, 41, 31))
        self.largeur.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.largeur.setObjectName("largeur")
        self.image_redimenssionerhl = QtWidgets.QPushButton(self.centralwidget)
        self.image_redimenssionerhl.setGeometry(QtCore.QRect(310, 670, 151, 31))
        self.image_redimenssionerhl.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.image_redimenssionerhl.setObjectName("image_redimenssionerhl")
        self.hauteur = QtWidgets.QTextEdit(self.centralwidget)
        self.hauteur.setGeometry(QtCore.QRect(250, 670, 41, 31))
        self.hauteur.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hauteur.setObjectName("hauteur")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(670, 570, 111, 31))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Sans Serif\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(670, 620, 101, 31))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Sans Serif\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(670, 670, 91, 31))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Sans Serif\";")
        self.label_9.setObjectName("label_9")
        self.gaussetxt = QtWidgets.QTextEdit(self.centralwidget)
        self.gaussetxt.setGeometry(QtCore.QRect(800, 570, 104, 31))
        self.gaussetxt.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"background-color: rgb(255, 255, 255);")
        self.gaussetxt.setObjectName("gaussetxt")
        self.mediantxt = QtWidgets.QTextEdit(self.centralwidget)
        self.mediantxt.setGeometry(QtCore.QRect(800, 620, 104, 31))
        self.mediantxt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mediantxt.setObjectName("mediantxt")
        self.moyentxt = QtWidgets.QTextEdit(self.centralwidget)
        self.moyentxt.setGeometry(QtCore.QRect(800, 670, 104, 31))
        self.moyentxt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.moyentxt.setObjectName("moyentxt")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(650, 550, 371, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(640, 560, 20, 161))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1010, 560, 20, 161))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(650, 710, 371, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.actiongausse = QtWidgets.QPushButton(self.centralwidget)
        self.actiongausse.setGeometry(QtCore.QRect(930, 570, 71, 31))
        self.actiongausse.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.actiongausse.setObjectName("actiongausse")
        self.actionmedian = QtWidgets.QPushButton(self.centralwidget)
        self.actionmedian.setGeometry(QtCore.QRect(930, 620, 71, 31))
        self.actionmedian.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.actionmedian.setObjectName("actionmedian")
        self.actionmoyen = QtWidgets.QPushButton(self.centralwidget)
        self.actionmoyen.setGeometry(QtCore.QRect(930, 670, 71, 31))
        self.actionmoyen.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.actionmoyen.setObjectName("actionmoyen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1063, 21))
        self.menubar.setStyleSheet("background-color: rgb(209, 127, 91);")
        self.menubar.setObjectName("menubar")
        self.menuFonctions = QtWidgets.QMenu(self.menubar)
        self.menuFonctions.setObjectName("menuFonctions")
        self.menuBinarisation = QtWidgets.QMenu(self.menuFonctions)
        self.menuBinarisation.setObjectName("menuBinarisation")
        self.menuFiltrage = QtWidgets.QMenu(self.menuFonctions)
        self.menuFiltrage.setObjectName("menuFiltrage")
        self.menuContour = QtWidgets.QMenu(self.menuFonctions)
        self.menuContour.setObjectName("menuContour")
        self.erosion = QtWidgets.QMenu(self.menuFonctions)
        self.erosion.setObjectName("erosion")
        self.menuSegmentation = QtWidgets.QMenu(self.menuFonctions)
        self.menuSegmentation.setObjectName("menuSegmentation")
        self.menuHistograme = QtWidgets.QMenu(self.menuFonctions)
        self.menuHistograme.setObjectName("menuHistograme")
        self.menuEgalisation = QtWidgets.QMenu(self.menuFonctions)
        self.menuEgalisation.setObjectName("menuEgalisation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.binarisationotsu = QtWidgets.QAction(MainWindow)
        self.binarisationotsu.setObjectName("binarisationotsu")
        self.binarisationotsu.triggered.connect(self.otsu)
        self.binarisationseuillage = QtWidgets.QAction(MainWindow)
        self.binarisationseuillage.setObjectName("binarisationseuillage")
        self.filtragegaussien = QtWidgets.QAction(MainWindow)
        self.filtragegaussien.setObjectName("filtragegaussien")
        self.filtragemoyenneure = QtWidgets.QAction(MainWindow)
        self.filtragemoyenneure.setObjectName("filtragemoyenneure")
        self.filtragemedian = QtWidgets.QAction(MainWindow)
        self.filtragemedian.setObjectName("filtragemedian")
        self.contourgradient = QtWidgets.QAction(MainWindow)
        self.contourgradient.setObjectName("contourgradient")
        self.contoursobel = QtWidgets.QAction(MainWindow)
        self.contoursobel.setObjectName("contoursobel")
        self.contourlaplacien = QtWidgets.QAction(MainWindow)
        self.contourlaplacien.setObjectName("contourlaplacien")
        self.contourrobert = QtWidgets.QAction(MainWindow)
        self.contourrobert.setObjectName("contourrobert")
        self.actionErosion = QtWidgets.QAction(MainWindow)
        self.actionErosion.setObjectName("actionErosion")
        self.actionErosion.triggered.connect(self.erosionn)

        self.dilataion = QtWidgets.QAction(MainWindow)
        self.dilataion.setObjectName("dilataion")
        self.ouverture = QtWidgets.QAction(MainWindow)
        self.ouverture.setObjectName("ouverture")
        self.fermeture = QtWidgets.QAction(MainWindow)
        self.fermeture.setObjectName("fermeture")
        self.fermeture.triggered.connect(self.fermeturre)
        self.croissance = QtWidgets.QAction(MainWindow)
        self.croissance.setObjectName("croissance")
        self.partition = QtWidgets.QAction(MainWindow)
        self.partition.setObjectName("partition")
        self.kmeans = QtWidgets.QAction(MainWindow)
        self.kmeans.setObjectName("kmeans")
        self.histogramecoleur = QtWidgets.QAction(MainWindow)
        self.histogramecoleur.setObjectName("histogramecoleur")
        self.histogramegray = QtWidgets.QAction(MainWindow)
        self.histogramegray.setObjectName("histogramegray")
        self.egalisationcoleur = QtWidgets.QAction(MainWindow)
        self.egalisationcoleur.setObjectName("egalisationcoleur")
        self.egalisationgray = QtWidgets.QAction(MainWindow)
        self.egalisationgray.setObjectName("egalisationgray")
        self.menuBinarisation.addAction(self.binarisationotsu)
        self.menuBinarisation.addAction(self.binarisationseuillage)
        self.menuFiltrage.addAction(self.filtragegaussien)
        self.menuFiltrage.addAction(self.filtragemoyenneure)
        self.menuFiltrage.addAction(self.filtragemedian)
        self.menuContour.addAction(self.contourgradient)
        self.menuContour.addAction(self.contoursobel)
        self.menuContour.addAction(self.contourlaplacien)
        self.menuContour.addAction(self.contourrobert)
        self.erosion.addAction(self.actionErosion)
        self.erosion.addAction(self.dilataion)
        self.erosion.addAction(self.ouverture)
        self.erosion.addAction(self.fermeture)
        self.menuSegmentation.addAction(self.croissance)
        self.menuSegmentation.addAction(self.partition)
        self.menuSegmentation.addAction(self.kmeans)
        self.menuHistograme.addAction(self.histogramecoleur)
        self.menuHistograme.addAction(self.histogramegray)
        self.menuEgalisation.addAction(self.egalisationcoleur)
        self.menuEgalisation.addAction(self.egalisationgray)
        self.menuFonctions.addAction(self.menuBinarisation.menuAction())
        self.menuFonctions.addAction(self.menuHistograme.menuAction())
        self.menuFonctions.addAction(self.menuFiltrage.menuAction())
        self.menuFonctions.addAction(self.menuEgalisation.menuAction())
        self.menuFonctions.addAction(self.menuContour.menuAction())
        self.menuFonctions.addAction(self.erosion.menuAction())
        self.menuFonctions.addAction(self.menuSegmentation.menuAction())
        self.menubar.addAction(self.menuFonctions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Traitement Image"))
        self.ouvrir_image.setText(_translate("MainWindow", "Votre image"))
        self.label_2.setText(_translate("MainWindow", "l\'image:"))
        self.label_3.setText(_translate("MainWindow", "Résultat:"))
        self.label_4.setText(_translate("MainWindow", "Saisir angle :"))
        self.label_5.setText(_translate("MainWindow", "Saisir pourcentage :"))
        self.image_negative.setText(_translate("MainWindow", "Image negative"))
        self.image_rotation.setText(_translate("MainWindow", "Rotation"))
        self.image_rotation.clicked.connect(self.show_rotation)
        self.image_redimenssionerpr.setText(_translate("MainWindow", "Redimenssioner %"))
        self.label_6.setText(_translate("MainWindow", "Saisir Taille :"))
        self.image_redimenssionerhl.setText(_translate("MainWindow", "Redimenssioner H*L"))
        self.label_7.setText(_translate("MainWindow", "valeur de l\'écart :"))
        self.label_8.setText(_translate("MainWindow", "Taille du filtre :"))
        self.label_9.setText(_translate("MainWindow", "Taille du filtre :"))
        self.actiongausse.setText(_translate("MainWindow", "Gausse"))
        self.actiongausse.clicked.connect(self.gaussian)
        self.actionmedian.setText(_translate("MainWindow", "Median"))
        self.actionmedian.clicked.connect(self.median)
        self.actionmoyen.setText(_translate("MainWindow", "Moyenneure"))
        self.actionmoyen.clicked.connect(self.Moyenneur)
        self.menuFonctions.setTitle(_translate("MainWindow", "Fonctions"))
        self.menuBinarisation.setTitle(_translate("MainWindow", "Binarisation"))
        self.menuFiltrage.setTitle(_translate("MainWindow", "Filtrage"))
        self.menuContour.setTitle(_translate("MainWindow", "Contour"))
        self.erosion.setTitle(_translate("MainWindow", "Morphologie mathematique"))

        self.menuSegmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.menuHistograme.setTitle(_translate("MainWindow", "Histograme"))
        self.menuEgalisation.setTitle(_translate("MainWindow", "Egalisation"))
        self.binarisationotsu.setText(_translate("MainWindow", "Otsu"))
        self.binarisationseuillage.setText(_translate("MainWindow", "seuillage "))
        self.filtragegaussien.setText(_translate("MainWindow", "Gaussien"))
        self.filtragemoyenneure.setText(_translate("MainWindow", "Moyenneure"))
        self.filtragemedian.setText(_translate("MainWindow", "Médian"))
        self.contourgradient.setText(_translate("MainWindow", "Gradient"))
        self.contourgradient.triggered.connect(self.grad)

        self.contoursobel.setText(_translate("MainWindow", "Sobel"))
        self.contoursobel.triggered.connect(self.Sobel)

        self.contourlaplacien.setText(_translate("MainWindow", "Laplacien"))
        self.contourlaplacien.triggered.connect(self.laplacien)

        self.contourrobert.setText(_translate("MainWindow", "Robert"))
        self.contourrobert.triggered.connect(self.Robert)
        self.actionErosion.setText(_translate("MainWindow", "Erosion"))
        self.dilataion.setText(_translate("MainWindow", "dilatation"))
        self.dilataion.triggered.connect(self.dilatation)
        self.ouverture.setText(_translate("MainWindow", "Ouverture"))
        self.ouverture.triggered.connect(self.ouvverture)
        self.fermeture.setText(_translate("MainWindow", "Fermeture"))
        self.croissance.setText(_translate("MainWindow", "Croissance de regions"))
        self.partition.setText(_translate("MainWindow", "Parition de regions"))
        self.kmeans.setText(_translate("MainWindow", "Methode des K-means"))
        self.histogramecoleur.setText(_translate("MainWindow", "Coleur"))
        self.histogramegray.setText(_translate("MainWindow", "Gray"))
        self.egalisationcoleur.setText(_translate("MainWindow", "coleur"))
        self.egalisationcoleur.triggered.connect(self.histeq)
        self.egalisationgray.setText(_translate("MainWindow", "gray"))
        self.egalisationgray.triggered.connect(self.histeq)
        self.histogramecoleur.triggered.connect(self.hist)
        self.histogramegray.triggered.connect(self.histgray)
        self.binarisationseuillage.triggered.connect(self.binarise)
        self.image_redimenssionerhl.clicked.connect(self.show_redimtaille)
        self.image_redimenssionerpr.clicked.connect(self.show_redimpurcentage)
        self.image_negative.clicked.connect(self.show_negative)
        self.ouvrir_image.clicked.connect(self.getimage)
    def getimage(self):
        filename = QFileDialog.getOpenFileName()
        Ui_MainWindow.path = filename[0]
        pixmap = QtGui.QPixmap(Ui_MainWindow.path)
        print(Ui_MainWindow.path)
        pixmap4 = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.afficher_image.setPixmap(pixmap4)
    def show_negative(self):
        image = cv2.imread(Ui_MainWindow.path)
        img = 255 - image
        # cv2.imshow("image negative", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        random = randint(1,2000)
        print(random)
        x="image"+str(random)
        cv2.imwrite("D://"+x+".png",img)
        pixmap = QtGui.QPixmap("D://"+x+".png")
        pixmap4 = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap4)
    def show_rotation(self):
        anglevalue = int(self.rotationtxt.toPlainText())
        print(anglevalue)
        image = cv2.imread(Ui_MainWindow.path)
        (h, w) = image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, anglevalue, 0.6)
        rotated = cv2.warpAffine(image, M, (h, w))
        # cv2.imshow("image rotation", rotated)
        # cv2.waitKey(0);
        # cv2.destroyAllWindows()  # destroys the window showing image
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        cv2.imwrite("D://" + x + ".png", rotated)
        pixmap = QtGui.QPixmap("D://" + x + ".png")
        pixmap4 = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap4)
    def show_redimpurcentage(self):
        pourcentage = int(self.tailleprtxt.toPlainText())
        print(pourcentage)
        image = cv2.imread(Ui_MainWindow.path)
        scale_percent = pourcentage
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        cv2.imwrite("D://" + x + ".png", resized)
        pixmap = QtGui.QPixmap("D://" + x + ".png")
        # pixmap4 = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap)
        # cv2.imshow("redimmensionner image", resized)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    def show_redimtaille(self):
        hauteur = int(self.hauteur.toPlainText())
        largeur = int(self.largeur.toPlainText())
        print(hauteur)
        print(largeur)
        image = cv2.imread(Ui_MainWindow.path)
        dim = (hauteur, largeur)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        cv2.imwrite("D://" + x + ".png", resized)
        pixmap = QtGui.QPixmap("D://" + x + ".png")
        # pixmap4 = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap)
        # cv2.imshow("redimmensionner image", resized)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    def binarise(self):

        image_init = cv2.imread(Ui_MainWindow.path)
        gray_image = cv2.cvtColor(image_init, cv2.COLOR_BGR2GRAY)
        # Choisir l'image d'origine
        largeur = int(gray_image.shape[0])
        print('largeur=', largeur)
        hauteur = int(gray_image.shape[1])
        print('hauteur = ', hauteur)  # Affiche la taille de l'image
        # ret,thresh1 = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)
        # cv2.imshow("fffffffff",thresh1)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        for i in range(1, largeur):
            for j in range(1, hauteur):
                if gray_image[i][j] <= 120:
                    gray_image[i][j] = 255
                else:
                    gray_image[i][j] = 0
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        cv2.imwrite("D://" + x + ".png", gray_image)
        pixmap = QtGui.QPixmap("D://" + x + ".png")
        pixmap4 = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap4)
    def otsu(self):
        image_init = cv2.imread(Ui_MainWindow.path)
        gray = cv2.cvtColor(image_init, cv2.COLOR_BGR2GRAY)
        pixel_number = gray.shape[0] * gray.shape[1]
        mean_weigth = 1.0 / pixel_number
        his, bins = np.histogram(gray, np.arange(0, 257))
        final_thresh = -1
        final_value = -1
        intensity_arr = np.arange(256)

        for t in bins[1:-1]:
            pcb = np.sum(his[:t])
            pcf = np.sum(his[t:])
            Wb = pcb * mean_weigth
            Wf = pcf * mean_weigth
            mub = np.sum(intensity_arr[:t] * his[:t]) / float(pcb)
            muf = np.sum(intensity_arr[t:] * his[t:]) / float(pcf)
            np.seterr(divide='ignore', invalid='ignore')
            value = Wb * Wf * (mub - muf) ** 2
            if value > final_value:
                final_thresh = t
                final_value = value

        final_img = gray.copy()
        final_img[gray > final_thresh] = 255
        final_img[gray < final_thresh] = 0
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://" + y + ".png", final_img)
        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
        pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap5)

    def histgray(self):
        image_init = cv2.imread(Ui_MainWindow.path)
        gray_image = cv2.cvtColor(image_init, cv2.COLOR_BGR2GRAY)
        Image = np.zeros(257)
        for i in range(1, gray_image.shape[0]):
            for j in range(1, gray_image.shape[1]):
                v = gray_image[i][j] + 1
                Image[v] = Image[v] + 1

        plt.plot(Image)
        plt.show()
    def hist(self):
        image_init = cv2.imread(Ui_MainWindow.path)
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([image_init], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])

        plt.show()
    def imhist(self,im):
        # calculates normalized histogram of an image
        m, n = im.shape
        h = [0.0] * 256
        for i in range(m):
            for j in range(n):
                h[im[i, j]] += 1
        return np.array(h) / (m * n)

    def cumsum(self,h):
        # finds cumulative sum of a numpy array, list
        return [sum(h[:i + 1]) for i in range(len(h))]

    def histeq(self):
        img=cv2.imread(Ui_MainWindow.path)
        im=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h = self.imhist(im)
        cdf = np.array(self.cumsum(h))  # cumulative distribution function
        sk = np.uint8(255 * cdf)  # finding transfer function values
        s1, s2 = im.shape
        Y = np.zeros_like(im)
        # applying transfered values for each pixels
        for i in range(0, s1):
            for j in range(0, s2):
                Y[i, j] = sk[im[i, j]]
        H = self.imhist(Y)
        # return transformed image, original and new istogram,
        # and transform function
        plt.plot(H)
        plt.show()
    def Moyenneur(self):
        taille = float(self.moyentxt.toPlainText())
        image = cv2.imread(Ui_MainWindow.path)
        f = Filtrage(image)
        img = f.Moyenneur(taille)
        height, width, byteValue = img.shape
        print(byteValue)
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://" + y + ".png", img)
        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
        pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap5)

    def gaussian(self):
        taille = float(self.gaussetxt.toPlainText())
        image = cv2.imread(Ui_MainWindow.path)
        f = Filtrage(image)
        img = f.Gaussien(taille)
        height, width, byteValue = img.shape
        print(byteValue)
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://" + y + ".png", img)
        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
        pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap5)

    def median(self):
        image = cv2.imread(Ui_MainWindow.path)
        taille = float(self.mediantxt.toPlainText())
        height, width, byteValue = image.shape
        if byteValue == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            f = Filtrage(image)
            img = f.Median(taille)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            f = Filtrage(image)
            img = f.Median(taille)
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://" + y + ".png", img)
        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
        pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap5)
    def grad(self):
        image = cv2.imread(Ui_MainWindow.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.grad(20)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            c = Contours(image)
            img = c.grad(20)
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://" + y + ".png", img)
        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
        pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap5)

    def Robert(self):
        image = cv2.imread(Ui_MainWindow.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Robert(20)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            c = Contours(image)
            img = c.Robert(20)
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://" + y + ".png", img)
        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
        pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap5)

    def Sobel(self):
        image = cv2.imread(Ui_MainWindow.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Sobel(50)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            c = Contours(image)
            img = c.Sobel(50)
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://" + y + ".png", img)
        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
        pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap5)
    def laplacien(self):
        image = cv2.imread(Ui_MainWindow.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Laplacien(20)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            c = Contours(image)
            img = c.Laplacien(20)
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://" + y + ".png", img)
        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
        pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap5)
    def erosionn(self):
        image = cv2.imread(Ui_MainWindow.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.Erosion(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.Erosion(h)
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://" + y + ".png", img)
        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
        pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap5)
    def dilatation(self):
        image = cv2.imread(Ui_MainWindow.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.dilatation(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.dilatation(h)
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://" + y + ".png", img)
        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
        pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap5)

    def ouvverture(self):
        image = cv2.imread(Ui_MainWindow.path)
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
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.Erosion(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.dilatation(h)
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://" + y + ".png", img)
        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
        pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap5)

    def fermeturre(self):
        image = cv2.imread(Ui_MainWindow.path)
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
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.Erosion(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.dilatation(h)
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://" + y + ".png", img)
        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
        pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.resultat_image.setPixmap(pixmap5)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
