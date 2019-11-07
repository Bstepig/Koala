#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QApplication, QFileDialog, QPushButton, QHBoxLayout

import database
from widgets.image import ImageWidget


class CreateProduct(QWidget):
    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.setObjectName("add_product")
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setFixedSize(300, 260)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setObjectName("layout")

        inputs = (
            ('name', 'Название', 'str', ''),
            ('description', 'Описание', 'str', ''),
            ('count', 'Количество', 'int', 0),
            ('purchase_price', 'Закупочная цена', 'float', 0),
            ('selling_price', 'Продажная цена', 'float', 0),
            ('units', 'Еденицы измерения', 'str', 'шт'),
            ('barcode', 'Штрихкод', 'int', 0),
        )

        self.line_edits = {}

        for info in inputs:
            i = info[0]
            title = QtWidgets.QLabel()
            title.setObjectName(f"{i}_title")
            title.setText(info[1])

            type = info[2]
            line_edit = None
            if type == 'str':
                line_edit = QtWidgets.QLineEdit()
                line_edit.setText(info[3])
            elif type == 'int':
                line_edit = QtWidgets.QSpinBox()
                line_edit.setValue(info[3])
            elif type == 'float':
                line_edit = QtWidgets.QDoubleSpinBox()
                line_edit.setValue(info[3])
            line_edit.setObjectName(f"{i}_input")
            self.line_edits[i] = line_edit

            line = QtWidgets.QHBoxLayout()
            line.setObjectName(f"{i}_line")
            line.addWidget(title)
            line.addWidget(line_edit)

            self.layout.addLayout(line)

        self.image_input = QPushButton()
        self.image_input.setObjectName('image_input')
        self.image_input.setText('Выбрать картинку')

        self.image = ImageWidget()

        self.image_layout = QHBoxLayout()
        self.image_layout.addWidget(self.image)
        self.image_layout.addWidget(self.image_input)

        self.layout.addLayout(self.image_layout)

        # self.line_edits['barcode'].setMinimum(000000000000)
        # self.line_edits['barcode'].setMaximum(999999999999)

        self.line_edits['barcode'].setValue(database.get_last_id() + 1)


        self.create = QtWidgets.QPushButton(self)
        self.create.setObjectName("create")
        self.create.setText('Добавить')
        self.layout.addWidget(self.create)
        self.create.clicked.connect(self.addProduct)

        self.setLayout(self.layout)
        QtCore.QMetaObject.connectSlotsByName(self)

    def addProduct(self):
        database.add_product(
            name=self.line_edits['name'].text(),
            description=self.line_edits['description'].text(),
            count=self.line_edits['count'].value(),
            purchase_price=self.line_edits['purchase_price'].value(),
            selling_price=self.line_edits['selling_price'].value(),
            units=self.line_edits['units'].text(),
            barcode=self.line_edits['barcode'].value(),
            image=self.image_path
        )
        self.close()

    def closeEvent(self, event) -> None:
        self.closed.emit()

    @QtCore.pyqtSlot()
    def on_image_input_clicked(self):
        self.image_path = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'Картинка(*.png *.jpg *.jpeg)')[0]
        if self.image_path:
            self.image.load(self.image_path, 30)


def main(*arg):
    database.connect('test')
    app = QApplication(*arg)
    ex = CreateProduct()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
