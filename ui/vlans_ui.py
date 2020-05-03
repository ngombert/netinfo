# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vlans.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(609, 405)
        self.lbl_status = QtWidgets.QLabel(Dialog)
        self.lbl_status.setGeometry(QtCore.QRect(14, 380, 581, 20))
        self.lbl_status.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_status.setObjectName("lbl_status")
        self.tbl_results = QtWidgets.QTableView(Dialog)
        self.tbl_results.setGeometry(QtCore.QRect(5, 91, 601, 281))
        self.tbl_results.setObjectName("tbl_results")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 591, 28))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.txt_hostname = QtWidgets.QLineEdit(self.splitter)
        self.txt_hostname.setObjectName("txt_hostname")
        self.btn_login = QtWidgets.QPushButton(self.splitter)
        self.btn_login.setObjectName("btn_login")
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(10, 50, 591, 28))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.box_interfaces = QtWidgets.QComboBox(self.splitter_2)
        self.box_interfaces.setEnabled(False)
        self.box_interfaces.setObjectName("box_interfaces")
        self.btn_get_vlans = QtWidgets.QPushButton(self.splitter_2)
        self.btn_get_vlans.setEnabled(False)
        self.btn_get_vlans.setObjectName("btn_get_vlans")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Netinfo / VLANs"))
        self.lbl_status.setText(_translate("Dialog", "not connected"))
        self.label.setText(_translate("Dialog", "Switch IP/hostname :"))
        self.btn_login.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Select Interface :"))
        self.btn_get_vlans.setText(_translate("Dialog", "Get VLANs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
