from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel, QHBoxLayout, QLineEdit, QVBoxLayout, QSpinBox
from PyQt5.QtCore import Qt

from utils import get_styles


class PaymentWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.to_pay_title = QLabel()
        self.surrender_title = QLabel()
        self.to_pay_value = QSpinBox()
        self.surrender_value = QLabel()
        self.to_pay_currency = QLabel()
        self.surrender_currency = QLabel()
        self.total_currency = QLabel()

        self.total_container = QFrame()
        self.total_title = QLabel()
        self.total_value = QLabel()

        self.pay = QPushButton()

        self.initUI()

    def initUI(self):

        self.setStyleSheet(get_styles('style') + get_styles('payment'))
        self.setObjectName('payment')
        self.to_pay_title.setObjectName('to_pay_title')
        self.surrender_title.setObjectName('surrender_title')
        self.to_pay_value.setObjectName('to_pay_value')
        self.surrender_value.setObjectName('surrender_value')
        self.to_pay_currency.setObjectName('to_pay_currency')
        self.surrender_currency.setObjectName('surrender_currency')
        self.total_title.setObjectName('total_title')
        self.total_value.setObjectName('total_value')
        self.total_currency.setObjectName('total_currency')
        self.pay.setObjectName('pay_btn')

        self.to_pay_value.setMaximum(2147483647)

        self.to_pay_title.setText('К оплате')
        self.surrender_title.setText('Сдача')
        self.total_title.setText('Итого')
        self.to_pay_currency.setText('руб')
        self.surrender_currency.setText('руб')
        self.total_currency.setText('руб')

        self.pay.setText('Оплатить')

        layout = QVBoxLayout()
        to_pay_layout = QHBoxLayout()
        surrender_layout = QHBoxLayout()
        total_layout = QHBoxLayout()

        to_pay_layout.addWidget(self.to_pay_title, 1)
        to_pay_layout.addWidget(self.to_pay_value, 1)
        to_pay_layout.addWidget(self.to_pay_currency)

        self.to_pay_value.setAlignment(Qt.AlignRight)

        surrender_layout.addWidget(self.surrender_title, 1)
        surrender_layout.addWidget(self.surrender_value, 1)
        surrender_layout.addWidget(self.surrender_currency)

        self.surrender_value.setAlignment(Qt.AlignRight)

        total_layout.addWidget(self.total_title, 1)
        total_layout.addWidget(self.total_value, 1)
        total_layout.addWidget(self.total_currency)

        self.total_value.setAlignment(Qt.AlignRight)
        # self.pay.setAlignment(Qt.AlignRight)

        layout.addLayout(to_pay_layout)
        layout.addLayout(surrender_layout)
        layout.addLayout(total_layout)
        pay_layout = QHBoxLayout()
        pay_layout.addStretch(2)
        pay_layout.addWidget(self.pay, 1)
        self.pay.setMinimumWidth(130)
        layout.addLayout(pay_layout)

        self.setLayout(layout)
