from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout

from design.navbar import Navbar
from design.product_table import ProductTableWidget
from design.sidebar import SidebarWidget
from utils import get_styles
from forms.createProduct import CreateProduct


class UI_Main(QFrame):

    def __init__(self):
        self.add_product_form = CreateProduct()
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setStyleSheet(get_styles('style'))

        # QFontDatabase().addApplicationFont(f'resources/fonts/Montserrat-Medium.ttf')

        navbar = Navbar()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(navbar)

        content = QHBoxLayout()
        content.setContentsMargins(0, 0, 0, 0)
        content.setSpacing(0)

        self.sidebar = SidebarWidget()
        self.sidebar.setObjectName('sidebar')


        self.setLayout(layout)

        self.table = ProductTableWidget(self)
        self.side_layout = QVBoxLayout()
        self.side_layout.setContentsMargins(0, 0, 0, 0)
        self.side_layout.setSpacing(0)
        self.side_layout.addWidget(self.table, 1)

        self.side = QFrame()
        self.side.setLayout(self.side_layout)
        self.side.setObjectName('content')

        content.addWidget(self.sidebar, 1)
        content.addWidget(self.side, 2)

        layout.addLayout(content)

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setLayout(layout)
        self.setMinimumHeight(300)
        self.setMinimumWidth(600)
        self.resize(800, 400)
        self.setWindowTitle('Koala')
        self.setObjectName('mainWindow')
        self.show()
        for i in range(self.sidebar.products_layout.count() - 1):
            self.sidebar.products_layout.itemAt(i).widget().clicked.connect(self.add2cart)

        self.add_product_form.closed.connect(self.update_list)
        QtCore.QMetaObject.connectSlotsByName(self)
