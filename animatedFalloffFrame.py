### animation falloff frame example
###  https://pyqt5.com/example/pyqt5%E5%8A%A8%E7%94%BB%E8%BE%B9%E6%A1%86%E9%98%B4%E5%BD%B1/

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018年9月25日
@author: Irony
@site: https://pyqt5.com, https://github.com/892768447
@email: 892768447@qq.com
@file: Test
@description: 
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit
from AnimationShadowEffect import AnimationShadowEffect  # @UnresolvedImport
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0
class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        # 绿色边框
        labelGreen = QLabel(self, pixmap=QPixmap('1.jpg').scaled(100, 100))
        layout.addWidget(labelGreen)
        aniGreen = AnimationShadowEffect(Qt.darkGreen, labelGreen)
        labelGreen.setGraphicsEffect(aniGreen)
        aniGreen.start()
        # 红色边框,圆形图片
        labelRed = QLabel(self)
        labelRed.setMinimumSize(100, 100)
        labelRed.setMaximumSize(100, 100)
        labelRed.setStyleSheet('border-image: url(1.jpg);border-radius: 50px;')
        layout.addWidget(labelRed)
        aniRed = AnimationShadowEffect(Qt.red, labelGreen)
        labelRed.setGraphicsEffect(aniRed)
        aniRed.start()
        # 蓝色边框按钮
        button = QPushButton('按钮', self)
        aniButton = AnimationShadowEffect(Qt.blue, button)
        layout.addWidget(button)
        button.setGraphicsEffect(aniButton)
        aniButton.start()
        # 青色边框输入框
        lineedit = QLineEdit(self)
        aniEdit = AnimationShadowEffect(Qt.cyan, lineedit)
        layout.addWidget(lineedit)
        lineedit.setGraphicsEffect(aniEdit)
        aniEdit.start()
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
