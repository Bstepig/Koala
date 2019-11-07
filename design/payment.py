from PyQt5.QtWidgets import QFrame, QPushButton, QLabel, QHBoxLayout, QLineEdit, QVBoxLayout


class Navbar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.to_pay_title = QLabel()
        self.surrender_title = QLabel()
        self.to_pay_value = QLineEdit()
        self.surrender_value = QLabel()
        self.to_pay_currency = QLabel()
        self.surrender_currency = QLabel()

        self.total_title = QLabel()
        self.total_value = QLabel()
        self.pay = QLabel()

        self.initUI()

    def initUI(self):
        self.setObjectName('payment')
        self.to_pay_title.setObjectName('to_pay_title')
        self.surrender_title.setObjectName('surrender_title')
        self.to_pay_value.setObjectName('to_pay_value')
        self.surrender_value.setObjectName('surrender_value')
        self.to_pay_currency.setObjectName('to_pay_currency')
        self.surrender_currency.setObjectName('surrender_currency')
        self.total_title.setObjectName('total_title')
        self.total_value.setObjectName('total_value')

        self.to_pay_title.setText('К оплате')
        self.surrender_title.setText('Сдача')
        self.total_title.setText('Итого')
        self.to_pay_currency.setText('руб')
        self.surrender_currency.setText('руб')

        self.pay.setText('К оплате')

        layout = QHBoxLayout()
        to_pay_layout = QHBoxLayout()
        surrender_layout = QHBoxLayout()
        total_layout = QVBoxLayout()

        to_pay_layout.addWidget(self.to_pay_title)
        to_pay_layout.addWidget(self.to_pay_value)
        to_pay_layout.addWidget(self.to_pay_currency)

        surrender_layout.addWidget(self.surrender_title)
        surrender_layout.addWidget(self.surrender_value)
        surrender_layout.addWidget(self.surrender_currency)

        total_layout.addWidget(self.total_title)
        total_layout.addWidget(self.total_value)

        layout.addLayout()