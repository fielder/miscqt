import sys

from PyQt4 import QtCore
from PyQt4 import QtGui


images = [  ":/trolltech",
            ":/trolltech/qmessagebox",
            ":/trolltech/qmessagebox/images",
            ":/trolltech/qmessagebox/images/qtlogo-64.png",
            ":/trolltech/styles",
            ":/trolltech/styles/commonstyle",
            ":/trolltech/styles/commonstyle/images",
            ":/trolltech/styles/commonstyle/images/networkdrive-16.png",
            ":/trolltech/styles/commonstyle/images/networkdrive-32.png",
            ":/trolltech/styles/commonstyle/images/dvd-16.png",
            ":/trolltech/styles/commonstyle/images/cdr-16.png",
            ":/trolltech/styles/commonstyle/images/up-16.png",
            ":/trolltech/styles/commonstyle/images/up-32.png",
            ":/trolltech/styles/commonstyle/images/dvd-32.png",
            ":/trolltech/styles/commonstyle/images/cdr-32.png",
            ":/trolltech/styles/commonstyle/images/left-32.png",
            ":/trolltech/styles/commonstyle/images/stop-32.png",
            ":/trolltech/styles/commonstyle/images/file-16.png",
            ":/trolltech/styles/commonstyle/images/down-16.png",
            ":/trolltech/styles/commonstyle/images/stop-24.png",
            ":/trolltech/styles/commonstyle/images/left-16.png",
            ":/trolltech/styles/commonstyle/images/down-32.png",
            ":/trolltech/styles/commonstyle/images/file-32.png",
            ":/trolltech/styles/commonstyle/images/dirlink-32.png",
            ":/trolltech/styles/commonstyle/images/diropen-32.png",
            ":/trolltech/styles/commonstyle/images/diropen-16.png",
            ":/trolltech/styles/commonstyle/images/dirlink-16.png",
            ":/trolltech/styles/commonstyle/images/networkdrive-128.png",
            ":/trolltech/styles/commonstyle/images/media-volume-muted-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-cancel-128.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-open-128.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-apply-32.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-apply-16.png",
            ":/trolltech/styles/commonstyle/images/fonttruetype-16.png",
            ":/trolltech/styles/commonstyle/images/newdirectory-128.png",
            ":/trolltech/styles/commonstyle/images/filecontents-128.png",
            ":/trolltech/styles/commonstyle/images/floppy-128.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-delete-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-delete-32.png",
            ":/trolltech/styles/commonstyle/images/harddrive-128.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-clear-32.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-close-32.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-clear-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-close-16.png",
            ":/trolltech/styles/commonstyle/images/dirclosed-128.png",
            ":/trolltech/styles/commonstyle/images/trash-128.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-apply-128.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-yes-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-yes-32.png",
            ":/trolltech/styles/commonstyle/images/fontbitmap-16.png",
            ":/trolltech/styles/commonstyle/images/newdirectory-32.png",
            ":/trolltech/styles/commonstyle/images/dirclosed-32.png",
            ":/trolltech/styles/commonstyle/images/newdirectory-16.png",
            ":/trolltech/styles/commonstyle/images/dirclosed-16.png",
            ":/trolltech/styles/commonstyle/images/up-128.png",
            ":/trolltech/styles/commonstyle/images/media-pause-32.png",
            ":/trolltech/styles/commonstyle/images/media-pause-16.png",
            ":/trolltech/styles/commonstyle/images/cdr-128.png",
            ":/trolltech/styles/commonstyle/images/dvd-128.png",
            ":/trolltech/styles/commonstyle/images/media-volume-16.png",
            ":/trolltech/styles/commonstyle/images/harddrive-32.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-cancel-16.png",
            ":/trolltech/styles/commonstyle/images/harddrive-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-closetab-hover-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-cancel-32.png",
            ":/trolltech/styles/commonstyle/images/viewdetailed-128.png",
            ":/trolltech/styles/commonstyle/images/right-128.png",
            ":/trolltech/styles/commonstyle/images/fileinfo-16.png",
            ":/trolltech/styles/commonstyle/images/filelink-16.png",
            ":/trolltech/styles/commonstyle/images/filelink-32.png",
            ":/trolltech/styles/commonstyle/images/fileinfo-32.png",
            ":/trolltech/styles/commonstyle/images/dirlink-128.png",
            ":/trolltech/styles/commonstyle/images/media-seek-forward-16.png",
            ":/trolltech/styles/commonstyle/images/media-seek-forward-32.png",
            ":/trolltech/styles/commonstyle/images/diropen-128.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-help-128.png",
            ":/trolltech/styles/commonstyle/images/viewdetailed-16.png",
            ":/trolltech/styles/commonstyle/images/viewdetailed-32.png",
            ":/trolltech/styles/commonstyle/images/media-seek-backward-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-ok-128.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-no-128.png",
            ":/trolltech/styles/commonstyle/images/media-seek-backward-32.png",
            ":/trolltech/styles/commonstyle/images/refresh-32.png",
            ":/trolltech/styles/commonstyle/images/refresh-24.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-save-128.png",
            ":/trolltech/styles/commonstyle/images/viewlist-128.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-yes-128.png",
            ":/trolltech/styles/commonstyle/images/computer-32.png",
            ":/trolltech/styles/commonstyle/images/computer-16.png",
            ":/trolltech/styles/commonstyle/images/parentdir-32.png",
            ":/trolltech/styles/commonstyle/images/parentdir-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-closetab-16.png",
            ":/trolltech/styles/commonstyle/images/media-play-16.png",
            ":/trolltech/styles/commonstyle/images/desktop-16.png",
            ":/trolltech/styles/commonstyle/images/media-stop-16.png",
            ":/trolltech/styles/commonstyle/images/desktop-32.png",
            ":/trolltech/styles/commonstyle/images/media-play-32.png",
            ":/trolltech/styles/commonstyle/images/down-128.png",
            ":/trolltech/styles/commonstyle/images/media-stop-32.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-delete-128.png",
            ":/trolltech/styles/commonstyle/images/media-skip-backward-32.png",
            ":/trolltech/styles/commonstyle/images/media-skip-backward-16.png",
            ":/trolltech/styles/commonstyle/images/viewlist-16.png",
            ":/trolltech/styles/commonstyle/images/viewlist-32.png",
            ":/trolltech/styles/commonstyle/images/file-128.png",
            ":/trolltech/styles/commonstyle/images/floppy-32.png",
            ":/trolltech/styles/commonstyle/images/left-128.png",
            ":/trolltech/styles/commonstyle/images/floppy-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-no-32.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-ok-32.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-no-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-ok-16.png",
            ":/trolltech/styles/commonstyle/images/media-skip-forward-32.png",
            ":/trolltech/styles/commonstyle/images/media-skip-forward-16.png",
            ":/trolltech/styles/commonstyle/images/filelink-128.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-open-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-open-32.png",
            ":/trolltech/styles/commonstyle/images/fileinfo-128.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-help-32.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-help-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-save-16.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-save-32.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-closetab-down-16.png",
            ":/trolltech/styles/commonstyle/images/parentdir-128.png",
            ":/trolltech/styles/commonstyle/images/filecontents-32.png",
            ":/trolltech/styles/commonstyle/images/trash-32.png",
            ":/trolltech/styles/commonstyle/images/filecontents-16.png",
            ":/trolltech/styles/commonstyle/images/trash-16.png",
            ":/trolltech/styles/commonstyle/images/right-16.png",
            ":/trolltech/styles/commonstyle/images/right-32.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-clear-128.png",
            ":/trolltech/styles/commonstyle/images/standardbutton-close-128.png",
            ":/trolltech/styles/macstyle",
            ":/trolltech/styles/macstyle/images",
            ":/trolltech/styles/macstyle/images/dockdock-down-16.png",
            ":/trolltech/styles/macstyle/images/closedock-16.png",
            ":/trolltech/styles/macstyle/images/dockdock-16.png",
            ":/trolltech/styles/macstyle/images/closedock-down-16.png",
            ":/trolltech/dialogs",
            ":/trolltech/dialogs/qprintpreviewdialog",
            ":/trolltech/dialogs/qprintpreviewdialog/images",
            ":/trolltech/dialogs/qprintpreviewdialog/images/view-page-sided-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/view-page-sided-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/view-page-multi-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/view-page-multi-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/go-previous-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/go-previous-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/go-last-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/go-next-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/go-last-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/go-next-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/layout-landscape-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/layout-landscape-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/view-page-one-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/view-page-one-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/go-first-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/go-first-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/layout-portrait-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/layout-portrait-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/page-setup-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/page-setup-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/fit-width-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/fit-width-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/zoom-out-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/zoom-out-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/zoom-in-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/zoom-in-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/print-32.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/print-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/fit-page-24.png",
            ":/trolltech/dialogs/qprintpreviewdialog/images/fit-page-32.png",
            ":/trolltech/dialogs/qprintdialog",
            ":/trolltech/dialogs/qprintdialog/images",
            ":/trolltech/dialogs/qprintdialog/images/status-color.png",
            ":/trolltech/dialogs/qprintdialog/images/status-gray-scale.png" ]


app = QtGui.QApplication(sys.argv)
win = QtGui.QMainWindow()

def copyToClipboard():
    app.clipboard().setText(QtCore.QObject.sender().toolTip())

grid = QtGui.QGridLayout()
row = 0
col = 0
for idx, path in enumerate(filter(lambda p: p.endswith(".png"), images)):
    tb = QtGui.QToolButton()
    tb.setIcon(QtGui.QIcon(path))
    tb.setToolTip(path)
    tb.clicked.connect(copyToClipboard)
    grid.addWidget(tb, row, col, 1, 1)
    col += 1
    if (col % 10) == 0:
            col = 0
	row += 1

vbox = QtGui.QVBoxLayout()
vbox.addWidget(QtGui.QLabel("Click a button to copy its path to the clip-board"))
vbox.addLayout(grid)

w = QtGui.QWidget()
w.setLayout(vbox)
scrollarea = QtGui.QScrollArea(win)
scrollarea.setWidget(w)

win.setCentralWidget(scrollarea)
win.setWindowTitle("PyQT icon browser")
win.show()
win.resize(330, 530)

sys.exit(app.exec_())
