import re

from PyQt4 import QtCore
from PyQt4 import QtGui


class ColorButton(QtGui.QPushButton):
    def __init__(self, color=None, parent=None):
        super(ColorButton, self).__init__(parent=parent)

        self.setObjectName("color_button")
        self.setColor(color)

        self.clicked.connect(self._runColorPicker)

    def clearColor(self):
        self.setColor(None)

    def setColor(self, color):
        if not color:
            self.setStyleSheet("")
        else:
            rgb = (color.red(), color.green(), color.blue())
            self.setStyleSheet("#color_button { background-color: rgb(%d,%d,%d) }" % rgb)

    def color(self):
        m = re.compile(r"rgb\((\d+),(\d+),(\d+)\)").search(self.styleSheet())
        if m:
            rgb = (int(m.group(gidx)) for gidx in (1, 2, 3))
            ret = QtGui.QColor(*rgb)
        else:
            ret = None
        return ret

    def _runColorPicker(self):
        if self.color() is not None:
            dialog = QtGui.QColorDialog(self.color(), parent=self)
        else:
            dialog = QtGui.QColorDialog(parent=self)

        if dialog.exec_():
            self.setColor(dialog.selectedColor())
