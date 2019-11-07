#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QPushButton, QDialog, QLabel, \
    QLineEdit

import database
from utils import get_styles


class LoginWidget(QDialog):
    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.title = QLabel()
        self.input = QLineEdit()
        self.accept_btn = QPushButton()
        self.layout = QVBoxLayout(self)

        self.initUI()

    def initUI(self):

        self.title.setText('Введите имя БД')
        self.input.setPlaceholderText('Название...')
        self.accept_btn.setText('Принять')

        self.title.setObjectName('login_title')
        self.input.setObjectName('login_input')
        self.accept_btn.setObjectName('login_accept')

        self.layout.setContentsMargins(40, 40, 40, 40)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.accept_btn)

        self.setObjectName("add_product")
        QtCore.QMetaObject.connectSlotsByName(self)


        self.setStyleSheet(get_styles('style'))
        self.setStyleSheet(get_styles('create-product'))

    def on_login_accept_clicked(self):
        database.init(self.input.text())
        self.close()

    def closeEvent(self, event) -> None:
        self.closed.emit()


def main(*arg):
    database.connect('test')
    app = QApplication(*arg)
    ex = LoginWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
