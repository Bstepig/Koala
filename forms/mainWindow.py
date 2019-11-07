#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from typing import List

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

import database
from design.product import ProductWidget
from design.product_table import ProductTableWidget
from design.product_table_item import ProductTableItemWidget
from design.ui_main import UI_Main
from models.product import Product
from utils import load_fonts

cart: List[Product] = []


class Main(UI_Main):

    def __init__(self):
        super().__init__()
        self.update_list()
        self.sync_cart()

    def sync_cart(self):
        self.clear_cart()
        layout = self.table.products_layout
        for i in database.get_cart():
            layout.insertWidget(layout.count() - 1, ProductTableItemWidget(i))

    def clear_cart(self):
        self.clear_layout(self.table.products_layout, 1)

    def add2cart(self):
        product = self.sender().product
        database.add2cart(product.id)
        layout = self.table.products_layout
        layout.insertWidget(layout.count() - 1, ProductTableItemWidget(product))
        self.sync_cart()

    @QtCore.pyqtSlot()
    def on_plus_clicked(self):
        self.open_add_product()

    @QtCore.pyqtSlot(str)
    def on_search_textEdited(self, filter_str: str = ''):
        self.update_list(filter_str)

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


def main(*arg):
    database.connect('test')
    app = QApplication(*arg)
    load_fonts()
    ex = Main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
