"""Test app to show how to dynamically add/remove widgets in a scroll
area."""

import sys

from PyQt4 import QtCore
from PyQt4 import QtGui


class MyWidget(QtGui.QFrame):
    """Simple composite widget."""

    def __init__(self, parent=None):
        QtGui.QFrame.__init__(self, parent)

        # ==== members ====
        self._title = ""
        self._text = None
        self._slider = None

        # ==== setup ====
        self.setFrameStyle(QtGui.QFrame.StyledPanel)

        self._title = QtGui.QLabel("No Title")
        self._text = QtGui.QLineEdit()
        self._slider = QtGui.QSlider(QtCore.Qt.Horizontal)

        l = QtGui.QVBoxLayout()
        l.addWidget(self._title)
        l.addWidget(self._text)
        l.addWidget(self._slider)

        self.setLayout(l)

        #self.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)

    def setTitle(self, t):
        self._title.setText("<h3>%s</h3>" % t)


counts = 0
def addOne():
    global counts
    w = MyWidget()
    w.setTitle("Widget Number %d" % counts)
    l.addWidget(w)
    counts += 1


app = QtGui.QApplication(sys.argv)
win = QtGui.QMainWindow()

tbar = QtGui.QToolBar()
a = tbar.addAction(QtGui.QIcon(":/trolltech/styles/commonstyle/images/newdirectory-16.png"), "Add")
a.triggered.connect(addOne)
win.addToolBar(tbar)

s = QtGui.QScrollArea()
l = QtGui.QVBoxLayout()
s.setLayout(l)
win.setCentralWidget(s)

win.setWindowTitle("Test...")
win.show()
sys.exit(app.exec_())
