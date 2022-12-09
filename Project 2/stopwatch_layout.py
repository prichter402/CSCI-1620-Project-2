# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stopwatch_layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Stopwatch(object):
    def setupUi(self, Stopwatch):
        Stopwatch.setObjectName("Stopwatch")
        Stopwatch.resize(800, 678)
        Stopwatch.setMinimumSize(QtCore.QSize(800, 670))
        Stopwatch.setMaximumSize(QtCore.QSize(800, 841))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        Stopwatch.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Stopwatch)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 800))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 800))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(0, 0, 800, 200))
        self.time.setMinimumSize(QtCore.QSize(800, 200))
        self.time.setMaximumSize(QtCore.QSize(800, 500))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(72)
        self.time.setFont(font)
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.lap_label = QtWidgets.QLabel(self.centralwidget)
        self.lap_label.setGeometry(QtCore.QRect(510, 160, 70, 41))
        self.lap_label.setMinimumSize(QtCore.QSize(70, 41))
        self.lap_label.setMaximumSize(QtCore.QSize(70, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(20)
        self.lap_label.setFont(font)
        self.lap_label.setObjectName("lap_label")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(190, 600, 191, 41))
        self.start_button.setMinimumSize(QtCore.QSize(191, 41))
        self.start_button.setMaximumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(18)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.lap_button = QtWidgets.QPushButton(self.centralwidget)
        self.lap_button.setEnabled(False)
        self.lap_button.setGeometry(QtCore.QRect(420, 600, 191, 41))
        self.lap_button.setMinimumSize(QtCore.QSize(191, 41))
        self.lap_button.setMaximumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(18)
        self.lap_button.setFont(font)
        self.lap_button.setObjectName("lap_button")
        self.student_label = QtWidgets.QLabel(self.centralwidget)
        self.student_label.setGeometry(QtCore.QRect(200, 160, 200, 41))
        self.student_label.setMinimumSize(QtCore.QSize(200, 41))
        self.student_label.setMaximumSize(QtCore.QSize(200, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.student_label.setFont(font)
        self.student_label.setObjectName("student_label")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(310, 540, 191, 41))
        self.save_button.setMinimumSize(QtCore.QSize(191, 41))
        self.save_button.setMaximumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.name1 = QtWidgets.QLineEdit(self.centralwidget)
        self.name1.setGeometry(QtCore.QRect(190, 220, 200, 20))
        self.name1.setMinimumSize(QtCore.QSize(200, 20))
        self.name1.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(12)
        self.name1.setFont(font)
        self.name1.setText("")
        self.name1.setObjectName("name1")
        self.name2 = QtWidgets.QLineEdit(self.centralwidget)
        self.name2.setGeometry(QtCore.QRect(190, 270, 200, 20))
        self.name2.setMinimumSize(QtCore.QSize(200, 20))
        self.name2.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name2.setFont(font)
        self.name2.setObjectName("name2")
        self.name3 = QtWidgets.QLineEdit(self.centralwidget)
        self.name3.setGeometry(QtCore.QRect(190, 320, 200, 20))
        self.name3.setMinimumSize(QtCore.QSize(200, 20))
        self.name3.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name3.setFont(font)
        self.name3.setObjectName("name3")
        self.name4 = QtWidgets.QLineEdit(self.centralwidget)
        self.name4.setGeometry(QtCore.QRect(190, 370, 200, 20))
        self.name4.setMinimumSize(QtCore.QSize(200, 20))
        self.name4.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name4.setFont(font)
        self.name4.setObjectName("name4")
        self.name5 = QtWidgets.QLineEdit(self.centralwidget)
        self.name5.setGeometry(QtCore.QRect(190, 420, 200, 20))
        self.name5.setMinimumSize(QtCore.QSize(200, 20))
        self.name5.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name5.setFont(font)
        self.name5.setObjectName("name5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 220, 200, 30))
        self.label.setMinimumSize(QtCore.QSize(200, 30))
        self.label.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 270, 200, 30))
        self.label_2.setMinimumSize(QtCore.QSize(200, 30))
        self.label_2.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 320, 200, 30))
        self.label_3.setMinimumSize(QtCore.QSize(200, 30))
        self.label_3.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 370, 200, 30))
        self.label_4.setMinimumSize(QtCore.QSize(200, 30))
        self.label_4.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 420, 200, 30))
        self.label_5.setMinimumSize(QtCore.QSize(200, 30))
        self.label_5.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(190, 470, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.error.setFont(font)
        self.error.setText("")
        self.error.setObjectName("error")
        self.errorname1 = QtWidgets.QLabel(self.centralwidget)
        self.errorname1.setGeometry(QtCore.QRect(0, 220, 175, 16))
        self.errorname1.setMinimumSize(QtCore.QSize(175, 16))
        self.errorname1.setMaximumSize(QtCore.QSize(175, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.errorname1.setFont(font)
        self.errorname1.setText("")
        self.errorname1.setObjectName("errorname1")
        self.errorname2 = QtWidgets.QLabel(self.centralwidget)
        self.errorname2.setGeometry(QtCore.QRect(0, 270, 175, 16))
        self.errorname2.setMinimumSize(QtCore.QSize(175, 16))
        self.errorname2.setMaximumSize(QtCore.QSize(175, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.errorname2.setFont(font)
        self.errorname2.setText("")
        self.errorname2.setObjectName("errorname2")
        self.errorname3 = QtWidgets.QLabel(self.centralwidget)
        self.errorname3.setGeometry(QtCore.QRect(0, 320, 175, 16))
        self.errorname3.setMinimumSize(QtCore.QSize(175, 16))
        self.errorname3.setMaximumSize(QtCore.QSize(175, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.errorname3.setFont(font)
        self.errorname3.setText("")
        self.errorname3.setObjectName("errorname3")
        self.errorname4 = QtWidgets.QLabel(self.centralwidget)
        self.errorname4.setGeometry(QtCore.QRect(0, 370, 175, 16))
        self.errorname4.setMinimumSize(QtCore.QSize(175, 16))
        self.errorname4.setMaximumSize(QtCore.QSize(175, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.errorname4.setFont(font)
        self.errorname4.setText("")
        self.errorname4.setObjectName("errorname4")
        self.errorname5 = QtWidgets.QLabel(self.centralwidget)
        self.errorname5.setGeometry(QtCore.QRect(0, 420, 175, 16))
        self.errorname5.setMinimumSize(QtCore.QSize(175, 16))
        self.errorname5.setMaximumSize(QtCore.QSize(175, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.errorname5.setFont(font)
        self.errorname5.setText("")
        self.errorname5.setObjectName("errorname5")
        Stopwatch.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Stopwatch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Stopwatch.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Stopwatch)
        self.statusbar.setObjectName("statusbar")
        Stopwatch.setStatusBar(self.statusbar)

        self.retranslateUi(Stopwatch)
        QtCore.QMetaObject.connectSlotsByName(Stopwatch)

    def retranslateUi(self, Stopwatch):
        _translate = QtCore.QCoreApplication.translate
        Stopwatch.setWindowTitle(_translate("Stopwatch", "MainWindow"))
        self.time.setText(_translate("Stopwatch", "00:00:00:00"))
        self.lap_label.setText(_translate("Stopwatch", "Laps:"))
        self.start_button.setText(_translate("Stopwatch", "Start"))
        self.lap_button.setText(_translate("Stopwatch", "Lap"))
        self.student_label.setText(_translate("Stopwatch", "Student :"))
        self.save_button.setText(_translate("Stopwatch", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Stopwatch = QtWidgets.QMainWindow()
    ui = Ui_Stopwatch()
    ui.setupUi(Stopwatch)
    Stopwatch.show()
    sys.exit(app.exec_())