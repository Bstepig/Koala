#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Union

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel


class ImageWidget(QLabel):
    def __init__(self, data: Union[bytes, str] = '', size: int = 40, parent=None):
        super().__init__(parent=parent)

        self.data = data
        self.size = size

        self.load()

    def load(self, data='', size=0):
        data = data if data else self.data
        size = size if size else self.size
        _image = None
        if type(data) == str:
            _image = QtGui.QImage(data)
        else:
            _image = QtGui.QImage.fromData(data)
        _image.convertToFormat(QtGui.QImage.Format_ARGB32)

        img_size = min(_image.width(), _image.height())
        if img_size == 0:

            out_img = QtGui.QImage(size, size, QtGui.QImage.Format_ARGB32)
            out_img.fill(QtCore.Qt.transparent)
            painter = QtGui.QPainter(out_img)  # Paint the output image
            painter.setPen(QtCore.Qt.NoPen)  # Don't draw an outline
            painter.setRenderHint(QtGui.QPainter.Antialiasing, True)  # Use AA
            brush = QtGui.QBrush(QColor('#E6E6E6'))  # Create grey brush
            painter.setBrush(brush)  # Use the image texture brush
            painter.drawEllipse(0, 0, size, size)  # Actually draw the circle
            painter.end()

        else:
            rect = QtCore.QRect(
                int((_image.width() - img_size) / 2),
                int((_image.height() - img_size) / 2),
                img_size,
                img_size,
            )
            _image = _image.copy(rect)

            out_img = QtGui.QImage(img_size, img_size, QtGui.QImage.Format_ARGB32)
            out_img.fill(QtCore.Qt.transparent)

            painter = QtGui.QPainter(out_img)  # Paint the output image
            painter.setPen(QtCore.Qt.NoPen)  # Don't draw an outline
            painter.setRenderHint(QtGui.QPainter.Antialiasing, True)  # Use AA

            brush = QtGui.QBrush(QColor('#E6E6E6'))  # Create grey brush
            painter.setBrush(brush)  # Use the image texture brush
            painter.drawEllipse(0, 0, img_size, img_size)  # Actually draw the circle
            brush = QtGui.QBrush(_image)  # Create texture brush
            painter.setBrush(brush)  # Use the image texture brush
            painter.drawEllipse(0, 0, img_size, img_size)  # Actually draw the circle

            painter.end()

        pixmap = QtGui.QPixmap.fromImage(out_img).scaled(size, size, QtCore.Qt.KeepAspectRatio,
                                                         QtCore.Qt.SmoothTransformation)

        self.setPixmap(pixmap)
