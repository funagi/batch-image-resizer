# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/workspace/batch-image-resizer/registerwidget.ui'
#
# Created: Thu Apr 26 08:49:56 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_registerDialog(object):
    def setupUi(self, registerDialog):
        registerDialog.setObjectName(_fromUtf8("registerDialog"))
        registerDialog.resize(414, 257)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        registerDialog.setFont(font)
        self.gridLayout_2 = QtGui.QGridLayout(registerDialog)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.mainFrame = QtGui.QFrame(registerDialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.mainFrame.setFont(font)
        self.mainFrame.setStyleSheet(_fromUtf8("#mainFrame{\n"
"    /*background-color: rgb(214, 214, 214);\n"
"    border-image: url(:/images/metal-background.jpg);*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(226, 230, 231, 255), stop:1 rgba(196, 201, 204, 255));\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"#buttonsFrame{\n"
"    margin-bottom: 2px;\n"
"    border: none;\n"
"    padding: 0px;\n"
"    border-image: url(:/images/top-line-bg.png) repeat top;\n"
"}"))
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setLineWidth(5)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tip1Label = QtGui.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.tip1Label.setFont(font)
        self.tip1Label.setObjectName(_fromUtf8("tip1Label"))
        self.gridLayout.addWidget(self.tip1Label, 0, 0, 1, 1)
        self.moneyBackLabel = QtGui.QLabel(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moneyBackLabel.sizePolicy().hasHeightForWidth())
        self.moneyBackLabel.setSizePolicy(sizePolicy)
        self.moneyBackLabel.setMinimumSize(QtCore.QSize(90, 90))
        self.moneyBackLabel.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.moneyBackLabel.setFont(font)
        self.moneyBackLabel.setText(_fromUtf8(""))
        self.moneyBackLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/guarantee30.png")))
        self.moneyBackLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.moneyBackLabel.setMargin(5)
        self.moneyBackLabel.setObjectName(_fromUtf8("moneyBackLabel"))
        self.gridLayout.addWidget(self.moneyBackLabel, 0, 1, 4, 1)
        self.tip5Label = QtGui.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.tip5Label.setFont(font)
        self.tip5Label.setObjectName(_fromUtf8("tip5Label"))
        self.gridLayout.addWidget(self.tip5Label, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.check1Label = QtGui.QLabel(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check1Label.sizePolicy().hasHeightForWidth())
        self.check1Label.setSizePolicy(sizePolicy)
        self.check1Label.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.check1Label.setFont(font)
        self.check1Label.setText(_fromUtf8(""))
        self.check1Label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/check.png")))
        self.check1Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.check1Label.setMargin(5)
        self.check1Label.setObjectName(_fromUtf8("check1Label"))
        self.horizontalLayout_3.addWidget(self.check1Label)
        self.tip3Label = QtGui.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.tip3Label.setFont(font)
        self.tip3Label.setObjectName(_fromUtf8("tip3Label"))
        self.horizontalLayout_3.addWidget(self.tip3Label)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.check2Label = QtGui.QLabel(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check2Label.sizePolicy().hasHeightForWidth())
        self.check2Label.setSizePolicy(sizePolicy)
        self.check2Label.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.check2Label.setFont(font)
        self.check2Label.setText(_fromUtf8(""))
        self.check2Label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/check.png")))
        self.check2Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.check2Label.setMargin(5)
        self.check2Label.setObjectName(_fromUtf8("check2Label"))
        self.horizontalLayout_4.addWidget(self.check2Label)
        self.tip4Label = QtGui.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.tip4Label.setFont(font)
        self.tip4Label.setObjectName(_fromUtf8("tip4Label"))
        self.horizontalLayout_4.addWidget(self.tip4Label)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.buyButton = QtGui.QPushButton(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buyButton.sizePolicy().hasHeightForWidth())
        self.buyButton.setSizePolicy(sizePolicy)
        self.buyButton.setMinimumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.buyButton.setFont(font)
        self.buyButton.setObjectName(_fromUtf8("buyButton"))
        self.horizontalLayout_2.addWidget(self.buyButton)
        spacerItem = QtGui.QSpacerItem(108, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tip2Label = QtGui.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.tip2Label.setFont(font)
        self.tip2Label.setObjectName(_fromUtf8("tip2Label"))
        self.verticalLayout.addWidget(self.tip2Label)
        self.keyLineEdit = QtGui.QLineEdit(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keyLineEdit.sizePolicy().hasHeightForWidth())
        self.keyLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.keyLineEdit.setFont(font)
        self.keyLineEdit.setText(_fromUtf8(""))
        self.keyLineEdit.setObjectName(_fromUtf8("keyLineEdit"))
        self.verticalLayout.addWidget(self.keyLineEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonsFrame = QtGui.QFrame(self.mainFrame)
        self.buttonsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.buttonsFrame.setObjectName(_fromUtf8("buttonsFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(112, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.registerButton = QtGui.QPushButton(self.buttonsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout.addWidget(self.registerButton)
        self.cancelButton = QtGui.QPushButton(self.buttonsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.buttonsFrame)
        self.gridLayout_2.addWidget(self.mainFrame, 0, 0, 1, 1)

        self.retranslateUi(registerDialog)
        QtCore.QMetaObject.connectSlotsByName(registerDialog)

    def retranslateUi(self, registerDialog):
        registerDialog.setWindowTitle(QtGui.QApplication.translate("registerDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.tip1Label.setText(QtGui.QApplication.translate("registerDialog", "Register now to remove any trial limitations.", None, QtGui.QApplication.UnicodeUTF8))
        self.tip5Label.setText(QtGui.QApplication.translate("registerDialog", "Registered user can:", None, QtGui.QApplication.UnicodeUTF8))
        self.tip3Label.setText(QtGui.QApplication.translate("registerDialog", "Get perment, lifetime free software updates.", None, QtGui.QApplication.UnicodeUTF8))
        self.tip4Label.setText(QtGui.QApplication.translate("registerDialog", "Get unlimited email technical support.", None, QtGui.QApplication.UnicodeUTF8))
        self.buyButton.setText(QtGui.QApplication.translate("registerDialog", "Order online now...", None, QtGui.QApplication.UnicodeUTF8))
        self.tip2Label.setText(QtGui.QApplication.translate("registerDialog", "Copy and paste the License key into the field below, then click register.", None, QtGui.QApplication.UnicodeUTF8))
        self.registerButton.setText(QtGui.QApplication.translate("registerDialog", "Register", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("registerDialog", "Later", None, QtGui.QApplication.UnicodeUTF8))

import prog_rc
