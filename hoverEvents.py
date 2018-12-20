import sys

from PiSide2.QtCore import *
from PiSide2.QtGui import *

class eventFilterWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        widget = QWidget()

        button = QPushButton("Trigger event!")
        button.installEventFilter(self)

        hbox = QHBoxLayout()
        hbox.addWidget(button)
        widget.setLayout(hbox)
        self.setCentralWidget(widget)
        self.show()

    def eventFilter(self, object, event):

        if event.type() == QEvent.MouseButtonPress:
            print 'mouth button press '
            return True

        elif event.type() == QEvent.HoverEnter:
            print 'hover enter'
            return True
        elif event.type() == QEvent.HoverLeave:
            print 'hover leave'
            return True
        elif event.type() == QEvent.HoverMove:
            print 'hover move'
            return True

        return False

# window.delteLater()
window = eventFilterWindow()
