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
from PyQt5.QtCore import pyqtSlot
Widgets = [' QHBoxLayout', 'QGroupBox', 'QDialog', 'QVBoxLayout','QSizePolicy',
    'QPushButton','QWidget','QMessageBox','QApplication','QMainWindow','QAction','qApp','QToolTip','QGridLayout']

for libs in Widgets:
    try:
        exec ("from PyQt5.QtWidgets import {module}".format(module=libs))
    except Exception as e:
        print (e)

Gui = ['QIcon' ,'QFont']

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
        self.width = 200        
        self.height = 300
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
        # layout.setColumnStretch(1, 5)
        # layout.setColumnStretch(1, 5)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        netflixButton = QPushButton(QIcon(':/myicons/netflix.png'),'',self)
        netflixButton.setToolTip('<b>NetFlix</b>')
        # netflixButton.resize(netflixButton.sizeHint())
        netflixButton.clicked.connect(self.netflixPressed)    
        netflixButton.setSizePolicy(sizePolicy)
        layout.addWidget(netflixButton,1,0)

        huluButton = QPushButton(QIcon(':/myicons/hulu.png'),'',self)
        huluButton.setToolTip('<b>Hulu</b>')
        huluButton.clicked.connect(self.huluPressed)    
        huluButton.setSizePolicy(sizePolicy)
        layout.addWidget(huluButton,2,0)     


        self.horizontalGroupBox.setLayout(layout)
        
    ''' 
    layout = [N , H , Y]
    '''

    def huluPressed(self):
        sender = self.sender()
        webbrowser.open_new_tab('http://hulu.com/')
        
        
    
    def netflixPressed(self):
        sender = self.sender()
        webbrowser.open_new_tab('http://netlflix.com/')
        
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
