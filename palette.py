import collections
import re

from PyQt4 import QtCore
from PyQt4 import QtGui


class ColorCell(QtGui.QPushButton):
    hovered = QtCore.pyqtSignal(bool)

    def __init__(self, color=None, parent=None):
        super(ColorCell, self).__init__(parent=parent)

        self.setColor(color)

    def clearColor(self):
        self.setColor(None)

    def setColor(self, color):
        if not color:
            self.setStyleSheet("")
        else:
            self.setStyleSheet("* { background-color: rgb(%d,%d,%d) }" % (color.red(),
                                                                          color.green(),
                                                                          color.blue()))

    def color(self):
        pat = "rgb\\((\\d+),(\\d+),(\\d+)\\)"
        m = re.compile(pat).search(self.styleSheet())
        if not m:
            return None
        r, g, b = [int(m.group(gidx)) for gidx in (1, 2, 3)]
        return QtGui.QColor(r, g, b)

    def enterEvent(self, ev):
        self.hovered.emit(True)
        ev.accept()

    def leaveEvent(self, ev):
        self.hovered.emit(False)
        ev.accept()


class EditableRGBColorCell(ColorCell):
    def mouseReleaseEvent(self, ev):
        if ev.button() == QtCore.Qt.MiddleButton:
            # Note we use self.parent() as the dialog's parent and not
            # self. Using self causes the dialog's background to be the
            # same as the button's background, making for a real shitty
            # view.
            if self.color() is not None:
                dialog = QtGui.QColorDialog(self.color(), parent=self.parent())
            else:
                dialog = QtGui.QColorDialog(parent=self.parent())
            if dialog.exec_():
                self.setColor(dialog.selectedColor())
            ev.accept()
        else:
            super(EditableRGBColorCell, self).mouseReleaseEvent(ev)


class ReadOnlyColorCell(ColorCell):
    def mousePressEvent(self, ev):
        ev.ignore()


class PaletteColorCell(ColorCell):
    def sizeHint(self):
        return QtCore.QSize(32, 32)


class _PreviewCell(ReadOnlyColorCell):
    def sizeHint(self):
        return QtCore.QSize(128, 128)


class IndexedColorPicker(QtGui.QWidget):
    """
    A interface to show a 256-color palette, where one cell is
    selectable.
    """

    def __init__(self, colors={}, parent=None):
        super(IndexedColorPicker, self).__init__(parent=parent)

        # main color grid
        self._buttongroup = QtGui.QButtonGroup(parent=self)
        self._grid = QtGui.QGridLayout()
        for r in xrange(16):
            for c in xrange(16):
                coloridx = r * 16 + c

                cell = PaletteColorCell(color=colors.get(coloridx))
                cell.setCheckable(True)
                if (r, c) == (0, 0):
                    cell.setChecked(True)
                cell.hovered.connect(self._cellHovered)

                self._buttongroup.addButton(cell, coloridx)

                self._grid.addWidget(cell, r, c)

        vbox = QtGui.QVBoxLayout()

        # preview cell
        self._preview = _PreviewCell()
        vbox.addWidget(self._preview)

        # text labels
        self._labels = collections.OrderedDict()
        self._labels["index"] = QtGui.QLabel("Index:")
        self._labels["red"]   = QtGui.QLabel("Red:")
        self._labels["green"] = QtGui.QLabel("Green:")
        self._labels["blue"]  = QtGui.QLabel("Blue:")
        for l in self._labels.itervalues():
            vbox.addWidget(l)

        vbox.addStretch()

        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(self._grid)
        hbox.addLayout(vbox)

        self.setLayout(hbox)

    def selected(self):
        return (self._buttongroup.checkedId(), self._buttongroup.checkedButton().color())

    def _cellHovered(self, is_on):
        color = self.sender().color()
        idx = self._buttongroup.id(self.sender())
        if is_on and color:
            self._labels["index"].setText("Index: %d" % idx)
            self._labels["red"].setText("Red: %d" % color.red())
            self._labels["green"].setText("Green: %d" % color.green())
            self._labels["blue"].setText("Blue: %d" % color.blue())
            self._preview.setColor(color)
        else:
            self._labels["index"].setText("Index:")
            self._labels["red"].setText("Red:")
            self._labels["green"].setText("Green:")
            self._labels["blue"].setText("Blue:")
            self._preview.clearColor()


if __name__ == "__main__":
    import sys
    import random

    randcolors = {i:QtGui.QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for i in xrange(18)}
    randcolors[7] = None
    randcolors[8] = None
    randcolors[11] = None

    app = QtGui.QApplication(sys.argv)

    win = QtGui.QMainWindow()
    win.setCentralWidget(IndexedColorPicker(colors=randcolors))
    win.setWindowTitle("Palette Widget")
    win.setWindowIcon(QtGui.QIcon(":/trolltech/qmessagebox/images/qtlogo-64.png"))
    win.show()
    win.resize(640, 480)

    sys.exit(app.exec_())
