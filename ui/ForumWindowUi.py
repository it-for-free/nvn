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

         # описываем действие ("действие" - это понятие из QT -см. ссылки выше листинга)
##        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
##        exitAction.setShortcut('Ctrl+Q')
##        exitAction.setStatusTip('Выйти изприложения')
##        exitAction.triggered.connect(QtGui.qApp.quit)

        ForumWindow.verticalLayout = QtGui.QVBoxLayout(ForumWindow)
        ForumWindow.verticalLayout.setObjectName("verticalLayout")

        ForumWindow.horizontalLayout = QtGui.QHBoxLayout(ForumWindow)
        ForumWindow.horizontalLayout.setObjectName("horizontalLayout")

        ForumWindow.back = QtGui.QPushButton(ForumWindow)
        ForumWindow.horizontalLayout.addWidget(ForumWindow.back)
        ForumWindow.back.setToolTip("Вернуться на предыдущую страницу")
        ForumWindow.back.setText("Назад")
        ForumWindow.back.setLayoutDirection(QtCore.Qt.RightToLeft)

# описываем действие ("действие" - это понятие из QT -см. ссылки выше листинга)
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', ForumWindow)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выйти из приложения')

#действие открытия нового окна
        newWindowAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&ForumWindow', ForumWindow)
        newWindowAction.setShortcut('Ctrl+P')
        newWindowAction.setStatusTip('Открыть дополнительное окно')

#действие для диалога выбора директории
        FolderChooser = QtGui.QAction(QtGui.QIcon('exit.png'), '&Choose Folder', ForumWindow)
        FolderChooser .setShortcut('Ctrl+D')
        FolderChooser .setStatusTip('Открыть диалог выбора диретории')


        # пример подключения слота к действию (сигналу)
        #
        exitAction.triggered.connect(QtGui.qApp.quit)
        newWindowAction.triggered.connect(ForumWindow.someFunc)
        FolderChooser.triggered.connect(ForumWindow.someFunc)
        ForumWindow.statusBar()

        #создаём статус бар для окна
        menubar =  ForumWindow.menuBar()

       # добавляем меню "Файл" на форму
        fileMenu = menubar.addMenu('&File')

      # подключаем действия как элементы полменю
        fileMenu.addAction(FolderChooser)
        fileMenu.addAction(newWindowAction)
        fileMenu.addAction(exitAction)

        ForumWindow.show()

    def someFunc(self, ForumWindow):
        return
