from PyQt5.QtWidgets import QHBoxLayout, QLabel, QFrame

columns = (
    ("Товар", 2),
    ("Цена", 1),
    ("Количество", 1),
    ("Сумма", 1)
)


class ProductTableHeaderWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.initUI()

    def initUI(self):

        header = QHBoxLayout()

        for c in columns:
            label = QLabel()
            label.setText(c[0])
            # label.setStyleSheet("""
            #     font-size: 14px;
            #     color: #474747;
            #     text-align: center;
            # """)
            header.addWidget(label, c[1])

        self.setLayout(header)
