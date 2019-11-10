from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout

from design import PaymentWidget
from design.navbarwidget import NavbarWidget
from design.product_table import ProductTableWidget
from design.sidebar import SidebarWidget
from forms.login import LoginWidget
from utils import get_styles
from forms.createProduct import CreateProduct


class UI_Main(QFrame):

    resized = QtCore.pyqtSignal()

    def __init__(self):
        self.add_product_form = CreateProduct()
        self.login_form = LoginWidget()
        super().__init__()
        self.layout = QVBoxLayout()
        self.sidebar = SidebarWidget()
        self.table = ProductTableWidget(self)
        self.side_layout = QVBoxLayout()
        self.side = QFrame()

        self.navbar = NavbarWidget()
        self.payment = PaymentWidget()

        self.initUI()

    def initUI(self):

        self.setWindowTitle('Koala')
        self.setObjectName('mainWindow')

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.layout.addWidget(self.navbar)

        content = QHBoxLayout()
        content.setContentsMargins(0, 0, 0, 0)
        content.setSpacing(0)

        self.sidebar.setObjectName('sidebar')

        self.setLayout(self.layout)

        self.side_layout.setContentsMargins(0, 0, 0, 0)
        self.side_layout.setSpacing(0)
        self.side_layout.addWidget(self.table, 1)
        self.side_layout.addWidget(self.payment)

        self.side.setLayout(self.side_layout)
        self.side.setObjectName('content')

        content.addWidget(self.sidebar, 1)
        content.addWidget(self.side, 2)

        self.layout.addLayout(content)

        self.setLayout(self.layout)
        self.setMinimumHeight(300)
        self.setMinimumWidth(600)
        self.resize(800, 400)
        self.show()

        for i in range(self.sidebar.products_layout.count() - 1):
            self.sidebar.products_layout.itemAt(i).widget().clicked.connect(self.add2cart)

        self.add_product_form.closed.connect(self.close_add_product_form)
        self.login_form.closed.connect(self.close_login_form)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setStyleSheet(get_styles('style') + get_styles('modal-container'))

    def add2cart(self):
        pass

    def update_list(self):
        pass

    def close_add_product_form(self):
        pass

    def close_login_form(self):
        pass
