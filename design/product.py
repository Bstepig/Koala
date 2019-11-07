#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout, QVBoxLayout

from models.product import Product
from widgets.image import ImageWidget


class ProductWidget(QFrame):
    clicked = QtCore.pyqtSignal()

    def __init__(self, product: Product, parent=None):
        super().__init__(parent=parent)

        self.product = product

        self.name = QVBoxLayout()
        self.line = QHBoxLayout()
        self.title = QLabel()
        self.image = ImageWidget(self.product.image, 40)
        self.price = QLabel()
        self.count = QLabel()

        self.initUI()

    def initUI(self):
        self.setObjectName('product')
        self.setFixedHeight(72)

        self.line.setContentsMargins(0, 15, 0, 15)

        self.title.setObjectName('product_title')
        self.price.setObjectName('product_price')
        self.count.setObjectName('product_count')

        self.title.setText(self.product.name)
        self.price.setText(self.product.selling_price)
        self.count.setText(self.product.count)

        self.name.addWidget(self.title)
        self.name.addWidget(self.count)

        self.line.addSpacing(8)
        self.line.addWidget(self.image)
        self.line.addLayout(self.name)
        self.line.addStretch(1)
        self.line.addWidget(self.price)

        self.setLayout(self.line)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.clicked.emit()
