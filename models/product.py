#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Product:
    def __init__(self,
                 _id: int,
                 name: str,
                 description: str,
                 count: int,
                 image: bytes,
                 purchase_price: float,
                 selling_price: float,
                 units: str,
                 barcode: int):
        self.id = _id
        self.name = name
        self.description = description
        self._count = count
        self.image = image
        self._purchase_price = purchase_price
        self._selling_price = selling_price
        self.units = units
        self.barcode = barcode

    @property
    def selling_price(self):
        return f'{self._selling_price:.2f} руб'

    @property
    def purchase_price(self):
        return f'{self._purchase_price:.2f} руб'

    @property
    def count(self):
        return f'{self._count} {self.units}'

    @count.setter
    def count(self, value):
        self._count = value

    @selling_price.setter
    def selling_price(self, value):
        self._selling_price = value
