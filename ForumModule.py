# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtCore, QtGui

from ui.httpWidget import Ui_HttpWidget
from ui.ForumWindowUi import ForumWindowUi

from PyQt4 import QtWebKit


# Описываем дополнительное окно
class ForumWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(ForumWindow, self).__init__(parent)
# запускаем метод рисующий виджеты окна
        self.ui = ForumWindowUi()
        self.ui.setupUi(self)
    def someFunc(self, ForumWindow):
        return
    def getMessages():
        return ForumDataManager.getMessagesForThread()

# Это ОСНОВНОЙ класс, реализующий вызовы, необходимые для
# обмена данными с сервером - именно к этому классу следует обращаться
# при написании нового Web CMS-драйвера (аналагично с реализованным
# драйвером для CMS Drupal 7)
class ForumDataManager:

    def getMessagesForThread(): #возвращает массив сообщений
        messages = []; # массив сообщений (текст каждого мы будем выводить на кнопке)

        i = 1 # счётчик цикла
        while i < 5: # прописываем условие
            mess = ForumMessage("Сообщение " + str(i))
            i = i + 1
        return messages

""" класс (универсальный  -его следует использовать независимо
 от используемого сетевого драйвера и способа графического
 представления данных в
 программе-клиете - то есть NVN-forum ),
 описывающий структуру сообщения
 ----------------------
# этот класс может содержать - текст, автора, дату
# и иные сведения"""
class ForumMessage:
    def __init__(self, text):
        self.text = text # запоминаем текст

