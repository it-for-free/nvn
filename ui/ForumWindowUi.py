# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit

import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui
# следующее  - импортируется для работы со слотами
from PyQt4.QtCore import QObject, pyqtSlot
from PyQt4 import QtCore, QtGui
import functools # необходимо чтобы использовать partial

"""
класс который мы опишем ниже
будет отвечать а внешний вид
нашего первобытного браузера
"""
class ForumWindowUi(object):

    def setupUi(self, ForumWindow):
        ForumWindow.setWindowTitle('Модуль форума')
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

      #  ok = QtGui.QPushButton("OK")
      #  cancel = QtGui.QPushButton("Cancel")

        hbox = QtGui.QHBoxLayout()
       # button1 = QPushButton("Сообщение 1")
       # button2 = QPushButton("Сообщение 2")

        vbox = QtGui.QVBoxLayout() #  создаёем вертикальный слой
        vbox.addStretch(1)
       # vbox.addWidget(button1) # добавляем первую кновку в вертикальном
# добавляем горизонтальный на вертикальный (а вместе с ним и все кнопки)
        vbox.addLayout(hbox)
       # vbox.addWidget(button2) # добавляем на вертикальный слой  ещё кнопку


        hbox.addStretch(1)
       # hbox.addWidget(ok)
      #  hbox.addWidget(cancel)

# Дальше потренируемся выводить переменное число кнопок в цикле



        # определяем содержимое виджета прокрутки
        #  - а именно слой формата (QFormLayout) - два столбца
        self.scrollLayout = QtGui.QFormLayout()

        # добавляем  ране созданный слой прокрутки
        # на виджет прокрутки
        self.scrollWidget = QtGui.QWidget() # cначала создаём сам виджет
        self.scrollWidget.setLayout(self.scrollLayout) # добавляем на него слой

        # определяем область механизм прокрутки (QScrollArea)
        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setWidgetResizable(True) #разрешаем проктурку
        #добавляем на область виджет, с ранее добавленным на него слоем слоем
        self.scrollArea.setWidget(self.scrollWidget)

        vbox.addWidget(self.scrollArea) # добавляем область прокрутки

        messages = []; # массив сообщений (текст каждого мы будем выводить на кнопке)

        i = 1 # счётчик цикла
        while i < 15: # прописываем условие
            text = "Сообщение " + str(i);
            button = QPushButton(text) # (конкатенация) добавляем номер сообщения
            #button.clicked.connect(lambda: self.show_message(text)) # не катит
            button.clicked.connect(functools.partial(self.show_print_message_window,text))
            messages.append(button)
            i = i + 1
        #messages =   ForumDataManager.getMessagesForThread

        for m in messages:
            #vbox.addWidget(m) # добавляем на вертикальный слой  ещё кнопку
            self.scrollLayout.addRow(m)


        self.vbox = vbox
        self.setLayout(vbox) #добвыляем вертикальный слой на форму

        self.resize(600, 250)

    # fwindow   - дескриптор главного окна форума
    def show_message(self, fwindow, text): # text  - передаваемый параметр (текст)
        QMessageBox.about(self, "некая подпись" ,"вы нажали на = " + text)

        vbox = QtGui.QVBoxLayout() #  создаёем вертикальный слой
        b2 = QPushButton(text);
        vbox.addWidget(b2)

        fwindow.setLayout(vbox)

        #for i in range(fwindow.vbox.count()): fwindow.vbox.itemAt(i).widget().close()

        for i in reversed(range(fwindow.vbox.count())):
            if fwindow.vbox.itemAt(i).widget() != None: # проверяем, что значение определено
                fwindow.vbox.itemAt(i).widget().setParent(None)
        b2 = QPushButton(text);
        fwindow.vbox.addWidget(b2)
    #def add_message(fwindow, ):


    def show_print_message_window(self, text): # text  - передаваемый параметр (текст)
        self.show_print_message_window = PrintMessageWindow(self)


# это окно будет использоваться чтобы написать сообщение для форума
class PrintMessageWindow(QWidget):

    def __init__(self, fwindow):
        super(PrintMessageWindow, self).__init__()

        self.setWindowTitle('Набор сообщения')

        ok = QtGui.QPushButton("OK")
        cancel = QtGui.QPushButton("Cancel")

        textbox = QTextEdit() # поле для ввода текста

        ac = QtGui.QAction("Insert AAA", textbox) # определяем действие
        ac.setShortcut(QtGui.QKeySequence("Ctrl+Space")) # определяем "горячую" комбинацию
        textbox.addAction(ac) # подключаем действие к полю ввода
        text = "текстовый параметр"
        # ниже прицепляем к действиею функцию вывода сообщения + можем указат
        # конкретный параметр  - который будет использован при вызове функции
        #ac.triggered.connect(functools.partial(FormWidget.show_message, self, textbox.toPlainText()))
        ac.triggered.connect(lambda: FormWidget.show_message (self, fwindow, textbox.toPlainText()))
        hbox = QtGui.QHBoxLayout()
        button1 = QPushButton("Сообщение 1")
        button2 = QPushButton("Сообщение 2")

        vbox = QtGui.QVBoxLayout() #  создаёем вертикальный слой
        vbox.addWidget(textbox)


        self.setLayout(vbox) #добвыляем вертикальный слой на форму
        self.resize(450, 250)
        self.show()

class MyTextEdit(QtGui.QTextEdit):
    def __init__(self,):
        QtGui.QTextEdit.__init__(self)
        self.ctrlIsPressed = False
    def keyPressEvent(self, event):
        #FormWidget.show_print_message_window(self, "123")
        if self.ctrlIsPressed:
        # и вот тут надо что то написать, что б курсор передвинулся
        # наверное либо сэмулировать нажатие стрелочки
        # либо как то програмно передвинуть курсор
            FormWidget.show_message(self, '123')
        else:
            QtGui.QTextEdit.keyPressEvent(self, event)