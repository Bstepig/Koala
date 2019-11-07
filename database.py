#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import json
import sqlite3
from sqlite3 import Connection
from typing import Tuple, List

from models import Product
from models import Sale
from definitions import ROOT_DIR

con: Connection


def execute(*args, **kwargs):
    global con
    try:
        con.cursor().execute(
            *args, **kwargs
        )
        con.commit()
    except (NameError, sqlite3.Error) as error:
        Exception(error)
        raise Exception("Problems with database")


def connect(path: str):
    global con
    print(f'Connecting to {path}...')
    con = sqlite3.connect(f'{ROOT_DIR}\\db\\{path}.db')


def init(dbname: str):
    connect(dbname)
    create_product_images_table()
    create_products_table()
    create_sales_history_table()
    create_cart_table()


def create_sales_history_table():
    execute(
        """CREATE TABLE IF NOT EXISTS sales_history (
        id INTEGER PRIMARY KEY,
        products TEXT NOT NULL,
        time TIMESTAMP NOT NULL
        )""")


def create_products_table():
    execute(
        """CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        description TEXT,
        count INT NOT NULL DEFAULT 0,
        purchase_price REAL,
        selling_price REAL NOT NULL,
        units TEXT DEFAULT шт,
        barcode INT UNIQUE
        )""")


def create_product_images_table():
    execute(
        """CREATE TABLE IF NOT EXISTS product_images (
        product_id INTEGER UNIQUE,
        image BLOB
        )""")


def add_product_image(product_id: int, image: bytes):
    execute("""INSERT INTO product_images (product_id, image) VALUES (?, ?)""", product_id, image)


def create_cart_table():
    execute(
        """CREATE TABLE IF NOT EXISTS cart (
        product_id INTEGER NOT NULL,
        count INT NOT NULL DEFAULT 0,
        price INT NOT NULL
        )"""
    )


def add2cart(product_id: int, count: int = 1, price: int = None) -> None:
    if price is None:
        price = get_product(product_id)._selling_price
    execute(
        """INSERT INTO cart (product_id, count, price)
        VALUES (?, ?, ?)
        """, (product_id, count, price)
    )


def update_cart_product(_id, count: int, price: int) -> None:
    execute(
        """UPDATE cart SET count = ?, price = ?
        WHERE id = ?
        """, (count, price, _id)
    )


def delete_cart_product(_id: int):
    execute("""DELETE FROM cart WHERE id = ?""", _id)


def get_products(filter_str: str = '') -> Tuple[Product]:
    global con
    c = con.cursor()
    base = """SELECT id, name, description, count, 
        (SELECT image FROM product_images WHERE product_id = id) AS image, 
        purchase_price, selling_price, units, barcode FROM Products"""
    if filter_str:
        c.execute(base + """ WHERE 
        name LIKE '%{0}%'
        OR id LIKE '%{0}%' 
        """.format(filter_str))  # OR description LIKE '%{0}%'
    else:
        c.execute(base)
    products = c.fetchall()
    return tuple(map(lambda product: Product(*product), products))


def get_product(_id: int) -> Product:
    global con
    c = con.cursor()
    c.execute("""SELECT id, name, description, count, 
        (SELECT image FROM product_images WHERE product_id = id) AS image, 
        purchase_price, selling_price, units, barcode FROM Products WHERE id = ?""", [_id])
    return Product(*c.fetchall()[0])


def add_product(name: str = "", description: str = "", count: int = 0, image: str = "", purchase_price: float = 0,
                selling_price: float = 0, units: str = "шт", barcode: int = 0):
    image = open(image, 'rb').read()
    execute(
        """INSERT INTO products (name, description, count, image, purchase_price, selling_price, units, barcode)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, description, count, image, purchase_price, selling_price, units, barcode)
    )


def update_product(_id: int, name: str = "", description: str = "", count: int = 0, image: str = "",
                   purchase_price: float = 0,
                   selling_price: float = 0, units: str = "шт", barcode: int = 0):
    image = open(image, 'rb').read()
    execute(
        """UPDATE products SET 
        name = ?, description, count = ?, image = ?, 
        purchase_price = ?, selling_price = ?, units = ?, barcode = ?
        WHERE id = ?
        """, (name, description, count, image, purchase_price, selling_price, units, barcode, _id)
    )


def delete_product(_id: int):
    execute("""DELETE FROM products WHERE id = ?""", _id)


def get_last_id():
    global con
    c = con.cursor()
    c.execute(
        """SELECT seq FROM sqlite_sequence WHERE name="products" """
    )
    return c.fetchall()[0][0]


# TODO: Make getting cart in one query
def get_cart() -> Tuple[Product]:
    global con
    c = con.cursor()
    c.execute("SELECT * FROM cart")
    cart = c.fetchall()
    out_cart = []
    for x in cart:
        p = get_product(x[0])
        p.count = x[1]
        p.selling_price = x[2]
        out_cart.append(p)
    return tuple(out_cart)


def sell(cart: List[Product]):
    products = json.dumps(cart)
    time = datetime.datetime.now()
    execute(
        """INSERT INTO sales_history (products, time)
        VALUES (?, ?)
        """, (products, time)
    )


def get_sales_history():
    global con
    c = con.cursor()
    c.execute(
        """SELECT * FROM sales_history"""
    )
    history = c.fetchall()
    return tuple(map(lambda sale: Sale(time=sale.time, _id=sale.id,
                                       products=json.loads(sale.products)), history))


# init('test')
if __name__ == '__main__':
    connect('test')
    for i in map(lambda x: print(x.image), get_products()):
        pass

    input()
