#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from typing import List

from PyQt5 import QtCore
from PyQt5.QtGui import QResizeEvent, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QVBoxLayout, QHBoxLayout, \
    QGraphicsDropShadowEffect

import database
from design import ProductWidget, ProductTableItemWidget, UI_Main
from models import Product
from utils import load_fonts


class Main(UI_Main):

    cart: List[Product] = []
    resized = QtCore.pyqtSignal()
    total_price: int = 0

    def __init__(self):
        super().__init__()
        self.modal_container = QFrame(self)
        self.modal_container.setObjectName('modal_container')
        self.resized.connect(self.on_mainWindow_resized)
        self.open_modal(self.login_form)

    def resizeEvent(self, event):
        self.resized.emit()

    def sync_cart(self):
        self.clear_cart()
        layout = self.table.products_layout
        for i in database.get_cart():
            # self.update_total_price(i.selling_price * i.count)
            layout.insertWidget(layout.count() - 1, ProductTableItemWidget(i))

    def clear_cart(self):
        self.clear_layout(self.table.products_layout, 1)

    def add2cart(self):
        product = self.sender().product
        database.add2cart(product.id)
        layout = self.table.products_layout
        product.count = 1
        # self.update_total_price(product.selling_price * product.count)
        layout.insertWidget(0, ProductTableItemWidget(product))

    def update_total_price(self, add: int):
        self.total_price += add

    def on_mainWindow_resized(self):
        if self.modal_container:
            self.modal_container.setFixedSize(self.size())

    @QtCore.pyqtSlot()
    def on_plus_clicked(self):
        self.open_modal(self.add_product_form)
        # self.open_add_product()

    @QtCore.pyqtSlot(str)
    def on_search_textEdited(self, filter_str: str = ''):
        self.update_list(filter_str)

    @QtCore.pyqtSlot(int)
    def on_to_pay_value_valueChanged(self, value: int = 0):
        self.payment.surrender_value.setText(f'{100000 - value}')

    def open_add_product(self):
        self.add_product_form.show()

    def update_list(self, filter_str: str = ''):
        self.clear_list()
        for p in database.get_products(filter_str):
            product = ProductWidget(p)
            product.clicked.connect(self.add2cart)
            self.sidebar.products_layout.insertWidget(self.sidebar.products_layout.count() - 1, product)

    def clear_list(self):
        self.clear_layout(self.sidebar.products_layout, 1)

    @staticmethod
    def clear_layout(layout, offset=0):
        for i in range(layout.count() - offset):
            layout.itemAt(i).widget().close()

    def open_modal(self, modal: QWidget):
        self.modal_container.setFixedSize(self.size())
        self.modal_container.show()
        self.modal_container.setObjectName("modal_container")
        v = QVBoxLayout()
        h = QHBoxLayout()
        v.addStretch(1)
        h.addStretch(1)

        v.addLayout(h)
        h.addWidget(modal, 1)

        v.addStretch(1)
        h.addStretch(1)

        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setBlurRadius(50)
        shadow.setOffset(0, 10)

        modal.setGraphicsEffect(shadow)

        self.modal_container.setLayout(v)
        modal.setObjectName("modal")

    def close_modal(self):
        self.modal_container.hide()

    def close_add_product_form(self):
        self.close_modal()
        self.update_list()

    def close_login_form(self):
        self.close_modal()
        self.navbar.shop.setText(database.dbname)
        self.update_data()

    def update_data(self):
        self.update_list()
        self.sync_cart()


def main(*arg):
    app = QApplication(*arg)
    load_fonts()
    ex = Main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
