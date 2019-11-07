from PyQt5.QtWidgets import QVBoxLayout, QWidget, QFrame, QHBoxLayout, QScrollArea, QLabel

from design.product_table_header import ProductTableHeaderWidget
from design.product_table_item import ProductTableItemWidget
from models import Product
from utils import get_styles
from widgets.image import ImageWidget


class ProductTableWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 13, 10, 0)
        self.layout.setSpacing(0)

        self.layout.addWidget(ProductTableHeaderWidget())

        self.products_layout = QVBoxLayout()

        table = QWidget()
        # table.setStyleSheet('border: none; background: transparent')
        table.setLayout(self.products_layout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(table)
        # scroll.setStyleSheet('border: none; background: transparent')

        self.layout.addWidget(scroll, 1)
        table.setLayout(self.products_layout)
        self.products_layout.addStretch(1)

        self.setLayout(self.layout)
        self.setStyleSheet(get_styles('style'))
        self.setStyleSheet(get_styles('product-table'))

    # def update_cart(self):
    #     for p in cart:
    #         self.layout.addWidget(ProductTableItemWidget(p))

    def add2cart(self, product: Product):
        self.products_layout.insertWidget(self.products_layout.count() - 1, ProductTableItemWidget(product))
