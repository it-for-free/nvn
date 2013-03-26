# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtCore, QtGui

from ui.httpWidget import Ui_HttpWidget
from ui.ForumWindowUi import ForumWindowUi
from ForumModule import ForumWindow

from PyQt4 import QtWebKit



class httpWidget(QtGui.QWidget):
    # конструктор класса
  def __init__(self, parent=None):
    super(httpWidget, self).__init__(parent)

# привязываем атрибут ui - user interface
    self.ui = Ui_HttpWidget()
    self.ui.setupUi(self)
    self.ty = 12

  # устанавливаем отступы
    l = self.layout()
    l.setMargin(10)
    #добавляем слой и определяем отступы
    self.ui.horizontalLayout.setMargin(5)

    # "некоммерческий" яндекс
    url = 'http://ya.ru'
    self.ui.url.setText(url)

    # load page
    self.ui.webView.setUrl(QtCore.QUrl(url))

    # history buttons:
    self.ui.back.setEnabled(False)
    self.ui.next.setEnabled(False)

# секция подключения сигналов к слотам
    QtCore.QObject.connect(self.ui.back,QtCore.SIGNAL("clicked()"), self.back)
    QtCore.QObject.connect(self.ui.next,QtCore.SIGNAL("clicked()"), self.next)
    QtCore.QObject.connect(self.ui.url,QtCore.SIGNAL("returnPressed()"), self.url_changed)
    QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("linkClicked (const QUrl&)"), self.link_clicked)
    QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("urlChanged (const QUrl&)"), self.link_clicked)
    QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("loadProgress (int)"), self.load_progress)
    QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&)"), self.title_changed)
    QtCore.QObject.connect(self.ui.reload,QtCore.SIGNAL("clicked()"), self.reload_page)
    QtCore.QObject.connect(self.ui.stop,QtCore.SIGNAL("clicked()"), self.stop_page)
    QtCore.QObject.connect(self.ui.forum,QtCore.SIGNAL("clicked()"), self.addwindow)



  def url_changed(self):
    """
    Url have been changed by user
    """
    page = self.ui.webView.page()
    history = page.history()
    if history.canGoBack(): # если есть "предыдущая" страница
	    self.ui.back.setEnabled(True)
    else:
	    self.ui.back.setEnabled(False)

    if history.canGoForward():# если есть "следующая" страница
	    self.ui.next.setEnabled(True)
    else:
	    self.ui.next.setEnabled(False)

    url = self.ui.url.text()
    self.ui.webView.setUrl(QtCore.QUrl(url))

  def stop_page(self):
    """
    останавливаем загрузку страницы
    """
    self.ui.webView.stop()

  def title_changed(self, title):
    """
    меняем заголовок окна в соответсвии с заголовком
    страницы
    """
    self.setWindowTitle(title)

  def reload_page(self):
    """
    перезагружаем страницу
    """
    self.ui.webView.setUrl(QtCore.QUrl(self.ui.url.text()))

  def link_clicked(self, url):
    """
    Если перешли по ссылке -
    то меняем адрес в адресной строке
    """
    page = self.ui.webView.page()
    history = page.history()
    if history.canGoBack():
	    self.ui.back.setEnabled(True)
    else:
	    self.ui.back.setEnabled(False)
    if history.canGoForward():
	    self.ui.next.setEnabled(True)
    else:
	    self.ui.next.setEnabled(False)

    self.ui.url.setText(url.toString())

  def load_progress(self, load):
    """
    Page load progress
    """
    if load == 100:
	    self.ui.stop.setEnabled(False)
    else:
	    self.ui.stop.setEnabled(True)

  def back(self):
    """
    Возвращаемся на преыдущую страницу
    если нажата кнопка "назад"
    """
    page = self.ui.webView.page()
    history = page.history()
    history.back()
    if history.canGoBack():
	    self.ui.back.setEnabled(True)
    else:
	    self.ui.back.setEnabled(False)

  def next(self):
    """
    переходим на следующую страницу
    если была нажат соотв. кнопка
    """
    page = self.ui.webView.page()
    history = page.history()
    history.forward()
    if history.canGoForward():
      self.ui.next.setEnabled(True)
    else:
      self.ui.next.setEnabled(False)

# с помощью декоратора указываем, что данный метод
# является слотом
 # @pyqtSlot()
  def addwindow(self):
      #""" C++: void foo() """
      self.addwin = ForumWindow()

# точка входа в программу
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = httpWidget()
  myapp.show()
  sys.exit(app.exec_())




