#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import json
import sqlite3
import sys
from sqlite3 import Connection
from typing import Tuple, List

from models import Product
from models import Sale
from definitions import ROOT_DIR

con: Connection
dbname: str


def execute(*args, **kwargs):
    global con
    try:
        con.cursor().execute(
            *args, **kwargs
        )
        con.commit()
    except ValueError as error:
        print('ERROR:', error)
        raise Exception("Problems with database", sys.exc_info()[0])
    except:
        print(sys.exc_info()[0])
        raise Exception("Problems with database", sys.exc_info()[0])


def connect(path: str):
    global con
    global dbname
    dbname = path
    print(f'Connecting to {path}...')
    con = sqlite3.connect(f'{ROOT_DIR}\\db\\{path}.db')


def init(dbname: str):
    connect(dbname)
    create_product_images_table()
    create_products_table()
    create_sales_history_table()
    create_sold_product_table()
    create_cart_table()


def create_sales_history_table():
    execute(
        """CREATE TABLE IF NOT EXISTS sales_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        time TIMESTAMP NOT NULL
        )""")


def create_sold_product_table():
    execute(
        """CREATE TABLE IF NOT EXISTS sold_products (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        product_id INTEGER NOT NULL,
        operation_id INTEGER NOT NULL,
        count REAL NOT NULL DEFAULT 0,
        selling_price REAL NOT NULL
        )""")


def create_products_table():
    execute(
        """CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL UNIQUE,
        description TEXT,
        count REAL NOT NULL DEFAULT 0,
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
    execute("""INSERT INTO product_images (product_id, image) VALUES (?, ?)""", (product_id, image))


def create_cart_table():
    execute(
        """CREATE TABLE IF NOT EXISTS cart (
        product_id INTEGER NOT NULL,
        count FLOAT NOT NULL DEFAULT 0,
        price FLOAT NOT NULL
        )"""
    )


def add2cart(product_id: int, count: float = 1, price: float = None) -> None:
    if price is None:
        price = get_product(product_id)._selling_price
    execute(
        """INSERT INTO cart (product_id, count, price)
        VALUES (?, ?, ?)
        """, (product_id, count, price)
    )


def update_cart_product(_id, count: float, price: float) -> None:
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


def add_product(name: str = "", description: str = "", count: float = 0, image: str = "", purchase_price: float = 0,
                selling_price: float = 0, units: str = "шт", barcode: int = 0):
    image = open(image, 'rb').read()
    execute(
        """INSERT INTO products (name, description, count, purchase_price, selling_price, units, barcode)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, description, count, purchase_price, selling_price, units, barcode)
    )
    add_product_image(get_last_id(), image)


def add_sold_product(product_id: int, operation_id: int, count: float, selling_price: float):
    execute(
        """INSERT INTO sold_products (product_id, operation_id, count, selling_price)
        VALUES (?, ?, ?, ?)
        """, (product_id, operation_id, count, selling_price)
    )


def update_product(_id: int, name: str = "", description: str = "", count: float = 0, image: str = "",
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


def get_last_id(table: str = 'products') -> int:
    global con
    c = con.cursor()
    c.execute(
        """SELECT seq FROM sqlite_sequence WHERE name=? """, (table,)
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
        p._count = x[1]
        p._selling_price = x[2]
        out_cart.append(p)
    return tuple(out_cart)


# TODO: Try to make that efficient
def sell():
    time = datetime.datetime.now()
    execute(
        """INSERT INTO sales_history (time)
        VALUES (?)
        """, (time,)
    )
    # TODO: operation_id getting error fix
    # operation_id = get_last_id('sales_history')
    # for product in get_cart():
    #     add_sold_product(product.id, operation_id, product._count, product._selling_price)
    execute("DELETE FROM cart")


def get_sales_history():
    global con
    c = con.cursor()
    c.execute(
        """SELECT * FROM sales_history"""
    )
    history = c.fetchall()
    return tuple(map(lambda sale: Sale(time=sale.time, _id=sale.id)))


# init('test')
if __name__ == '__main__':
    connect('test')
    for i in map(lambda x: print(x.image), get_products()):
        pass

    input()
