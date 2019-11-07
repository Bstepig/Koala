#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QLabel, QHBoxLayout, QLineEdit, QVBoxLayout, QFrame, QScrollArea, QPushButton, \
    QWidget, QApplication

from utils import get_styles, load_fonts


class SidebarWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.plus = QPushButton()
        self.search = QLineEdit()
        self.products_layout = QVBoxLayout()
        self.header = QHBoxLayout()
        self.title = QLabel()
        self.layout = QVBoxLayout()
        self.products = QWidget()
        self.scroll = QScrollArea()

        self.initUI()

    def initUI(self):
        load_fonts()
        self.setStyleSheet(get_styles('style'))
        self.setStyleSheet(get_styles('sidebar'))

        self.title.setObjectName('sidebar_title')
        self.title.setText('Товары')

        self.plus.setObjectName('plus')
        self.plus.setText('+')
        # self.plus.setFixedWidth(20)

        self.header.setContentsMargins(0, 0, 0, 0)
        self.header.setSpacing(0)
        self.header.addWidget(self.title)
        self.header.addStretch(1)
        self.header.addWidget(self.plus, 0)
        self.header.setObjectName('header')

        self.search.setObjectName('search')
        self.search.setPlaceholderText('Поиск...')

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.layout.addLayout(self.header)
        self.layout.addWidget(self.search)

        self.products_layout.setContentsMargins(0, 0, 0, 0)
        self.products_layout.setSpacing(0)

        self.products.setLayout(self.products_layout)

        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.products)
        self.layout.addWidget(self.scroll)

        self.products_layout.addStretch(1)

        self.setFixedWidth(300)
        self.setLayout(self.layout)
        self.setObjectName('sidebar')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SidebarWidget()
    ex.show()
    sys.exit(app.exec_())
