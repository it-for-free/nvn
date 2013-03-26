# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit

import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui
# следующее  - импортируется для работы со слотами
from PyQt4.QtCore import QObject, pyqtSlot
from PyQt4 import QtCore, QtGui

"""
класс который мы опишем ниже
будет отвечать а внешний вид
нашего первобытного браузера
"""
class ForumWindowUi(object):

#в контсрукторе получаем класс типа ForumWindow """
    def setAccessibleName(self,name):
        return

    def setupUi(self, ForumWindow):
       #self.setWindowTitle('Модуль форума')
        ok = QtGui.QPushButton("OK")
        cancel = QtGui.QPushButton("Cancel")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok)
        hbox.addWidget(cancel)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        ForumWindow.setLayout(vbox)

        ForumWindow.resize(300, 150)


        ForumWindow.show()
