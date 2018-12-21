from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QMovie

class gifLabel(QtWidgets.QLable):
    def __init__(self, parent = None):
        self.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.setObjectName("label")
    def start(self , gifFile):
        self.gif = QMovie(gifFile)
        self.setMovie(self.gif)
        self.gif.start()
    def stop(self):
        self.gif.stop()

##player = gifLabel()
##player.play('../...gif')
##player.stop()


### example 2
import sys
import os
import time
 #from myUI import Ui_MainWindow #导入生成myUI.py里生成的类
from tab import Ui_testTAB
from PyQt5 import QtWidgets, QtGui, QtCore 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#打开gif文件
movie = QtGui.QMovie("./icon/watch.gif") 
#设置cacheMode为CacheAll时表示gif无限循环，注意此时loopCount()返回-1
movie.setCacheMode(QtGui.QMovie.CacheAll) 
#播放速度
movie.setSpeed(100) 
#self.movie_screen是在qt designer里定义的一个QLabel对象的对象名，将gif显示在label上
self.movie_screen.setMovie(movie)   
#开始播放，对应的是movie.start()
movie.start()
--------------------- 
作者：Mengwei_Ren 
来源：CSDN 
原文：https://blog.csdn.net/Mengwei_Ren/article/details/72566991 
版权声明：本文为博主原创文章，转载请附上博文链接！
