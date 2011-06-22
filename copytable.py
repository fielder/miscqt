from PyQt4 import QtCore
from PyQt4 import QtGui


#TODO: copy horizontal/vertical headers when ctrl-c ?

class CopyableQTableWidget(QtGui.QTableWidget):
    """QTableWidget with ctrl-c capability."""

    COL_SEPARATOR = '\t'
    ROW_SEPARATOR = '\n'

    def __init__(self, parent=None):
        QtGui.QTableWidget.__init__(self, parent)

        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        a = QtGui.QAction("&Copy", self)
        a.setShortcut(QtGui.QKeySequence.Copy)
        self.addAction(a)
        a.triggered.connect(self.copySelectionToClipboard)

    def copySelectionToClipboard(self):
        if not self.selectedItems():
            return

        # Find bounds of selection
        min_row = 9999999
        max_row = -9999999
        min_col = 9999999
        max_col = -9999999
        for item in self.selectedItems():
            if item.row() < min_row:
                min_row = item.row()
            if item.row() > max_row:
                max_row = item.row()
            if item.column() < min_col:
                min_col = item.column()
            if item.column() > max_col:
                max_col = item.column()
        num_rows = (max_row - min_row) + 1
        num_cols = (max_col - min_col) + 1

        # Make a table containing the selected items in correct
        #  locations, None if a cell isn't selected.
        selected_items = [] # list of rows
        for i in xrange(num_rows):
            selected_items.append([None for j in xrange(num_cols)])

        # Populate table
        for item in self.selectedItems():
            selected_items[item.row() - min_row][item.column() - min_col] = item

        # Create the text
        text = ""
        for r in xrange(num_rows):
            for c in xrange(num_cols):
                item = selected_items[r][c]

                if item is not None:
                    text += item.text()
                if c < num_cols - 1:
                    text += self.COL_SEPARATOR

            text += self.ROW_SEPARATOR

        QtGui.QApplication.clipboard().setText(text)

