#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import resources

Widgets = ['QPushButton', 
                'QWidget', 
                'QMessageBox', 
                'QApplication',
                'QMainWindow',
                'QAction','qApp',
                'QToolTip']

for libs in Widgets:
    try:
        exec ("from PyQt5.QtWidgets import {module}".format(module=libs))
    except Exception as e:
        print (e)

Gui = ['QIcon' ]

for libs in Gui:
    try:
        exec ("from PyQt5.QtGui import {module}".format(module=libs))
    except Exception as e:
        print (e)