# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtCore, QtGui

from ui.httpWidget import Ui_HttpWidget
from ui.ForumWindowUi import ForumWindowUi

from PyQt4 import QtWebKit


# Описываем дополнительное окно
class ForumWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        super(ForumWindow, self).__init__(parent)
# запускаем метод рисующий виджеты окна
        self.ui = ForumWindowUi()
        self.ui.setupUi(self)