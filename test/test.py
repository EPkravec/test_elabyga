#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from api.main import client
from api.base_product import goods


class MyTestCase(unittest.TestCase):

    def test1(self):
        res = client.get('/resources')
        self.assertEqual(res.status_code, 200)

    def test2(self):
        res = client.get('/total-cost')
        self.assertEqual(res.status_code, 200)

    def test3(self):
        for i in goods:
            res = type(i['item_quantity'])
            self.assertEqual(res, int)

    def test4(self):
        for i in goods:
            self.assertEqual(type(i['price']), int)
            self.assertTrue(i['item_quantity'], 'N is Negative Number!')

    def test5(self):
        for i in goods:
            self.assertEqual(type(i['item_quantity']), int)
            self.assertTrue(i['item_quantity'], 'N is Negative Number!')


if __name__ == '__main__':
    unittest.main()
