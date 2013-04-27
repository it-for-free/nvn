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

        ForumWindow.resize(600, 250)

         # описываем действие ("действие" - это понятие из QT -см. ссылки выше листинга)
##        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
##        exitAction.setShortcut('Ctrl+Q')
##        exitAction.setStatusTip('Выйти изприложения')
##        exitAction.triggered.connect(QtGui.qApp.quit)






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


# Приклеиваем к главному окну управляющие элементы
        ForumWindow.form_widget = FormWidget()
        ForumWindow.setCentralWidget(ForumWindow.form_widget)

        ForumWindow.show()

    def someFunc(self, ForumWindow):
        return


class FormWidget(QWidget):

    def __init__(self):
        super(FormWidget, self).__init__()

        ok = QtGui.QPushButton("OK")
        cancel = QtGui.QPushButton("Cancel")

        hbox = QtGui.QHBoxLayout()
        button1 = QPushButton("Сообщение 1")
        button2 = QPushButton("Сообщение 2")

        vbox = QtGui.QVBoxLayout() #  создаёем вертикальный слой
        vbox.addStretch(1)
        vbox.addWidget(button1) # добавляем первую кновку в вертикальном
# добавляем горизонтальный на вертикальный (а вместе с ним и все кнопки)
        vbox.addLayout(hbox)
        vbox.addWidget(button2) # добавляем на вертикальный слой  ещё кнопку


        hbox.addStretch(1)
        hbox.addWidget(ok)
        hbox.addWidget(cancel)

# Дальше потренируемся выводить переменное число кнопок в цикле

        messages = []; # массив сообщений (текст каждого мы будем выводить на кнопке)

        i = 1 # счётчик цикла
        while i < 15: # прописываем условие
            button = QPushButton("Сообщение " + str(i)) # (конкатенация) добавляем номер сообщения
            messages.append(button)
            i = i + 1
        for m in messages:
            vbox.addWidget(m) # добавляем на вертикальный слой  ещё кнопку


        self.setLayout(vbox) #добвыляем вертикальный слой на форму

        self.resize(600, 250)

##        ForumWindow.verticalLayout = QtGui.QVBoxLayout(ForumWindow)
##        ForumWindow.verticalLayout.setObjectName("verticalLayout")
##
##        ForumWindow.horizontalLayout = QtGui.QHBoxLayout(ForumWindow)
##        ForumWindow.horizontalLayout.setObjectName("horizontalLayout")
##
##        ForumWindow.back = QtGui.QPushButton(ForumWindow)
##        ForumWindow.horizontalLayout.addWidget(ForumWindow.back)
##        ForumWindow.back.setToolTip("Вернуться на предыдущую страницу")
##        ForumWindow.back.setText("Назад")
##        ForumWindow.back.setLayoutDirection(QtCore.Qt.RightToLeft)