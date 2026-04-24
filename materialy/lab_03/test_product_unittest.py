# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Laptop", 2999.99, 10)

    # --- Testy add_stock ---

    def test_add_stock_positive(self):
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.product.add_stock(-10)

    # --- Testy remove_stock ---

    def test_remove_stock_positive(self):
        self.product.remove_stock(4)
        self.assertEqual(self.product.quantity, 6)

    def test_remove_stock_too_much_raises(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(11)

    def test_remove_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(-5)

    # --- Testy is_available ---

    def test_is_available_when_in_stock(self):
        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        self.product.remove_stock(10) 
        self.assertFalse(self.product.is_available())

    # --- Testy total_value ---

    def test_total_value(self):
        expected_value = 29999.9
        self.assertAlmostEqual(self.product.total_value(), expected_value, places=2)


if __name__ == "__main__":
    unittest.main()
