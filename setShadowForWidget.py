# -*- coding:utf-8 -*-
  
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
  
class testShadow(QWidget):
  
  
    """图片相册阴影效果"""
  
    def __init__(self, parent=None):
  
        super(testShadow, self).__init__(parent)
  
        #设置主窗体属性
        self.resize(960,480)
        self.setStyleSheet("background-color:#ccc")
        self.setWindowTitle(u"PyQt图片显示特效 V0.5 Beta")
  
        #创建lable,稍后将使用setPixmap绘制图片
        self.label = QLabel(self)
        self.label.setStyleSheet("border:5px solid #fff;margin:20px 0 0 20px;")
  
        #预加载图片
        self.img_=QImage(self)
        self.img_.load('.\GUILibs\IMG_0122.JPG')
  
        #图片显示
        self.label.setPixmap(QPixmap().fromImage(self.img_).scaled(QSize(240,120),Qt.KeepAspectRatio))
  
        #阴影效果
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setOffset(5,5)
        self.label.setGraphicsEffect(self.shadow)
  
  
  
if __name__ == "__main__":
  
    app = QApplication(sys.argv)
    main = testShadow()
    main.show()
    sys.exit(app.exec_())
