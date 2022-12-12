import sys
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow
from PySide6 import QtCore, QtWidgets, QtGui

import PySide6.QtCore

import random

from PySide6.QtCharts import QChart, QSplineSeries, QValueAxis ,QChartView
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import (QPainter,QPen)

from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QToolBar, QMainWindow)

from chart import Chart
import chart

import serial

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int32

import subprocess
 
reply=subprocess.getstatusoutput("")
print(reply)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_slot()
        self.ui.ros_init()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    # window.show()
    
    window_Q = QMainWindow()
    
    chart = Chart()
    chart.setTitle("Speed")
    chart.legend().hide()
    chart.setAnimationOptions(QChart.AllAnimations)
    chart_view = QChartView(chart)
    chart_view.setRenderHint(QPainter.Antialiasing)
    
    # chart_view.show()
        
    main_widget = QtWidgets.QWidget()
    
    main_layout = QVBoxLayout()
    main_layout.addWidget(window)
    main_layout.addWidget(chart_view)
    
    main_widget.setLayout(main_layout)
    
    main_widget.setWindowTitle("PC controller")
    main_widget.show()
    
    main_widget.resize(800, 700)
    main_widget.setFixedSize(800, 700)
    
    
    print("Start Success")
    sys.exit(app.exec())
