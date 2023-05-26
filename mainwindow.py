# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 656)
        MainWindow.setStyleSheet("background-color: #262626;\n"
"background-image: linear-gradient(to bottom right, #1a1a1a, #333333);\n"
"color: #fff;\n"
"font-family: \'Helvetica Neue\', sans-serif;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBoxPath = QtWidgets.QComboBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPath.sizePolicy().hasHeightForWidth())
        self.comboBoxPath.setSizePolicy(sizePolicy)
        self.comboBoxPath.setMinimumSize(QtCore.QSize(160, 40))
        self.comboBoxPath.setMaximumSize(QtCore.QSize(160, 40))
        self.comboBoxPath.setStyleSheet("QComboBox{\n"
"    font-size: 14px;\n"
"}")
        self.comboBoxPath.setObjectName("comboBoxPath")
        self.comboBoxPath.addItem("")
        self.comboBoxPath.addItem("")
        self.comboBoxPath.addItem("")
        self.verticalLayout.addWidget(self.comboBoxPath)
        self.comboBoxMazes = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBoxMazes.setMinimumSize(QtCore.QSize(160, 40))
        self.comboBoxMazes.setMaximumSize(QtCore.QSize(160, 40))
        self.comboBoxMazes.setStyleSheet("QComboBox{\n"
"    font-size: 14px;\n"
"}")
        self.comboBoxMazes.setObjectName("comboBoxMazes")
        self.comboBoxMazes.addItem("")
        self.comboBoxMazes.addItem("")
        self.comboBoxMazes.addItem("")
        self.verticalLayout.addWidget(self.comboBoxMazes)
        self.checkBoxVisualize = QtWidgets.QCheckBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxVisualize.sizePolicy().hasHeightForWidth())
        self.checkBoxVisualize.setSizePolicy(sizePolicy)
        self.checkBoxVisualize.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBoxVisualize.setMaximumSize(QtCore.QSize(160, 40))
        self.checkBoxVisualize.setObjectName("checkBoxVisualize")
        self.verticalLayout.addWidget(self.checkBoxVisualize)
        self.labelDelay = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelDelay.setMaximumSize(QtCore.QSize(160, 16777215))
        self.labelDelay.setObjectName("labelDelay")
        self.verticalLayout.addWidget(self.labelDelay)
        self.spinBoxDelayms = QtWidgets.QSpinBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxDelayms.sizePolicy().hasHeightForWidth())
        self.spinBoxDelayms.setSizePolicy(sizePolicy)
        self.spinBoxDelayms.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBoxDelayms.setMaximumSize(QtCore.QSize(160, 40))
        self.spinBoxDelayms.setFrame(True)
        self.spinBoxDelayms.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.spinBoxDelayms.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBoxDelayms.setMinimum(1)
        self.spinBoxDelayms.setMaximum(5000)
        self.spinBoxDelayms.setSingleStep(10)
        self.spinBoxDelayms.setProperty("value", 10)
        self.spinBoxDelayms.setObjectName("spinBoxDelayms")
        self.verticalLayout.addWidget(self.spinBoxDelayms)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBoxPath, self.comboBoxMazes)
        MainWindow.setTabOrder(self.comboBoxMazes, self.checkBoxVisualize)
        MainWindow.setTabOrder(self.checkBoxVisualize, self.spinBoxDelayms)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBoxPath.setItemText(0, _translate("MainWindow", "BFS"))
        self.comboBoxPath.setItemText(1, _translate("MainWindow", "DFS"))
        self.comboBoxPath.setItemText(2, _translate("MainWindow", "A* algorithm"))
        self.comboBoxMazes.setItemText(0, _translate("MainWindow", "Randomized Prim\'s Algorithm"))
        self.comboBoxMazes.setItemText(1, _translate("MainWindow", "Recursive Backtracking"))
        self.comboBoxMazes.setItemText(2, _translate("MainWindow", "Kruskal\'s Algorithm"))
        self.checkBoxVisualize.setText(_translate("MainWindow", "Visualize"))
        self.labelDelay.setText(_translate("MainWindow", "Visualization delay(ms)"))
