# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtCore, QtGui

from ui.httpWidget import Ui_HttpWidget
from ui.ForumWindowUi import ForumWindowUi

from PyQt4 import QtWebKit

# ForumWindow  - лишь один из примеров
# Возможной реализации графического интерфейся для
# ForumDataManager
class ForumWindow(QtGui.QMainWindow):

# dmanager - дескриптор ForumDataManager
# необходим для привязки сигналов к слотам
    def __init__(self, dmanager):
        super(ForumWindow, self).__init__()
# запускаем метод рисующий виджеты окна
        self.ui = ForumWindowUi()
        self.ui.setupUi(self, dmanager)
    def someFunc(self, ForumWindow):
        return
    def getMessages():
        return ForumDataManager.getMessagesForThread()

# Это ОСНОВНОЙ класс, реализующий вызовы, необходимые для
# обмена данными с сервером - именно к этому классу следует обращаться
# при написании нового Web CMS-драйвера (аналагично с реализованным
# драйвером для CMS Drupal 7)
class ForumDataManager:

    def __init__(self, parent=None):
         self.ui = ForumWindow(self)
         # self.messages - актуальный массив блоков (его состояние) (ВАЖНО !!)
         self.messages = self.getMessagesForThread()

    def getMessagesForThread(self): #возвращает массив сообщений
        messages = []; # массив сообщений (текст каждого мы будем выводить на кнопке)

        i = 1 # счётчик цикла
        while i < 5: # прописываем условие
            mess = ForumMessage("Сообщение " + str(i))
            messages.append(mess) # добавляем элемент
            i = i + 1
        return messages

    def newMessage(self, text): # обработик события появления нового сообщения (!)
        self.addMessage(text)
        self.updateMessageList()

    def addMessage(self, text): # пока что просто принимаем текст
        mess = ForumMessage(text)
        self.messages.append(mess) # добавляем элемент

    def updateMessageList(self):
        self.clear()
        self.printMessages()

    def printMessages(self):
        self.ui.ui.print_messages(self.messages)

    def clear(self): # очищает прокручивающееся поле блока сообщений
        self.ui.ui.clear_messages_block()



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

