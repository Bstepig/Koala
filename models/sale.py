#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List
from models.product import Product


class Sale:
    def __init__(self,
                 _id: int,
                 products: List[Product],
                 time: str,
                 ):
        self.id = _id
        self.products = products
        self.time = time
