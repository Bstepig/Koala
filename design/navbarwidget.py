from PyQt5.QtWidgets import QFrame, QPushButton, QLabel, QHBoxLayout

from utils import get_styles


class NavbarWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.layout = QHBoxLayout()
        self.products_btn = QPushButton()
        self.history_btn = QPushButton()
        self.receipt_btn = QPushButton()
        self.settings_btn = QPushButton()
        self.user = QLabel()
        self.shop = QLabel()
        self.initUI()

    def initUI(self):
        self.setStyleSheet(get_styles('style'))
        self.setStyleSheet(get_styles('navbar'))

        self.setObjectName('navbar')

        self.layout.setSpacing(22)

        self.products_btn.setText("")
        self.layout.addWidget(self.products_btn)
        self.products_btn.setProperty('class', 'navbar_btn')

        self.history_btn.setText("")
        self.layout.addWidget(self.history_btn)
        self.history_btn.setProperty('class', 'navbar_btn')

        self.receipt_btn.setText("")
        self.layout.addWidget(self.receipt_btn)
        self.receipt_btn.setProperty('class', 'navbar_btn')

        self.settings_btn.setText("")
        self.layout.addWidget(self.settings_btn)
        self.settings_btn.setProperty('class', 'navbar_btn')

        self.layout.addStretch(1)

        self.user.setText("CASHIER NAME")
        self.user.setObjectName('user')
        self.layout.addWidget(self.user)

        self.layout.addStretch(1)

        self.shop.setObjectName('shop')
        self.shop.setText("SHOP NAME")
        self.layout.addWidget(self.shop)

        self.setLayout(self.layout)
