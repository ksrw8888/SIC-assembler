from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setFont(QtGui.QFont("Roman times", 15))
        self.textEdit.setGeometry(QtCore.QRect(400, 30, 200, 30))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 25, 250, 40))
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont("Roman times", 16))
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 150, 900, 500))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFontPointSize(16)
        self.input_file_name = QtWidgets.QPushButton(self.centralwidget)
        self.input_file_name.setGeometry(QtCore.QRect(650, 30, 80, 30))
        self.input_file_name.setObjectName("input_file_name")
        self.op_table = QtWidgets.QPushButton(self.centralwidget)
        self.op_table.setGeometry(QtCore.QRect(130, 80, 120, 50))
        self.op_table.setObjectName("op_table")
        self.symbol_table = QtWidgets.QPushButton(self.centralwidget)
        self.symbol_table.setGeometry(QtCore.QRect(300, 80, 120, 50))
        self.symbol_table.setObjectName("symbol_table")
        self.object_code = QtWidgets.QPushButton(self.centralwidget)
        self.object_code.setGeometry(QtCore.QRect(450, 80, 120, 50))
        self.object_code.setObjectName("object_code")
        self.object_program_format = QtWidgets.QPushButton(self.centralwidget)
        self.object_program_format.setGeometry(QtCore.QRect(600, 80, 200, 50))
        self.object_program_format.setObjectName("object_program_format")

        language = ['English', '????????????', '?????????']
        self.language = QtWidgets.QComboBox(self.centralwidget)
        self.language.setGeometry(QtCore.QRect(20, 20, 120, 50))
        self.language.setObjectName("language")
        self.language.setFont(QtGui.QFont("Roman times", 15))
        self.language.addItems(language)
        self.language.activated[str].connect(self.change_language)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.set_transparent()
        self.set_qss()
        MainWindow.setStyleSheet('#MainWindow {background : #BBFFEE}')
        self.retranslateUi(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIC Assembler"))
        self.default_language()

    def set_transparent(self):
        self.op_table.setFlat(True)
        self.symbol_table.setFlat(True)
        self.object_code.setFlat(True)
        self.object_program_format.setFlat(True)
        self.input_file_name.setFlat(True)

    def set_qss(self):
        self.label.setStyleSheet('QLabel {color : blue}'
                                 'QLabel {qproperty-alignment : AlignCenter}')

        self.textBrowser.setStyleSheet('QTextBrowser {background : #00BFFF}')

        self.op_table.setStyleSheet('QPushButton:hover {color: red}')
        self.symbol_table.setStyleSheet('QPushButton:hover {color: #FF8800}')
        self.object_code.setStyleSheet('QPushButton:hover {color: #FF00FF}')
        self.object_program_format.setStyleSheet('QPushButton:hover {color: #808000}')
        self.input_file_name.setStyleSheet('QPushButton:hover {color: #EE82EE}')

        self.language.setStyleSheet('QComboBox {color : purple}'
                                    'QComboBox {background : yellow}'
                                    'QComboBox:!editable {background : white}'
                                    'QAbstractItemView {background : yellow}'
                                    'QAbstractItemView {color : purple}')

    def default_language(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Input file name"))
        self.input_file_name.setText(_translate("MainWindow", "Confirm"))
        self.op_table.setText(_translate("MainWindow", "OP Table"))
        self.symbol_table.setText(_translate("MainWindow", "Symbol Table"))
        self.object_code.setText(_translate("MainWindow", "Object Code"))
        self.object_program_format.setText(_translate("MainWindow", "Object Program Format"))

    def change_language(self):
        _translate = QtCore.QCoreApplication.translate
        if self.language.currentText() == '????????????':
            self.label.setText(_translate("MainWindow", "??????????????????"))
            self.input_file_name.setText(_translate("MainWindow", "??????"))
            self.op_table.setText(_translate("MainWindow", "????????????"))
            self.symbol_table.setText(_translate("MainWindow", "?????????"))
            self.object_code.setText(_translate("MainWindow", "?????????"))
            self.object_program_format.setText(_translate("MainWindow", "??????????????????"))

        if self.language.currentText() == 'English':
            self.default_language()

        if self.language.currentText() == '?????????':
            self.label.setText(_translate("MainWindow", "??????????????????????????????"))
            self.input_file_name.setText(_translate("MainWindow", "????????????"))
            self.op_table.setText(_translate("MainWindow", "???????????????"))
            self.symbol_table.setText(_translate("MainWindow", "????????????????????????"))
            self.object_code.setText(_translate("MainWindow", "???????????????????????????"))
            self.object_program_format.setText(_translate("MainWindow", "???????????????????????????????????????"))
