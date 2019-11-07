#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List
from models.product import Product


class CartProduct:
    def __init__(self,
                 _id: int,
                 product_id: int,
                 price: float,
                 count: int
                 ):
        self.id = _id
        self.product_id = product_id
        self.price = price
        self.count = count
