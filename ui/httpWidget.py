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
class Ui_HttpWidget(object):

#в контсрукторе получаем класс типа HttpWidget """
    def setAccessibleName(self,name):
        return
    def setupUi(self, HttpWidget):



        HttpWidget.setObjectName("HttpWidget")
        HttpWidget.resize(500, 336)

        self.verticalLayout = QtGui.QVBoxLayout(HttpWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # добавляем кнопку "предыдущая(назад)"
        self.back = QtGui.QPushButton(HttpWidget)
        self.horizontalLayout.addWidget(self.back)


        # добавляем кнопку "следующая(вперёд)"
        self.next = QtGui.QPushButton(HttpWidget)
        self.next.setEnabled(True) # разрешаем нажатие
        self.next.setLayoutDirection(QtCore.Qt.RightToLeft)



        #self.next.setObjectName("next")
        self.next.setAccessibleName("Следующая")
        self.horizontalLayout.addWidget(self.next)

        # добавляем кнопку остановки загрузки
        self.stop = QtGui.QPushButton(HttpWidget)
        #self.stop.setObjectName("stop")
        self.stop.setAccessibleName("Остановить загрузку")
        self.horizontalLayout.addWidget(self.stop)

        # добавляем кнопку перезагрузки страницы
        self.reload = QtGui.QPushButton(HttpWidget)
        # self.reload.setObjectName("reload")
        self.reload.setAccessibleName("Перезагрузить страницу")
        self.horizontalLayout.addWidget(self.reload)

        # добавляем адресную строку )))))
        self.url = QtGui.QLineEdit(HttpWidget)
        self.url.setObjectName("url")
        self.horizontalLayout.addWidget(self.url)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # добавляем кнопку перезагрузки страницы
        self.forum = QtGui.QPushButton(HttpWidget)
        # self.reload.setObjectName("reload")
        self.reload.setAccessibleName("Открыть модуль форума")
        self.horizontalLayout.addWidget(self.forum)

        # а вот и закрепление вебкита! =))
        self.webView = QtWebKit.QWebView(HttpWidget)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)

        self.retranslateUi(HttpWidget)#запускаем перевод


    # определяем метод для перевода надписей
    def retranslateUi(self, HttpWidget):

        #translate() необходима дял возможно перевода текста
        HttpWidget.setWindowTitle(QtGui.QApplication.translate("HttpWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

        self.back.setToolTip("Вернуться на предыдущую страницу")
        self.back.setText("Назад")

        self.forum.setToolTip("Нажмите на эту кнопку чтобы открыть сайт")
        self.forum.setText("Форум")

        self.next.setToolTip(QtGui.QApplication.translate("HttpWidget", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.next.setText(QtGui.QApplication.translate("HttpWidget", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setToolTip(QtGui.QApplication.translate("HttpWidget", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setText(QtGui.QApplication.translate("HttpWidget", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.reload.setToolTip(QtGui.QApplication.translate("HttpWidget", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.reload.setText(QtGui.QApplication.translate("HttpWidget", "Reload", None, QtGui.QApplication.UnicodeUTF8))
