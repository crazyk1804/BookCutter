# Form implementation generated from reading ui file 'book_cutter_app\gui\ui\ui_main_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 657)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.tbox_path_book = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tbox_path_book.setText("")
        self.tbox_path_book.setObjectName("tbox_path_book")
        self.horizontalLayout.addWidget(self.tbox_path_book)
        self.btn_find_book = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_find_book.setObjectName("btn_find_book")
        self.horizontalLayout.addWidget(self.btn_find_book)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_canvas = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_canvas.sizePolicy().hasHeightForWidth())
        self.lbl_canvas.setSizePolicy(sizePolicy)
        self.lbl_canvas.setStyleSheet("background-color: white;")
        self.lbl_canvas.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_canvas.setObjectName("lbl_canvas")
        self.verticalLayout_3.addWidget(self.lbl_canvas)
        self.horizontalSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.horizontalSlider)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.spn_offset_up = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spn_offset_up.setObjectName("spn_offset_up")
        self.horizontalLayout_3.addWidget(self.spn_offset_up)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.spn_offset_bottom = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spn_offset_bottom.setObjectName("spn_offset_bottom")
        self.horizontalLayout_4.addWidget(self.spn_offset_bottom)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.spn_offset_left = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spn_offset_left.setObjectName("spn_offset_left")
        self.horizontalLayout_5.addWidget(self.spn_offset_left)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.spn_offset_right = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spn_offset_right.setObjectName("spn_offset_right")
        self.horizontalLayout_6.addWidget(self.spn_offset_right)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.spn_offset_odd_top = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spn_offset_odd_top.setObjectName("spn_offset_odd_top")
        self.horizontalLayout_7.addWidget(self.spn_offset_odd_top)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.spn_offset_odd_left = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spn_offset_odd_left.setObjectName("spn_offset_odd_left")
        self.horizontalLayout_8.addWidget(self.spn_offset_odd_left)
        self.horizontalLayout_8.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_prev_page = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_prev_page.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_prev_page.setObjectName("btn_prev_page")
        self.horizontalLayout_9.addWidget(self.btn_prev_page)
        self.btn_next_page = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_next_page.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_next_page.setObjectName("btn_next_page")
        self.horizontalLayout_9.addWidget(self.btn_next_page)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btn_do_work = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_do_work.setObjectName("btn_do_work")
        self.verticalLayout_2.addWidget(self.btn_do_work)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.bar_progress = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.bar_progress.setProperty("value", 24)
        self.bar_progress.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bar_progress.setObjectName("bar_progress")
        self.verticalLayout.addWidget(self.bar_progress)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "경로"))
        self.btn_find_book.setText(_translate("MainWindow", "찾아보기"))
        self.lbl_canvas.setText(_translate("MainWindow", "이미지가 여기에 나옵니다"))
        self.label_9.setText(_translate("MainWindow", "절단 사이즈"))
        self.label_3.setText(_translate("MainWindow", "상단"))
        self.label_4.setText(_translate("MainWindow", "하단"))
        self.label_5.setText(_translate("MainWindow", "좌단"))
        self.label_6.setText(_translate("MainWindow", "우단"))
        self.label_10.setText(_translate("MainWindow", "홀수페이지 조정"))
        self.label_7.setText(_translate("MainWindow", "상단"))
        self.label_8.setText(_translate("MainWindow", "좌단"))
        self.label_11.setText(_translate("MainWindow", "페이지 조정"))
        self.btn_prev_page.setText(_translate("MainWindow", "◀"))
        self.btn_next_page.setText(_translate("MainWindow", "▶"))
        self.btn_do_work.setText(_translate("MainWindow", "시작"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())