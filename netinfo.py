#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import ui.vlans_ui as gui


class DialogVlans(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = gui.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        # un clic sur le bouton appellera la méthode 'action_bouton'
        self.ui.btn_login.clicked.connect(self.action_bouton)

    def action_bouton(self):
        print('Appui login.')
        self.ui.lbl_status.setText(self.ui.txt_hostname.text())

    def on_item_changed(self):
        print(self.ui.tbl_results.currentItem().text())


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = DialogVlans()
    window.show()
    sys.exit(app.exec_())