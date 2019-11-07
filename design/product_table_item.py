from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout

from models import Product
from widgets.image import ImageWidget


class ProductTableItemWidget(QFrame):
    def __init__(self, product: Product, parent=None):
        super().__init__(parent=parent)

        self.product = product

        self.initUI()

    def initUI(self):
        image = ImageWidget(self.product.image)
        title = QLabel(self)
        price = QLabel(self)
        count = QLabel(self)
        total = QLabel(self)

        image.setObjectName('image')
        title.setObjectName('title')
        price.setObjectName('price')
        count.setObjectName('count')
        total.setObjectName('total')

        line = QHBoxLayout()
        line.setContentsMargins(0, 15, 0, 15)
        line.setSpacing(0)

        title.setText(self.product.name)
        price.setText(self.product.selling_price)
        count.setText(self.product.count)
        total.setText(f'{self.product._count * self.product._selling_price:.2f} руб')

        title_layout = QHBoxLayout()
        title_layout.addWidget(image)
        title_layout.addWidget(title, 1)
        line.addLayout(title_layout, 2)
        line.addWidget(price, 1)
        line.addWidget(count, 1)
        line.addWidget(total, 1)

        self.setLayout(line)
