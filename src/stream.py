#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Author: Kshitej Jadhav 
Last edited: Sept 2017
"""


from imports import *   

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        netflixButton = QPushButton(QIcon(':/myicons/netflix.png'), 'Netflix', self)
        huluButton = QPushButton(QIcon(':/myicons/hulu.png'), 'Hulu', self)
        youtubeButton = QPushButton(QIcon(':/myicons/youtube.png'), 'Youtube', self)
        self.show()
    ''' 
    layout = []
    '''
        
        
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
    ex = Example()
    sys.exit(app.exec_())
