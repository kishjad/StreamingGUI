#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Kshitej Jadhav 
Last edited: Sept 2017
"""

import sys
import resources
#from selenium import webdriver
import webbrowser
from PyQt5.QtCore import pyqtSlot, QSize
Widgets = [' QHBoxLayout', 'QGroupBox', 'QDialog', 'QVBoxLayout','QSizePolicy',
    'QPushButton','QWidget','QMessageBox','QApplication','QMainWindow','QAction','qApp','QToolTip','QGridLayout']

for libs in Widgets:
    try:
        exec ("from PyQt5.QtWidgets import {module}".format(module=libs))
    except Exception as e:
        print (e)

Gui = ['QIcon' ,'QFont', 'QPixmap']

for libs in Gui:
    try:
        exec ("from PyQt5.QtGui import {module}".format(module=libs))
    except Exception as e:
        print (e)


class Streamer(QDialog):
    
    def __init__(self):
        super().__init__()
        self.left = 40
        self.top = 50
        self.width = 400        
        self.height = 400
        self.title = 'Streamer v1.0'
        self.initUI()
        
        
    def initUI(self):           
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createGridLayout()
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        
        self.show()
    
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Available Services")
        layout = QGridLayout()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        netflixButton = QPushButton('')
        netflixPix = QPixmap(':/myicons/netflix.png')
        netflixIcon = QIcon(netflixPix)
        netflixButton.setIcon(netflixIcon)
        netflixButton.setIconSize(netflixPix.rect().size())
        netflixButton.setToolTip('<b>NetFlix</b>')
        netflixButton.clicked.connect(self.netflixPressed)    
        netflixButton.setSizePolicy(sizePolicy)
        layout.addWidget(netflixButton,1,0)

        huluButton = QPushButton('')
        huluPix = QPixmap(':/myicons/hulu.png')
        huluIcon = QIcon(huluPix)
        huluButton.setIcon(huluIcon)
        huluButton.setIconSize(huluPix.rect().size())
        huluButton.setToolTip('<b>Hulu</b>')
        huluButton.clicked.connect(self.huluPressed)    
        huluButton.setSizePolicy(sizePolicy)
        layout.addWidget(huluButton,2,0)     

        youtubeButton = QPushButton('')
        youtubePix = QPixmap(':/myicons/youtube.png')
        youtubeIcon = QIcon(youtubePix)
        youtubeButton.setIcon(youtubeIcon)
        youtubeButton.setIconSize(youtubePix.rect().size())
        youtubeButton.setToolTip('<b>Youtube</b>')
        youtubeButton.clicked.connect(self.youtubePressed)    
        youtubeButton.setSizePolicy(sizePolicy)
        layout.addWidget(youtubeButton,1,1)     

        primeButton = QPushButton('')
        primePix = QPixmap(':/myicons/prime.png')
        primeIcon = QIcon(primePix)
        primeButton.setIcon(primeIcon)
        primeButton.setIconSize(primePix.rect().size())
        primeButton.setToolTip('<b>Prime</b>')
        primeButton.clicked.connect(self.primePressed)    
        primeButton.setSizePolicy(sizePolicy)
        layout.addWidget(primeButton,2,1)     

        self.horizontalGroupBox.setLayout(layout)
        

    def huluPressed(self):
        sender = self.sender()
        webbrowser.open_new_tab('https://www.hulu.com/')
        

    def netflixPressed(self):
        sender = self.sender()
        webbrowser.open_new_tab('https://www.netlflix.com/')

    def primePressed(self):
        sender = self.sender()
        webbrowser.open_new_tab('https://www.primevideo.com')

    def youtubePressed(self):
        sender = self.sender()
        webbrowser.open_new_tab('https://www.youtube.com/')    

    # def closeEvent(self, event):
        
    #     reply = QMessageBox.question(self, 'Message',
    #         "Are you sure to quit?", QMessageBox.Yes | 
    #         QMessageBox.No, QMessageBox.No)

    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Streamer()
    sys.exit(app.exec_())
