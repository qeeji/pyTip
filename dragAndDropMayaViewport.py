import maya.cmds as mc
import maya.mel as mm
import maya.OpenMayaUI as omui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin, MayaQWidgetDockableMixin
from shiboken2 import wrapInstance
import os
import sys
from pprint import pprint

# set global values for the main window

def getMayaWindow():
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(mayaMainWindowPtr), QWidget)

class MainWindowFilter(QObject):
    def eventFilter(self, receiver, event):
        self.receiver = receiver
        """
        if event.type() is QEvent.Enter:
            print("ENTER EVENT, FOOL!")
            self.mouse_button = QApplication.mouseButtons()
            #event.accept()
            return False
        """    
        if event.type() is QEvent.DragEnter:
            print("DRAG ENTERED!")
            event.accept()
            
            """
            if e.mimeData().hasFormat('text/plain'):
                event.accept()
            else:
                event.ignore() 
            """
            
        if event.type() is QEvent.Drop:
            print("DROPPED")
            library_w = event.source()
            if self.mouse_button == Qt.LeftButton:
                print 'you dropped the bomb.'
            else:
                print 'nothing dropped.'
                
        return False
        
global filter
filter = MainWindowFilter()
    
              
class CreateMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(CreateMainWindow, self).__init__(*args, **kwargs)
        
        self.mayaMainWindow = getMayaWindow()
        
        self.mayaMainWindow.setAcceptDrops(True)  
        self.mayaMainWindow.installEventFilter(filter)
 
        self.initUI()
               
        
    def initUI(self):
        mainHBox = QHBoxLayout(self)    

        label1 = MyLabel(self)
        
        mainHBox.addWidget(label1)        
        # Parent under main Maya window
        self.setParent(self.mayaMainWindow)
        self.setWindowFlags(Qt.Window)
        
        #self.setObjectName('CreateMainWindow_611')
        self.setWindowTitle('Drag This')
        self.setGeometry(100, 100, 550, 350)
        
        

    def closeEvent(self, e):
        '''
        Make sure the eventFilter is removed
        '''
        print 'closeEvent'
        self.mayaMainWindow.removeEventFilter(filter)
        return super(CreateMainWindow, self).closeEvent(e)

                    
class MyLabel(QLabel):
    def __init__(self, parent):
        super(MyLabel, self).__init__(parent)

        self.setStyleSheet("""
            background-color: black;
            color: white;
            font: bold;
            padding: 6px;
            border-width: 2px;
            border-style: solid;
            border-radius: 16px;
            border-color: white;
        """)
        
    def mouseMoveEvent(self, e):
        print 'e.buttons() = {}'.format(e.buttons())
        if e.buttons() != Qt.LeftButton:
            print 'Left button not detected.'
            return
        else:
            print 'Left button press detected.'

        # grab the button to a pixmap
        pixmap = QPixmap.grabWidget(self)


        # write the relative cursor position to mime data
        mimeData = QMimeData()
        # simple string with 'x,y'
        mimeData.setText('%d,%d' % (e.x(), e.y()))

        # make a QDrag
        drag = QDrag(self)
        # put our MimeData
        drag.setMimeData(mimeData)
        # set its Pixmap
        drag.setPixmap(pixmap)
        # shift the Pixmap so that it coincides with the cursor position
        drag.setHotSpot(e.pos())

        
        # below makes the pixmap half transparent
        painter = QPainter(pixmap)
        painter.setCompositionMode(painter.CompositionMode_DestinationIn)
        painter.fillRect(pixmap.rect(), QColor(0, 0, 0, 127))
        painter.end()

        mainWinDrag = QDrag(self)
        dropAction = drag.start(Qt.MoveAction)
        # start the drag operation
        # exec_ will return the accepted action from dropEvent
        #drag.exec_(Qt.DropAction.)
        if dropAction == Qt.MoveAction:
            print 'moved'
        else:
            print 'MoveAction = {}'.format(drag.exec_(Qt.MoveAction))
            print 'copied'

         
def main():
    ui = CreateMainWindow()
    ui.show()
    # ui.show(dockable=True, floating=True)

main()
